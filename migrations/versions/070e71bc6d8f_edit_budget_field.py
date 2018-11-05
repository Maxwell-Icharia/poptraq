"""Edit Budget Field

Revision ID: 070e71bc6d8f
Revises: e547021c99ee
Create Date: 2018-10-23 11:50:30.315580

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '070e71bc6d8f'
down_revision = 'e547021c99ee'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('county', sa.Column('current_budget', sa.Float(), nullable=False))
    op.drop_column('county', 'budget')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('county', sa.Column('budget', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False))
    op.drop_column('county', 'current_budget')
    # ### end Alembic commands ###