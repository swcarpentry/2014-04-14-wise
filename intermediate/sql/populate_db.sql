.separator ","

/* businesses */
CREATE TABLE business ("business_id" TEXT NOT NULL  UNIQUE,
                       "name" TEXT,
                       "address" TEXT,
                       "city" TEXT,
                       "state" TEXT,
                       "postal_code" TEXT,
                       "latitude" REAL,
                       "longitude" REAL,
                       "phone_number" TEXT);
.import businesses.csv business
delete from business where business_id = 'business_id';


/* inspections */
CREATE TABLE "inspection" ("business_id" TEXT NOT NULL ,
                           "score" INTEGER NOT NULL,
                           "inspection_date" STRING,
                           "inspection_type" STRING);
.import inspections.csv inspection
delete from inspection where business_id = 'business_id';

/* score legend */
CREATE TABLE "score_legend" ("min_score" INTEGER NOT NULL  UNIQUE ,
                             "max_score" INTEGER NOT NULL,
                             "description" TEXT);
.import ScoreLegend.csv score_legend
delete from score_legend where min_score = 'Minimum_Score';

/* violations */
CREATE TABLE "violation" ("business_id" TEXT NOT NULL ,
                          "violation_date" TEXT,
                          "description" TEXT);
.import violations.csv violation
delete from violation where business_id = 'business_id';


