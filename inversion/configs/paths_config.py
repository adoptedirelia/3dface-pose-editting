## Pretrained models paths
eg3d_ffhq = 'F:/mycode/3dface-pose-editting/inversion/utils/final_2200.pkl'
dlib = 'F:/mycode/3dface-pose-editting/inversion/utils/align.dat'

## Dirs for output files
checkpoints_dir = './checkpoints'
embedding_base_dir = './embeddings'
experiments_output_dir = './output'
logdir = '/media/data6/connorzl/pigan/S-GAN/stylegan3/pti_inversion/logs'

## Input info
# Location of the cameras json file
input_pose_path = 'F:/mycode/3dface-pose-editting/preprocess/inputs/epoch_20_000000/cameras.json'
# The image tag to lookup in the cameras json file
input_id = 'picture'
# Where the input image resides
input_data_path = 'F:/mycode/3dface-pose-editting/preprocess/inputs/crop_1024'
# Where the outputs are saved (i.e. embeddings/{input_data_id})
input_data_id = ''

# styleclip
style_clip_pretrained_mappers = 'F:/mycode/3dface-pose-editting/inversion/pretrained_models'
styleclip_output_dir = './styleclip_output/'
styleclip_temp = './styleclip_temp/'

## webui
web_pose = './preprocess/inputs'
web_pose_output = './inversion/out'
web_video_output = './inversion/video_out'
processed_pic = f'./inversion/embeddings/PTI/{input_id}/final_rgb_proj.png'

## Keywords
pti_results_keyword = 'PTI'
e4e_results_keyword = 'e4e'
sg2_results_keyword = 'SG2'
sg2_plus_results_keyword = 'SG2_plus'
multi_id_model_type = 'multi_id'

## Edit directions
interfacegan_age = 'editings/interfacegan_directions/age.pt'
interfacegan_smile = 'editings/interfacegan_directions/smile.pt'
interfacegan_rotation = 'editings/interfacegan_directions/rotation.pt'
ffhq_pca = 'editings/ganspace_pca/ffhq_pca.pt'
