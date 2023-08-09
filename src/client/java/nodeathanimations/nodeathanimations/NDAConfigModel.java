package nodeathanimations.nodeathanimations;

import io.wispforest.owo.config.annotation.Config;
import io.wispforest.owo.config.annotation.Modmenu;

@Modmenu(modId = "nodeathanimations")
@Config(name = "ndaconfig", wrapperName = "NDAConfig")
public class NDAConfigModel {
    public boolean enabled = true;
}
