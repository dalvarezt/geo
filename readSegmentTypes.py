def getSegmentTypes():
  segment_type = spark.read.format('org.apache.spark.sql.execution.datasources.csv.CSVFileFormat').option('header', 'true').load(local_cos.url('SegmentType.csv', local_bucket))
  return segment_type
