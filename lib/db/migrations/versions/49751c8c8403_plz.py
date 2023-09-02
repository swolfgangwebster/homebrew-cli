"""plz

Revision ID: 49751c8c8403
Revises: 
Create Date: 2023-09-01 19:33:58.913224

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '49751c8c8403'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('creators',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('entries', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('item_creator_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['item_creator_id'], ['creators.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('rules',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('rule', sa.String(), nullable=True),
    sa.Column('justification', sa.String(), nullable=True),
    sa.Column('rule_creator_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['rule_creator_id'], ['creators.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('spells',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('spell_creator_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['spell_creator_id'], ['creators.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('spells')
    op.drop_table('rules')
    op.drop_table('items')
    op.drop_table('creators')
    # ### end Alembic commands ###
