"""empty message

Revision ID: 7006f847500f
Revises: abfe47bd744a
Create Date: 2019-11-06 08:06:39.296348

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '7006f847500f'
down_revision = 'abfe47bd744a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('crawls', sa.Column('mileage', sa.Integer(), nullable=True))
    op.add_column('crawls', sa.Column('transmission', sa.String(length=60), nullable=True))
    op.create_index(op.f('ix_crawls_conditions'), 'crawls', ['conditions'], unique=False)
    op.create_index(op.f('ix_crawls_image'), 'crawls', ['image'], unique=False)
    op.create_index(op.f('ix_crawls_transmission'), 'crawls', ['transmission'], unique=False)
    op.drop_index('ix_crawls_Condition', table_name='crawls')
    op.drop_index('ix_crawls_Transmission', table_name='crawls')
    op.drop_column('crawls', 'Transmission')
    op.drop_column('crawls', 'Mileage')
    op.drop_column('crawls', 'Condition')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('crawls', sa.Column('Condition', mysql.VARCHAR(length=60), nullable=True))
    op.add_column('crawls', sa.Column('Mileage', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.add_column('crawls', sa.Column('Transmission', mysql.VARCHAR(length=60), nullable=True))
    op.create_index('ix_crawls_Transmission', 'crawls', ['Transmission'], unique=False)
    op.create_index('ix_crawls_Condition', 'crawls', ['Condition'], unique=False)
    op.drop_index(op.f('ix_crawls_transmission'), table_name='crawls')
    op.drop_index(op.f('ix_crawls_image'), table_name='crawls')
    op.drop_index(op.f('ix_crawls_conditions'), table_name='crawls')
    op.drop_column('crawls', 'transmission')
    op.drop_column('crawls', 'mileage')
    # ### end Alembic commands ###
