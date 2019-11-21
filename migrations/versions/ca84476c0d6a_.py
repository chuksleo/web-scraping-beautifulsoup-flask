"""empty message

Revision ID: ca84476c0d6a
Revises: 8ca0ba2d239c
Create Date: 2019-11-15 10:40:32.366491

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ca84476c0d6a'
down_revision = '8ca0ba2d239c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('crawls',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(length=600), nullable=True),
    sa.Column('price_title', sa.String(length=60), nullable=True),
    sa.Column('is_boost', sa.String(length=10), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('region_slug', sa.String(length=60), nullable=True),
    sa.Column('tops_count', sa.Integer(), nullable=True),
    sa.Column('as_top', sa.String(length=10), nullable=True),
    sa.Column('user_phone', sa.String(length=60), nullable=True),
    sa.Column('region_name', sa.String(length=100), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('short_description', sa.Text(), nullable=True),
    sa.Column('is_top', sa.String(length=10), nullable=True),
    sa.Column('date', sa.String(length=100), nullable=True),
    sa.Column('slug', sa.String(length=200), nullable=True),
    sa.Column('url', sa.String(length=255), nullable=True),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('images_count', sa.Integer(), nullable=True),
    sa.Column('conditions', sa.String(length=60), nullable=True),
    sa.Column('transmission', sa.String(length=60), nullable=True),
    sa.Column('mileage', sa.String(length=255), nullable=True),
    sa.Column('site', sa.String(length=255), nullable=True),
    sa.Column('image', sa.String(length=100), nullable=True),
    sa.Column('image_list', sa.Text(), nullable=True),
    sa.Column('year', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_crawls_conditions'), 'crawls', ['conditions'], unique=False)
    op.create_index(op.f('ix_crawls_date'), 'crawls', ['date'], unique=False)
    op.create_index(op.f('ix_crawls_id'), 'crawls', ['id'], unique=False)
    op.create_index(op.f('ix_crawls_image'), 'crawls', ['image'], unique=False)
    op.create_index(op.f('ix_crawls_price_title'), 'crawls', ['price_title'], unique=False)
    op.create_index(op.f('ix_crawls_region_name'), 'crawls', ['region_name'], unique=False)
    op.create_index(op.f('ix_crawls_region_slug'), 'crawls', ['region_slug'], unique=False)
    op.create_index(op.f('ix_crawls_site'), 'crawls', ['site'], unique=False)
    op.create_index(op.f('ix_crawls_title'), 'crawls', ['title'], unique=False)
    op.create_index(op.f('ix_crawls_transmission'), 'crawls', ['transmission'], unique=False)
    op.create_index(op.f('ix_crawls_url'), 'crawls', ['url'], unique=False)
    op.create_index(op.f('ix_crawls_user_phone'), 'crawls', ['user_phone'], unique=False)
    op.create_index(op.f('ix_crawls_year'), 'crawls', ['year'], unique=False)
    op.create_table('departments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=60), nullable=True),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=60), nullable=True),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=60), nullable=True),
    sa.Column('username', sa.String(length=60), nullable=True),
    sa.Column('first_name', sa.String(length=60), nullable=True),
    sa.Column('last_name', sa.String(length=60), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('department_id', sa.Integer(), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.Column('is_admin', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['department_id'], ['departments.id'], ),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_first_name'), 'users', ['first_name'], unique=False)
    op.create_index(op.f('ix_users_last_name'), 'users', ['last_name'], unique=False)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_last_name'), table_name='users')
    op.drop_index(op.f('ix_users_first_name'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    op.drop_table('roles')
    op.drop_table('departments')
    op.drop_index(op.f('ix_crawls_year'), table_name='crawls')
    op.drop_index(op.f('ix_crawls_user_phone'), table_name='crawls')
    op.drop_index(op.f('ix_crawls_url'), table_name='crawls')
    op.drop_index(op.f('ix_crawls_transmission'), table_name='crawls')
    op.drop_index(op.f('ix_crawls_title'), table_name='crawls')
    op.drop_index(op.f('ix_crawls_site'), table_name='crawls')
    op.drop_index(op.f('ix_crawls_region_slug'), table_name='crawls')
    op.drop_index(op.f('ix_crawls_region_name'), table_name='crawls')
    op.drop_index(op.f('ix_crawls_price_title'), table_name='crawls')
    op.drop_index(op.f('ix_crawls_image'), table_name='crawls')
    op.drop_index(op.f('ix_crawls_id'), table_name='crawls')
    op.drop_index(op.f('ix_crawls_date'), table_name='crawls')
    op.drop_index(op.f('ix_crawls_conditions'), table_name='crawls')
    op.drop_table('crawls')
    # ### end Alembic commands ###
