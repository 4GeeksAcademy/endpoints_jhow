"""empty message

Revision ID: 1694518263a8
Revises: 70216d85950d
Create Date: 2024-05-10 03:28:01.727655

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1694518263a8'
down_revision = '70216d85950d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('role', schema=None) as batch_op:
        batch_op.alter_column('description',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)

    with op.batch_alter_table('role_permission', schema=None) as batch_op:
        batch_op.alter_column('role_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('permission_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=sa.VARCHAR(length=80),
               type_=sa.String(length=250),
               existing_nullable=False)
        batch_op.alter_column('role_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('role_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('password',
               existing_type=sa.String(length=250),
               type_=sa.VARCHAR(length=80),
               existing_nullable=False)

    with op.batch_alter_table('role_permission', schema=None) as batch_op:
        batch_op.alter_column('permission_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('role_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    with op.batch_alter_table('role', schema=None) as batch_op:
        batch_op.alter_column('description',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)

    # ### end Alembic commands ###
