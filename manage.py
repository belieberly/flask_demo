# 通过 manage.py 来执行命令行是十分有必要的，因为一些 Flask 的扩展只有在 Flask app object 被创建之后才会被初始化，所以非常依赖于应用上下文的环境，在没有 Flask app object 时，直接运行默认的 Python CLI 会导致这些 Flask 扩展返回错误
# import Flask Script object
from flask_script import Manager, Server
import main
import models

# init the manager object via app object
manager = Manager(main.app)

# create a new command server
manager.add_command("server", Server())


@manager.shell
def make_shell_context():
    """
    Create a python CLI
    :return: default import object
    type:'dict'
    """
    return dict(app=main.app,
                db=models.db,
                User=models.User,
                Post = models.Post)


if __name__ == '__main__':
    manager.run()
