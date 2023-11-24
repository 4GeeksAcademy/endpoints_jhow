"""fecha de nacimiento

Revision ID: d058f4973de8
Revises: 16038e2c8ff0
Create Date: 2023-11-24 20:42:05.422212

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd058f4973de8'
down_revision = '16038e2c8ff0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint('user_fecha_de_nacimiento_key', type_='unique')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_unique_constraint('user_fecha_de_nacimiento_key', ['fecha_de_nacimiento'])

    # ### end Alembic commands ###
