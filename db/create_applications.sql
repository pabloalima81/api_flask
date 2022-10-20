CREATE TABLE applications(
   app_id      INTEGER  NOT NULL
  ,app_name    VARCHAR(16) NOT NULL
  ,role_id     INTEGER  NOT NULL
  ,is_critical BIT  NOT NULL
);
INSERT INTO applications(app_id,app_name,role_id,is_critical) VALUES (905,'sale_center',344,1);
INSERT INTO applications(app_id,app_name,role_id,is_critical) VALUES (905,'sale_center',543,1);
INSERT INTO applications(app_id,app_name,role_id,is_critical) VALUES (905,'sale_center',778,1);
INSERT INTO applications(app_id,app_name,role_id,is_critical) VALUES (594,'customer_support',437,1);
INSERT INTO applications(app_id,app_name,role_id,is_critical) VALUES (594,'customer_support',576,1);
INSERT INTO applications(app_id,app_name,role_id,is_critical) VALUES (594,'customer_support',897,1);
INSERT INTO applications(app_id,app_name,role_id,is_critical) VALUES (845,'prototype',332,0);
INSERT INTO applications(app_id,app_name,role_id,is_critical) VALUES (845,'prototype',334,0);
INSERT INTO applications(app_id,app_name,role_id,is_critical) VALUES (845,'prototype',331,0);
