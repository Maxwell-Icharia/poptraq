"""db_version_1_User_County_Admin

Revision ID: 8e7b01e72242
Revises: 
Create Date: 2018-10-16 23:32:52.686170

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8e7b01e72242'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admin',
    sa.Column('national_id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=False),
    sa.Column('surname', sa.String(), nullable=False),
    sa.Column('dob', sa.Date(), nullable=True),
    sa.Column('home_county', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('created', sa.String(), nullable=False),
    sa.Column('updated', sa.String(), nullable=False),
    sa.Column('last_seen', sa.String(), nullable=False),
    sa.Column('confirmed', sa.Boolean(), nullable=True),
    sa.Column('confirmed_on', sa.String(), nullable=True),
    sa.Column('role', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('national_id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('county',
    sa.Column('county_code', sa.Integer(), nullable=False),
    sa.Column('county_name', sa.String(), nullable=False),
    sa.Column('sub_county', sa.Integer(), nullable=False),
    sa.Column('sectors', sa.Integer(), nullable=False),
    sa.Column('population', sa.Float(), nullable=False),
    sa.Column('budget', sa.Float(), nullable=False),
    sa.Column('size', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('county_code')
    )
    op.create_table('user',
    sa.Column('national_id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=False),
    sa.Column('surname', sa.String(), nullable=False),
    sa.Column('dob', sa.Date(), nullable=False),
    sa.Column('home_county', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('created', sa.String(), nullable=False),
    sa.Column('updated', sa.String(), nullable=False),
    sa.Column('last_seen', sa.String(), nullable=False),
    sa.Column('confirmed', sa.Boolean(), nullable=True),
    sa.Column('confirmed_on', sa.String(), nullable=True),
    sa.Column('role', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('national_id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('county')
    op.drop_table('admin')
    # ### end Alembic commands ###
