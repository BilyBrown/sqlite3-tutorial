SELECT
  "client_intake"."UniqueID",
  string_agg( CONCAT("public"."activity_plots"."PlotID"),', ' ) AS"Plots",
  SUM("public"."gis_intake"."ga_total_gt") AS"GA Total GT",
  SUM("public"."client_intake"."Client GT Current") AS"Client GT"
FROM
  client_intake
JOIN "public"."activity_plots"
 ON client_intake."UniqueID" = "public"."activity_plots"."UniqueID"
JOIN "public"."gis_intake"
 ON client_intake."UniqueID" = "public"."gis_intake"."uniqueid"
GROUP BY"client_intake"."UniqueID", "gis_intake"."uniqueid";