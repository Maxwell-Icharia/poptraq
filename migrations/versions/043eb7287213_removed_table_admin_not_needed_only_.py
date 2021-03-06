"""Removed table Admin, Not needed, only specify roles

Revision ID: 043eb7287213
Revises: a9e08e4203f9
Create Date: 2018-10-20 04:28:36.563555

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '043eb7287213'
down_revision = 'a9e08e4203f9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('admin')
    op.add_column('user', sa.Column('status', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'status')
    op.create_table('admin',
    sa.Column('national_id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('first_name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('surname', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('dob', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('home_county', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('password', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('created', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('updated', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('last_seen', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('user', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('admin', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('national_id', name='admin_pkey'),
    sa.UniqueConstraint('email', name='admin_email_key')
    )
    # ### end Alembic commands ###
