"""empty message

Revision ID: 78951393921c
Revises: d122dad02dd7
Create Date: 2019-11-03 23:06:43.899886

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '78951393921c'
down_revision = 'd122dad02dd7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('crawls',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(length=600), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('crawls')
    # ### end Alembic commands ###
