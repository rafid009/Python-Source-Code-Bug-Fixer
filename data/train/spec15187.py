import numpy as np 

def function(x):

	j3 = x
	w3 = 6
	paths = []
	try:
		if w3 >= 4:
			w3 = w3+7
			paths.append(1)
		else:
			j3 = 9+9
			paths.append(2)
		if j3 < 6:
			j3 = j3-w3
			j3 = j3-1
			w3 = j3+w3
			paths.append(3)
		else:
			w3 = w3/9
			j3 = 6-1
			paths.append(4)
		paths.append(5)
		assert j3 >= 0
		j3 = j3**0.5
		return j3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))