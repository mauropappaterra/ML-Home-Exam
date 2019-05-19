# Home Exam Machine Learning
# dendogram.py
# Created by Mauro J. Pappaterra on 14 of May 2019.
import sonarmini as data
import math

def point2point (a, b):
    """Given two 2D coordinate points A and B it calculates the Eucledian distance"""
    distance = math.sqrt(((a[0] - b[0])**2 + (a[1] - b[1])**2))
    # print ("Distance " + str(a) + " and " + str(b) + " = " + str(round(distance,5)))
    return round(distance,5)

def point2cluster(point, cluster):
    """Returns the shortest distances between a point and a cluster"""
    distance = 999999999

    for element in cluster:

        if (isCluster(element)):
            distance = min(distance, point2cluster(point, element))
        else:
            distance = min(distance, point2point(point, element))
    #print(str(distance))
    return distance

def cluster2cluster(cluster_a, cluster_b):
    """Returns the shortest distances between two clusters"""
    distance = 999999999
    for point_a in cluster_a:
        for point_b in cluster_b:

            if (isCluster(point_a) and isCluster(point_b)):
                distance = min(distance, cluster2cluster(point_a, point_b))
            elif (isCluster(point_a) and not isCluster(point_b)):
                distance = min(distance, point2cluster(point_b, point_a))
            elif (isCluster(point_b) and not isCluster(point_a)):
                distance = min(distance, point2cluster(point_a, point_b))
            else:
                distance = min(distance, point2point(point_a, point_b))
    #print(str(distance))
    return distance

def isCluster (element):
    """Returns true if the element is a Cluster (python list)"""
    return (str(type(element)) == "<class 'list'>")

def findShortest (setpoints):
    """Given a setpoint that might or might not contain any clusters, return shortest path in Eucledian distance"""
    distances = []

    for i,point in enumerate(setpoints[:len(setpoints)-1]):
        j  = i + 1

        while (j < len(setpoints)):

            if (isCluster(point)):

                if (isCluster(setpoints[j])):
                    shortest = cluster2cluster(point, setpoints[j])
                else:
                    shortest = point2cluster(setpoints[j], point)
            else:
                if (isCluster(setpoints[j])):
                    shortest = point2cluster(point, setpoints[j])
                else:
                    shortest = point2point(point, setpoints[j])

            distances.append({'from':i,'to':j,'distance':shortest})

            j+=1

    # PRINT TO CONSOLE
    for distance in distances:
        print ("From " + str(setpoints[distance['from']]) + " to " + str(setpoints[distance['to']]) + " distance = " + str(distance['distance']))

    return sorted(distances, key=lambda i: i['distance'])[0]

def dendogram (setpoints):

    iterations = 1

    while( len(setpoints) != 1):

        print("Dendogram -> " + str(setpoints))

        print("\nITERATION no." + str(iterations))

        new_cluster = findShortest(setpoints)
        print("Shortest path -> " + str(setpoints[new_cluster['from']]) + " to " + str(setpoints[new_cluster['to']]) + " with Eucledian distance = " + str(new_cluster['distance']) )

        setpoints.append([setpoints.pop(new_cluster['to']),setpoints.pop(new_cluster['from'])])
        iterations +=1

    print("\nFinal Dendogram -> " + str(setpoints))


# FOR TESTING PURPOSES
#dendogram([(1,2),(2,1),(5,4),(7,5)])

dendogram(data.sonarmini_short)