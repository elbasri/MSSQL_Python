بايثون _ قواعد مايكروسوفت

يتضمن هذا المشروع سكربتات بلغة البرمجة بايثون لعمليات قواعد البيانات على مخدم مايكروسوفت. يشمل وظائف مثل إنشاء العرض، المحفزات، والإجراءات المخزنة، إنشاء اتصال بقاعدة البيانات، وتنفيذ عمليات قاعدة البيانات المحددة.


يشمل المشروع سكربتات بايثون مختلفة، كل منها يتعامل مع جوانب مختلفة في إدارة قاعدة البيانات لتطبيق محلي. الملفات المتاحة حاليا:

    الاتصال بقاعدة البيانات (conn.py): ينشئ اتصالاً بقاعدة بيانات SQL Server باستخدام إعدادات التكوين.
    التكوين (conf.py): يخزن تفاصيل التكوين مثل سلاسل الاتصال.
    إنشاء الإجراءات (createProcedure.py): سكربتات لإنشاء إجراءات مخزنة في قاعدة البيانات.
    إنشاء المشغلات (createTrigger.py): يمكن من إنشاء مشغلات قاعدة البيانات.
    إنشاء العروض (createViews.py): سكربتات لإنشاء عروض في قاعدة البيانات، مثل 'chauffeur' و 'agentGuichet'.
    حذف المشغلات (deleteTrigger.py): يوفر وظيفة حذف المشغلات الحالية.
    تنفيذ الإجراءات (execProcedure.py): يسمح بتنفيذ الإجراءات المخزنة.
    استيراد البيانات (import.py): يسهل استيراد البيانات إلى قاعدة البيانات.
    إدراج الجداول (listeTables.py): سكربتات لإدراج جميع الجداول في قاعدة البيانات.
    إدراج العروض (listeViews.py): يمكن من إدراج جميع العروض في قاعدة البيانات.

المتطلبات والمكتبات المطلوب تثبيتها

    Python 3.x
    مكتبة pyodbc للاتصال بقاعدة البيانات

كيفية التثبيت

    تأكد من تثبيت Python 3.x.
    تثبيت مكتبة pyodbc باستخدام pip: pip install pyodbc

كيفية التعاون

    إنشاء فرع من المستودع : أنشئ نسختك الخاصة من المشروع على جيتهوب.
    استنساخ المستودع : قم بنسخ المستودع المفرع إلى جهازك المحلي.
    إعداد البيئة: قم بإعداد بيئة بايثون الخاصة بك وتثبيت المكتبات المطلوبة.
    إجراء التغييرات: قم بالعمل على التحسينات

