"""empty message

Revision ID: adca57e64401
Revises: 94a59bb86979
Create Date: 2018-09-30 16:23:48.131070

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'adca57e64401'
down_revision = '94a59bb86979'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('county', 'budget',
               existing_type=postgresql.DOUBLE_PRECISION(precision=53),
               nullable=False)
    op.alter_column('county', 'county_name',
               existing_type=sa.VARCHAR(length=80),
               nullable=False)
    op.alter_column('county', 'population',
               existing_type=postgresql.DOUBLE_PRECISION(precision=53),
               nullable=False)
    op.alter_column('county', 'sectors',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('county', 'size',
               existing_type=postgresql.DOUBLE_PRECISION(precision=53),
               nullable=False)
    op.alter_column('county', 'sub_county',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.add_column('user', sa.Column('created', sa.DateTime(), nullable=False))
    op.add_column('user', sa.Column('updated', sa.DateTime(), nullable=False))
    op.alter_column('user', 'dob',
               existing_type=sa.DATE(),
               nullable=False)
    op.alter_column('user', 'email',
               existing_type=sa.VARCHAR(length=200),
               nullable=False)
    op.alter_column('user', 'first_name',
               existing_type=sa.VARCHAR(length=80),
               nullable=False)
    op.alter_column('user', 'home_county',
               existing_type=sa.VARCHAR(length=80),
               nullable=False)
    op.alter_column('user', 'national_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('user', 'password',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('user', 'surname',
               existing_type=sa.VARCHAR(length=80),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'surname',
               existing_type=sa.VARCHAR(length=80),
               nullable=True)
    op.alter_column('user', 'password',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('user', 'national_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('user', 'home_county',
               existing_type=sa.VARCHAR(length=80),
               nullable=True)
    op.alter_column('user', 'first_name',
               existing_type=sa.VARCHAR(length=80),
               nullable=True)
    op.alter_column('user', 'email',
               existing_type=sa.VARCHAR(length=200),
               nullable=True)
    op.alter_column('user', 'dob',
               existing_type=sa.DATE(),
               nullable=True)
    op.drop_column('user', 'updated')
    op.drop_column('user', 'created')
    op.alter_column('county', 'sub_county',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('county', 'size',
               existing_type=postgresql.DOUBLE_PRECISION(precision=53),
               nullable=True)
    op.alter_column('county', 'sectors',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('county', 'population',
               existing_type=postgresql.DOUBLE_PRECISION(precision=53),
               nullable=True)
    op.alter_column('county', 'county_name',
               existing_type=sa.VARCHAR(length=80),
               nullable=True)
    op.alter_column('county', 'budget',
               existing_type=postgresql.DOUBLE_PRECISION(precision=53),
               nullable=True)
    # ### end Alembic commands ###
