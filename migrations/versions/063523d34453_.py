"""empty message

Revision ID: 063523d34453
Revises: 8fed86b55490
Create Date: 2024-01-27 21:49:27.156812

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '063523d34453'
down_revision = '8fed86b55490'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_admin', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('is_admin')

    # ### end Alembic commands ###