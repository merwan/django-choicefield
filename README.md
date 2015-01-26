#Output from `python manage.py test`

```
Creating test database for alias 'default'...
.E
======================================================================
ERROR: myapp.tests.tests_forms (unittest.loader.ModuleImportFailure)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/usr/lib/python3.4/unittest/case.py", line 57, in testPartExecutor
    yield
  File "/usr/lib/python3.4/unittest/case.py", line 574, in run
    testMethod()
  File "/usr/lib/python3.4/unittest/loader.py", line 32, in testFailure
    raise exception
ImportError: Failed to import test module: myapp.tests.tests_forms
Traceback (most recent call last):
  File "/home/merouane/workspace/sandbox/django-bug/venv/lib/python3.4/site-packages/django/db/backends/utils.py", line 65, in execute
    return self.cursor.execute(sql, params)
  File "/home/merouane/workspace/sandbox/django-bug/venv/lib/python3.4/site-packages/django/db/backends/sqlite3/base.py", line 485, in execute
    return Database.Cursor.execute(self, query, params)
sqlite3.OperationalError: no such table: myapp_topleveldomain

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/usr/lib/python3.4/unittest/loader.py", line 312, in _find_tests
    module = self._get_module_from_name(name)
  File "/usr/lib/python3.4/unittest/loader.py", line 290, in _get_module_from_name
    __import__(name)
  File "/home/merouane/workspace/sandbox/django-bug/bug/myapp/tests/tests_forms.py", line 3, in <module>
    from myapp.forms import DomainForm
  File "/home/merouane/workspace/sandbox/django-bug/bug/myapp/forms.py", line 6, in <module>
    class DomainForm(forms.Form):
  File "/home/merouane/workspace/sandbox/django-bug/bug/myapp/forms.py", line 11, in DomainForm
    for tld in TopLevelDomain.objects.all()],
  File "/home/merouane/workspace/sandbox/django-bug/venv/lib/python3.4/site-packages/django/db/models/query.py", line 141, in __iter__
    self._fetch_all()
  File "/home/merouane/workspace/sandbox/django-bug/venv/lib/python3.4/site-packages/django/db/models/query.py", line 966, in _fetch_all
    self._result_cache = list(self.iterator())
  File "/home/merouane/workspace/sandbox/django-bug/venv/lib/python3.4/site-packages/django/db/models/query.py", line 265, in iterator
    for row in compiler.results_iter():
  File "/home/merouane/workspace/sandbox/django-bug/venv/lib/python3.4/site-packages/django/db/models/sql/compiler.py", line 700, in results_iter
    for rows in self.execute_sql(MULTI):
  File "/home/merouane/workspace/sandbox/django-bug/venv/lib/python3.4/site-packages/django/db/models/sql/compiler.py", line 786, in execute_sql
    cursor.execute(sql, params)
  File "/home/merouane/workspace/sandbox/django-bug/venv/lib/python3.4/site-packages/django/db/backends/utils.py", line 65, in execute
    return self.cursor.execute(sql, params)
  File "/home/merouane/workspace/sandbox/django-bug/venv/lib/python3.4/site-packages/django/db/utils.py", line 94, in __exit__
    six.reraise(dj_exc_type, dj_exc_value, traceback)
  File "/home/merouane/workspace/sandbox/django-bug/venv/lib/python3.4/site-packages/django/utils/six.py", line 658, in reraise
    raise value.with_traceback(tb)
  File "/home/merouane/workspace/sandbox/django-bug/venv/lib/python3.4/site-packages/django/db/backends/utils.py", line 65, in execute
    return self.cursor.execute(sql, params)
  File "/home/merouane/workspace/sandbox/django-bug/venv/lib/python3.4/site-packages/django/db/backends/sqlite3/base.py", line 485, in execute
    return Database.Cursor.execute(self, query, params)
django.db.utils.OperationalError: no such table: myapp_topleveldomain


----------------------------------------------------------------------
Ran 2 tests in 0.001s

FAILED (errors=1)
Destroying test database for alias 'default'...
```
