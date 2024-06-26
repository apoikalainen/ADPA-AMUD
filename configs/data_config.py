def add_data_config(parser):
    parser.add_argument('--heterogeneity', help='Select whether to analyze network heterogeneity', type=bool, default=False)
    # dataset
    #   name: cornell

    parser.add_argument('--uns_directed_unw_name', help='unsigned & directed & unweighted data name', type=str, default="mooc")
    parser.add_argument('--uns_directed_unw_root', help='unsigned & directed & unweighted data root', type=str, default="./datasets/directed/unweighted/")
    parser.add_argument('--uns_directed_unw_node_split', help='unsigned & directed & unweighted data node split method', type=str, default="official")
    parser.add_argument('--uns_directed_unw_edge_split', help='unsigned & directed & unweighted data edge split method', type=str, default="direction")
    parser.add_argument('--uns_directed_unw_node_split_id', help='unsigned & directed & unweighted data node split id', type=int, default=0)
    parser.add_argument('--uns_directed_unw_edge_split_id', help='unsigned & directed & unweighted data edge split id', type=int, default=0)
    parser.add_argument('--uns_directed_unw_dimension_k', help='generate node features based on the structure topology', type=int, default=2)
    
