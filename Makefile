# -*- coding: utf-8 -*-

# Copyright (c) 2009, Johan Liseborn <johan.liseborn@gmail.com>
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

CTAGS = ctags -R --sort=yes
ETAGS = ${CTAGS} -e

DJANGO_ADDRESS = 0.0.0.0
DJANGO_PORT = 8000

.PHONY: run ctags clean regendb

run:
	@./manage.py runserver ${DJANGO_ADDRESS}:${DJANGO_PORT}

ctags:
	${CTAGS}

etags:
	${ETAGS}

regendb:
	rm -f wooter.db
	./manage.py syncdb
	@echo "Ready to run..."

clean:
	find . -name \*.pyc -delete
	find . -name \*~ -delete
