import os
from argparse import ArgumentParser

from nms_process import nms_process
from eval_edge import eval_edge


def main(args):
    alg = [args.alg]  # algorithms for plotting
    model_name_list = [args.model_name_list]  # model name
    result_dir = os.path.abspath(args.result_dir)  # forward result directory
    save_dir = os.path.abspath(args.save_dir)  # nms result directory
    gt_dir = os.path.abspath(args.gt_dir)  # ground truth directory
    key = args.key  # x = scipy.io.loadmat(filename)[key]
    file_format = args.file_format  # ".mat" or ".npy"
    workers = args.workers  # number workers
    nms_process(model_name_list, result_dir, save_dir, key, file_format)
    eval_edge(alg, model_name_list, save_dir, gt_dir, workers)


if __name__ == '__main__':
    # General main dir
    main_res_dir = 'results'
    data_name = 'BIPED'
    model = 'DXN'
    base_dir = os.path.join(main_res_dir,data_name+'-'+model)
    os.makedirs(base_dir,exist_ok=True)
    # At the end you will have in the base_dir, for example results/BIPED-DXN, the following folders>
    # * edge_maps= edges predicted from DXN model
    # * edge_nms=  Non-maximum-supression from edge_maps
    # * gt= GT of the dataset for evalution
    # * values = The computer results


    parser = ArgumentParser("edge eval")
    parser.add_argument("--alg", type=str, default=data_name+'-'+model, help="algorithms for plotting.")
    parser.add_argument("--model_name_list", type=str, default="hed", help="model name")
    parser.add_argument("--result_dir", type=str, default=base_dir, help="results directory")
    parser.add_argument("--file_format", type=str, default=".png", help=".mat or .npy, .png")
    parser.add_argument("--workers", type=int, default="-1", help="number workers, -1 for all workers")
    parser.add_argument("--version_detaile", type=str, default="20 epochs WD1e-8 ", help="Additional details of the model")
    args = parser.parse_args()
    main(args)


