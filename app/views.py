from app import app, db
from flask import url_for, redirect, render_template, request, abort, current_app
from flask_admin import Admin, helpers, expose, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from app.models import User, Post, Comment, Tag, Role, People
from flask_security import Security, SQLAlchemyUserDatastore, current_user, login_required, roles_required, roles_accepted

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)


@app.route('/test1')
@login_required
def test_login():
    return f'<h2>Только для авторизованных!!!</h2>'

@app.route('/test2')
@roles_required ('admin') # должен иметь роль admin
def test_roles_req():
    return f'<h2>Только для admina!!!</h2>'

@app.route('/test3')
@roles_accepted ('admin','user') # должен иметь роль admin или user
def test_roles_acc():
    return f'<h2>Только для admina или usera!!!</h2>'

@app.route('/')
def index():
    return render_template ('index.html')

# Создаем модифицированные ModelView для показа только залогиненным юзерам
class MyModelView(ModelView):

    def is_accessible(self):
        """Проверяет, зашел ли админ в совй профиль, если да, то возвращает его, показывает основное меню с таблицами"""
        return (current_user.is_active and
                current_user.is_authenticated and
                current_user.has_role('admin')) #функция модели User

    def _handle_view(self, name, **kwargs):
        """
        Override builtin _handle_view in order to redirect users when a view is not accessible.
        """
        if not self.is_accessible():
            if current_user.is_authenticated:
                # permission denied
                abort(403)
            else:
                return redirect(url_for('security.login', next=request.url))

# Переадресация страниц (используется в шаблонах), изменение вида главной страницы админки (под главным меню)
class MyAdminIndexView(AdminIndexView):
    @expose('/')
    def index(self):
        if not current_user.is_authenticated:
            return redirect(url_for('.login_page'))  # перенаправление на страницу логина, если не зашел в свой профиль
        result = User.query.all()
        # return super(MyAdminIndexView, self).index()
        return self.render('admin/index2.html', result=result)  # рендерим измененный index

    @expose('/login/', methods=('GET', 'POST'))
    def login_page(self):
        if current_user.is_authenticated:
            return redirect(url_for('.index'))  # перенаправление на главную, если не зашел в свой профиль
        return super(MyAdminIndexView, self).index()

# Create admin
admin = Admin(app, index_view=MyAdminIndexView(), base_template='admin/master-extended.html', template_mode='bootstrap3')

# Добавляем вьюхи только для залогиненых юзеров с ролью admin из класса MyModelView
admin.add_view(MyModelView(User, db.session))
admin.add_view(MyModelView(Role, db.session))
admin.add_view(MyModelView(Post, db.session))
admin.add_view(MyModelView(Comment, db.session))
admin.add_view(MyModelView(Tag, db.session))
admin.add_view(MyModelView(People, db.session))

# define a context processor for merging flask-admin's template context into the
# flask-security views.
@security.context_processor
def security_context_processor():
    return dict(
        admin_base_template=admin.base_template,
        admin_view=admin.index_view,
        h=helpers,
        get_url=url_for
    )

