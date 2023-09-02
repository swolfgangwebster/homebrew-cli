from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Creator(Base):
    __tablename__ = 'creators'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    entries = Column(Integer(), default = 0)
    spells = relationship("Spell", backref='creator')
    items = relationship("Item", backref='creator')
    rules = relationship("Rule", backref='creator')

    def __repr__(self):
        ent = "1 entry." if self.entries == 1 else f"{self.entries} entries."
        return f"{self.name} has {ent}"

class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    description = Column(String())
    item_creator_id = Column(Integer(), ForeignKey('creators.id'))

    def __repr__(self):
        print('\n')
        return f":::{self.name}::: \n\t{self.description}\n"
    
class Spell(Base):
    __tablename__ = 'spells'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    description = Column(String())
    spell_creator_id = Column(Integer(), ForeignKey('creators.id'))

    def __repr__(self):
        print('\n')
        return f":::{self.name}::: \n\t{self.description}\n"
    

class Rule(Base):
    __tablename__ = 'rules'

    id = Column(Integer(), primary_key=True)
    rule = Column(String())
    justification = Column(String())
    rule_creator_id = Column(Integer(), ForeignKey('creators.id'))

    def __repr__(self):
        return f":::Rule::: \n\t{self.rule} \n\tJustification: {self.justification}\n"