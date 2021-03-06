"""empty message

Revision ID: 98b1a5c9e520
Revises: 7006f847500f
Create Date: 2019-11-06 08:10:31.304447

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '98b1a5c9e520'
down_revision = '7006f847500f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('crawls', sa.Column('as_top', sa.String(length=10), nullable=True))
    op.add_column('crawls', sa.Column('content', sa.String(length=600), nullable=True))
    op.add_column('crawls', sa.Column('date', sa.String(length=100), nullable=True))
    op.add_column('crawls', sa.Column('id', sa.Integer(), nullable=False))
    op.add_column('crawls', sa.Column('images_count', sa.Integer(), nullable=True))
    op.add_column('crawls', sa.Column('is_boost', sa.String(length=10), nullable=True))
    op.add_column('crawls', sa.Column('is_top', sa.String(length=10), nullable=True))
    op.add_column('crawls', sa.Column('mileage', sa.Integer(), nullable=True))
    op.add_column('crawls', sa.Column('price', sa.Integer(), nullable=True))
    op.add_column('crawls', sa.Column('price_title', sa.String(length=60), nullable=True))
    op.add_column('crawls', sa.Column('product_id', sa.Integer(), nullable=True))
    op.add_column('crawls', sa.Column('region_name', sa.String(length=100), nullable=True))
    op.add_column('crawls', sa.Column('region_slug', sa.String(length=60), nullable=True))
    op.add_column('crawls', sa.Column('short_description', sa.String(length=100), nullable=True))
    op.add_column('crawls', sa.Column('site', sa.String(length=60), nullable=True))
    op.add_column('crawls', sa.Column('slug', sa.String(length=200), nullable=True))
    op.add_column('crawls', sa.Column('title', sa.String(length=100), nullable=True))
    op.add_column('crawls', sa.Column('tops_count', sa.Integer(), nullable=True))
    op.add_column('crawls', sa.Column('transmission', sa.String(length=60), nullable=True))
    op.add_column('crawls', sa.Column('url', sa.String(length=255), nullable=True))
    op.add_column('crawls', sa.Column('user_id', sa.Integer(), nullable=True))
    op.add_column('crawls', sa.Column('user_phone', sa.String(length=60), nullable=True))
    op.create_index(op.f('ix_crawls_conditions'), 'crawls', ['conditions'], unique=False)
    op.create_index(op.f('ix_crawls_date'), 'crawls', ['date'], unique=False)
    op.create_index(op.f('ix_crawls_image'), 'crawls', ['image'], unique=False)
    op.create_index(op.f('ix_crawls_price_title'), 'crawls', ['price_title'], unique=False)
    op.create_index(op.f('ix_crawls_region_name'), 'crawls', ['region_name'], unique=False)
    op.create_index(op.f('ix_crawls_region_slug'), 'crawls', ['region_slug'], unique=False)
    op.create_index(op.f('ix_crawls_short_description'), 'crawls', ['short_description'], unique=False)
    op.create_index(op.f('ix_crawls_site'), 'crawls', ['site'], unique=False)
    op.create_index(op.f('ix_crawls_slug'), 'crawls', ['slug'], unique=False)
    op.create_index(op.f('ix_crawls_title'), 'crawls', ['title'], unique=False)
    op.create_index(op.f('ix_crawls_transmission'), 'crawls', ['transmission'], unique=False)
    op.create_index(op.f('ix_crawls_url'), 'crawls', ['url'], unique=False)
    op.create_index(op.f('ix_crawls_user_phone'), 'crawls', ['user_phone'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_crawls_user_phone'), table_name='crawls')
    op.drop_index(op.f('ix_crawls_url'), table_name='crawls')
    op.drop_index(op.f('ix_crawls_transmission'), table_name='crawls')
    op.drop_index(op.f('ix_crawls_title'), table_name='crawls')
    op.drop_index(op.f('ix_crawls_slug'), table_name='crawls')
    op.drop_index(op.f('ix_crawls_site'), table_name='crawls')
    op.drop_index(op.f('ix_crawls_short_description'), table_name='crawls')
    op.drop_index(op.f('ix_crawls_region_slug'), table_name='crawls')
    op.drop_index(op.f('ix_crawls_region_name'), table_name='crawls')
    op.drop_index(op.f('ix_crawls_price_title'), table_name='crawls')
    op.drop_index(op.f('ix_crawls_image'), table_name='crawls')
    op.drop_index(op.f('ix_crawls_date'), table_name='crawls')
    op.drop_index(op.f('ix_crawls_conditions'), table_name='crawls')
    op.drop_column('crawls', 'user_phone')
    op.drop_column('crawls', 'user_id')
    op.drop_column('crawls', 'url')
    op.drop_column('crawls', 'transmission')
    op.drop_column('crawls', 'tops_count')
    op.drop_column('crawls', 'title')
    op.drop_column('crawls', 'slug')
    op.drop_column('crawls', 'site')
    op.drop_column('crawls', 'short_description')
    op.drop_column('crawls', 'region_slug')
    op.drop_column('crawls', 'region_name')
    op.drop_column('crawls', 'product_id')
    op.drop_column('crawls', 'price_title')
    op.drop_column('crawls', 'price')
    op.drop_column('crawls', 'mileage')
    op.drop_column('crawls', 'is_top')
    op.drop_column('crawls', 'is_boost')
    op.drop_column('crawls', 'images_count')
    op.drop_column('crawls', 'id')
    op.drop_column('crawls', 'date')
    op.drop_column('crawls', 'content')
    op.drop_column('crawls', 'as_top')
    # ### end Alembic commands ###
