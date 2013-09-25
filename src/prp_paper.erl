-module(prp_paper).
-export([init/1, to_html/2]).
 
-include_lib("webmachine/include/webmachine.hrl").
 
init([]) -> {ok, undefined}.
 
to_html(RD, Ctx) ->
    Id = wrq:path_info(id, RD),
    Resp = "<html><body>" ++ Id ++ "</body></html>",
    {Resp, RD, Ctx}.
