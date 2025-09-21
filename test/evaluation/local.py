from lib.test.evaluation.environment import EnvSettings

def local_env_settings():
    settings = EnvSettings()

    # Set your local paths here.

    settings.davis_dir = ''
    settings.got10k_lmdb_path = '/data/software/jxx/EVPTrack-jxx/data/got10k_lmdb'
    # settings.got10k_path = '/data/software/jxx/EVPTrack-jxx/data/got10k'

    ###################################################################### start0
    settings.got10k_path = '/home/gzz4090/datasets/GOT-10K/full_data'
    settings.lasot_path = '/home/gzz4090/datasets/LaSOT'
    settings.trackingnet_path = '/home/gzz4090/datasets/TrackingNet'

    settings.tnl2k_path = '/home/gzz4090/datasets/TNL2K/'
    settings.lasot_extension_subset_path = '/home/gzz4090/datasets/LaSOT_EXT'
    settings.uav_path = '/home/gzz4090/datasets/UAV123/data_seq'
    settings.otb_path = '/home/gzz4090/datasets/OTB100'
    settings.nfs_path = '/home/gzz4090/datasets/nfs'

    ###################################################################### end0

    settings.got_packed_results_path = ''
    settings.got_reports_path = ''
    settings.itb_path = '/data/software/jxx/EVPTrack-jxx/data/itb'
    # settings.lasot_extension_subset_path = '/data/software/jxx/EVPTrack-jxx/data/lasotext'
    settings.lasot_lmdb_path = '/data/software/jxx/EVPTrack-jxx/data/lasot_lmdb'
    # settings.lasot_path = '/data/software/jxx/EVPTrack-jxx/data/lasot'
    settings.network_path = '/data/software/jxx/EVPTrack-jxx/output/test/networks'    # Where tracking networks are stored.
    settings.prj_dir = '/data/software/jxx/EVPTrack-jxx'
    settings.result_plot_path = '/data/software/jxx/EVPTrack-jxx/output/test/result_plots'
    settings.results_path = '/data/software/jxx/EVPTrack-jxx/output/test/tracking_results'    # Where to store tracking results
    settings.save_dir = '/data/software/jxx/EVPTrack-jxx/output'
    settings.segmentation_path = '/data/software/jxx/EVPTrack-jxx/output/test/segmentation_results'
    settings.tc128_path = '/data/software/jxx/EVPTrack-jxx/data/TC128'
    settings.tn_packed_results_path = ''
    # settings.tnl2k_path = '/data/software/jxx/EVPTrack-jxx/data/tnl2k'
    settings.tpl_path = ''
    # settings.trackingnet_path = '/data/software/jxx/EVPTrack-jxx/data/trackingnet'
    # settings.uav_path = '/data/software/jxx/EVPTrack-jxx/data/uav'
    settings.vot18_path = '/data/software/jxx/EVPTrack-jxx/data/vot2018'
    settings.vot22_path = '/data/software/jxx/EVPTrack-jxx/data/vot2022'
    settings.vot_path = '/data/software/jxx/EVPTrack-jxx/data/VOT2019'
    settings.youtubevos_dir = ''

    return settings

