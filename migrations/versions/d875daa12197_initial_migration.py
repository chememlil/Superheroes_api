"""initial migration

Revision ID: d875daa12197
Revises: 
Create Date: 2024-10-07 18:28:11.909992

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd875daa12197'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('hero',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('super_name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('power',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('hero_power',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('strength', sa.String(), nullable=True),
    sa.Column('hero_id', sa.Integer(), nullable=True),
    sa.Column('power_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['hero_id'], ['hero.id'], ),
    sa.ForeignKeyConstraint(['power_id'], ['power.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('hero_power')
    op.drop_table('power')
    op.drop_table('hero')
    # ### end Alembic commands ###
