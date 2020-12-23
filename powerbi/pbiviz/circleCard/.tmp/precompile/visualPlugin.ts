import { Visual } from "../../src/visual";
import powerbiVisualsApi from "powerbi-visuals-api"
import IVisualPlugin = powerbiVisualsApi.visuals.plugins.IVisualPlugin
import VisualConstructorOptions = powerbiVisualsApi.extensibility.visual.VisualConstructorOptions
var powerbiKey: any = "powerbi";
var powerbi: any = window[powerbiKey];

var circleCardF5CF6180C771462CBEE4EE17CA8D2D40_DEBUG: IVisualPlugin = {
    name: 'circleCardF5CF6180C771462CBEE4EE17CA8D2D40_DEBUG',
    displayName: 'CircleCard',
    class: 'Visual',
    apiVersion: '2.6.0',
    create: (options: VisualConstructorOptions) => {
        if (Visual) {
            return new Visual(options);
        }

        throw 'Visual instance not found';
    },
    custom: true
};

if (typeof powerbi !== "undefined") {
    powerbi.visuals = powerbi.visuals || {};
    powerbi.visuals.plugins = powerbi.visuals.plugins || {};
    powerbi.visuals.plugins["circleCardF5CF6180C771462CBEE4EE17CA8D2D40_DEBUG"] = circleCardF5CF6180C771462CBEE4EE17CA8D2D40_DEBUG;
}

export default circleCardF5CF6180C771462CBEE4EE17CA8D2D40_DEBUG;