"""Add field for django user ID

Revision ID: 4125efc4b538
Revises: 5a8de84a8c9b
Create Date: 2018-04-24 13:28:14.883918

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '4125efc4b538'
down_revision = '5a8de84a8c9b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('token', 'token',
               existing_type=postgresql.UUID(),
               nullable=True)
    op.add_column('user', sa.Column('old_id', sa.BigInteger(), nullable=True))
    op.create_unique_constraint(None, 'user', ['name'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='unique')
    op.drop_column('user', 'old_id')
    op.alter_column('token', 'token',
               existing_type=postgresql.UUID(),
               nullable=False)
    # ### end Alembic commands ###
