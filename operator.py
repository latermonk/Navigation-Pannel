
write a python k8s operator

import kubernetes
from kubernetes import client, config

class K8sOperator(object):
    def __init__(self):
        config.load_kube_config()
        self.v1 = client.CoreV1Api()

    def list_pods(self):
        ret = self.v1.list_pod_for_all_namespaces(watch=False)
        for i in ret.items:
            print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))

    def create_pod(self, namespace, pod_name):
        # Configureate Pod template container
        container = client.V1Container(
            name="nginx",
            image="nginx:1.7.9",
            ports=[client.V1ContainerPort(container_port=80)])
        # Create and configurate a spec section
        template = client.V1PodTemplateSpec(
            metadata=client.V1ObjectMeta(labels={"app": "nginx"}),
            spec=client.V1PodSpec(containers=[container]))
        # Create the specification of deployment
        spec = client.V1DeploymentSpec(
            replicas=3,
            template=template)
        # Instantiate the deployment object
        deployment = client.V1Deployment(
            api_version="apps/v1",
            kind="Deployment",
            metadata=client.V1ObjectMeta(name=pod_name),
            spec=spec)

        # Create Deployment
        self.v1.create_namespaced_deployment(
            namespace=namespace,
            body=deployment)
        print("Deployment created. ")

    def delete_pod(self, namespace, pod_name):
        # Delete deployment
        self.v1.delete_namespaced_deployment(
            name=pod_name,
            namespace=namespace,
            body=client.V1DeleteOptions(
                propagation_policy='Foreground',
                grace_period_seconds=5))
        print("Deployment deleted. ")
