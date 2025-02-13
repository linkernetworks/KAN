# KAN API overview

KubeAI Application Nucleus for edge (KAN) API defines a common object model that describes the full stack of intelligent Edge solutions, from AI models to solutions to devices and sensors. Because these objects are defined as standard Kubernetes [custom resources](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/), you can use popular Kubernetes tools like [kubectl](https://kubernetes.io/docs/reference/kubectl/kubectl/) to manipulate these objects.

## KAN API object models

* [AI model](./object-model/ai-model.md) (```model.ai.kan```)
* [AI skill](./object-model/ai-skill.md) (```skill.ai.kan```)
* [Device](./object-model/device.md) (```device.fabric.kan```)
* [Target](./object-model/target.md) (```target.fabric.kan```)
* [Solution](./object-model/solution.md) (```solution.solution.kan```)
* [Instance](./object-model/instance.md) (```instance.solution.kan```)

## Mapping between KAN API object models and KAN portal concepts

The KAN portal experience aims to provide a streamlined experience of creating and managing intelligent Edge solutions leveraging cameras. Hence, we’ve hidden some KAN API concepts and renamed a few objects to make the UX more intuitive for target scenarios. The following table summarizes how portal concepts are mapped to API concepts:

| API Object | Portal Concept |
|--------|--------|
| ```device.fabric.kan``` | Camera |
| ```instance.solution.kan``` | Deployment |
| ```model.ai.kan``` | AI Model |
| ```skill.ai.kan``` | AI Skill |
| ```solution.solution.kan``` | There are no solutions surfaced on portal. Essentially, a portal operates on a single, system-maintained solution object on behalf of the user. |
| ```target.fabric.kan``` | Compute device | 

## Typical workflows

Depending on your focus, you can start with the AI workflow, the device workflow, or the solution workflow as described below. At the end, you can create ```Instance``` objects which represent running deployments of your intelligent Edge solution.

### AI workflow

1. Create your AI model using tools of your choice. 
2. Once you have the AI model file, register your AI model with KAN as a ```Model``` object. 
3. Then define AI ```Skill``` objects that define processing pipelines. A processing pipeline reads data from a data source, applies one or more AI models (and other transformations), and sends inference results to designated outputs.

### Device workflow

1. Register your computational devices with KAN as ```Target``` objects. You can also specify desired runtime components, such as a KAN agent, in your target definition.
2. Manually register your non-computational devices, such as sensors and actuators, as ```Device``` objects. You can also leverage projects like [Akri](https://github.com/project-akri/akri) to auto-discover devices.

### Solution workflow

1. Define your intelligent solution as a ```Solution``` object, which consists of a number of ```Component``` elements. A component is usually a container, and it may refer to AI ```Skill``` objects in its properties.
2. Define a ```Instance``` object that maps a ```Solution``` to one or multiple ```Target``` objects. Once the instance object is created, KAN ensures the impacted targets are updated according to the desired solution state and target state.

> [!NOTE]
> The current version of KAN portal doesn't explicitly expose the ```Solution``` object. Behind the scenes, you always work with a single ```Solution``` object that is automatically managed. However, you can use KAN API to examine and update the object.

## A sample workflow

Assume that you are creating an intelligent edge solution that uses a website to show number of cars passing an intersection each hour. The following workflow describes how to create and deploy such a solution using KAN API.

1. Create or select a car detection model. KAN comes with a model zoo, which contains a car detection model you can use.
2. Register the model as a KAN ```Model``` object.
3. Define a KAN ```Skill``` object that defines a pipeline that:

    * Takes input from a camera;
    * Sends frames to the car detection model;
    * Collects inference results and sends detection events to an output (such as IoT Hub or an HTTP endpoint).
    
4. Define a KAN ```Solution``` object that will create a Docker container ```Component``` that takes the ```Skill``` as input and drives the inference process. 

   Since KAN provides some containers out-of-the-box, you don't have to create these containers yousrelf.
   
6. Create your website container and add it as a ```Component``` of your ```Solution```.
7. Define a ```Target``` that represents a computer to which you want to deploy your solution.
8. Define ```Device``` objects for cameras you want to use. These ```Device``` objects are associated with your ```Target``` object through labeling.
9. Create a ```Instance``` object that deploys your ```Solution``` to your ```Target```.

## Getting started

Visit the [KAN API Quickstart](./quick_start/quick_start.md) to try out the tutorials.

## Next steps

* For more information about KAN configuration, visit [KAN Project: Setup guide](/docs/tutorial/setup-guide.md).
