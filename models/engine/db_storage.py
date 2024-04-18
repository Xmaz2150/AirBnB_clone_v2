#!/usr/bin/python3
""" Database storage """


class DBStorage:
    """ Database storage """
    __engine = None
    __session = None

    def __init__(self):
        """ Constructor """
        from sqlalchemy import create_engine
        from models.base_model import Base
        from sqlalchemy.orm import sessionmaker
        from os import getenv

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Queries all objects depending on the class name """
        from models.state import State
        from models.city import City
        from models.user import User

        classes = {
            'State': State, 'City': City, 'User': User
        }

        if cls:
            query = self.__session.query(classes[cls]).all()
            dicts = {}
            new_dict = {}

            for obj in query:
                if obj._sa_instance_state:
                    delattr(obj, '_sa_instance_state')
                key = obj.__class__.__name__ + "." + str(obj.id)
                new_dict[key] = obj
                dicts[key] = obj
            return dicts
        else:
            query = []
            for c in classes.values():
                query += self.__session.query(c).all()

            dicts = {}
            new_dict = {}

            for obj in query:
                if obj._sa_instance_state:
                    delattr(obj, '_sa_instance_state')
                key = obj.__class__.__name__ + "." + str(obj.id)
                new_dict[key] = obj
                dicts[key] = obj
            return dicts

    def new(self, obj):
        """ Adds object to current database session """
        self.__session.add(obj)

    def save(self):
        """ Commits all changes of current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Deletes obj from current database session """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ Creates all tables in database """
        from models.base_model import Base
        from models.state import State
        from models.city import City
        from models.user import User

        from sqlalchemy.orm import scoped_session, sessionmaker

        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
