package nodeathanimations.nodeathanimations;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import net.fabricmc.api.ClientModInitializer;

public class NoDeathAnimationModClient implements ClientModInitializer {
    public static final Logger LOGGER = LoggerFactory.getLogger("nodeathanimations");
    @Override
    public void onInitializeClient() {
        LOGGER.info("NoDeathAnimation Mod initialized");
    }
}