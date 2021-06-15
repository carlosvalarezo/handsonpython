"""alters table4 renames column completed to done

Revision ID: ff9de38f698e
Revises: 9bd382d02144
Create Date: 2021-06-15 10:31:08.497007

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ff9de38f698e'
down_revision = '9bd382d02144'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('table4', 'done', server_default=False)


def downgrade():
    op.alter_column('table4', 'completed')
