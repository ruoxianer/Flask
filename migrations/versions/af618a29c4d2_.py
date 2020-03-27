"""empty message

Revision ID: af618a29c4d2
Revises: 14ec4dce9aba
Create Date: 2020-03-13 14:53:51.310232

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'af618a29c4d2'
down_revision = '14ec4dce9aba'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admin_user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=256), nullable=True),
    sa.Column('_password', sa.String(length=256), nullable=True),
    sa.Column('is_delete', sa.Boolean(), nullable=True),
    sa.Column('permission', sa.Integer(), nullable=True),
    sa.Column('is_super', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('admin_user')
    # ### end Alembic commands ###
