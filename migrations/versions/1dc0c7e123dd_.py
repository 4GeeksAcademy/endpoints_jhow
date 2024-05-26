"""empty message

Revision ID: 1dc0c7e123dd
Revises: df1678dfb273
Create Date: 2024-05-24 00:25:51.499858

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1dc0c7e123dd'
down_revision = 'df1678dfb273'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('transactions', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_refunded', sa.Boolean(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('transactions', schema=None) as batch_op:
        batch_op.drop_column('is_refunded')

    # ### end Alembic commands ###