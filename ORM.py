from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    def __init__(self, name, email, password, address):
        self.name = name
        self.email = email
        self.password = password
        self.address = address
        
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    address = Column(String)
    
    def __repr__(self):
        return "<user(name={0}, email={1}, password={2}, address={3})>".format(self.name, self.email, self.password, self.address)

    

def main():
    engine = create_engine('sqlite:///:memory:', echo=False)
    
    Base.metadata.create_all(engine)
    
    #Create user 
    user1 = User("Jonah Kavadlo", "jkavadlo1@live.maryville.edu", "4D$qJArt2d!X", "28 Forest Crest Drive")
    print(user1)
    
    Session = sessionmaker(bind=engine)
    session = Session()
    
    #Add user to session and retreive it
    session.add(user1)
    newUser1 = session.query(User).filter_by(email='jkavadlo1@live.maryville.edu').first()
    print(newUser1)

main()