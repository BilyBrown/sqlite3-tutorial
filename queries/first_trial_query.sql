SELECT
  "client_intake"."unique_id",
  string_agg( CONCAT("public"."activity_plots"."plot_id"),', ' ) AS"Plots",
  SUM("public"."gis_intake"."ga_total_gt") AS"GA Total GT",
  SUM("public"."client_intake"."client_gt_current") AS"Client GT"
FROM
  client_intake
LEFT JOIN "public"."activity_plots"
 ON client_intake."unique_id" = "public"."activity_plots"."unique_id"
JOIN "public"."gis_intake"
 ON client_intake."unique_id" = "public"."gis_intake"."uniqueid"
WHERE public.client_intake.status IN ( 'OPEN','PENDING','IN PROCESS', 'POST' )
GROUP BY"client_intake"."unique_id", "gis_intake"."uniqueid";


SELECT
  SUM( client_intake.client_gt_current ) AS sum_of_client_gt
FROM
  client_intake
WHERE client_intake.status IN ( 'OPEN','PENDING','IN PROCESS', 'POST' ) ;