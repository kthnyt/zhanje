class OrderProcessor:
    # if mrd:
    # use mrd_to_consol mapper
    # change df to consol_df
    #  consol_df.to_sql
    # write into platform_order db is_processed
    # run it in batches, switching between platforms
    # scheduler 1 hour
    #  trigger manual bulk processing on anny order-related api call

    #  ????? ######################
    #  Trigger an asynchronous celery task to consolidated platform orders, on CSV upload
    #  Schedular to clean up afterward, if any platform orders remain unprocessed
    # celery_app.send_task("app.worker.consolidate_platform_orders", args=[template])
    # beat takes over where async does not finish processing

    @staticmethod
    def consolidate(template: str):
        # iterate thorough all platforms when scheduler is consolidating with `template='All'`
        # else deal with platform from current template
        # pd.read_sql chunk of unprocessed template orders
        # filter columns using platform_to_consol column_map
        # rename columns
        # df.to_sql
        return False
