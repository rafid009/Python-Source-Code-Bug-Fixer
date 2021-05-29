import numpy as np 

def function(x):

	w9 = 0
	j1 = x
	paths = []
	try:
		if j1 < 0:
			j1 = j1/4
			j1 = j1+w9
			paths.append(1)
		else:
			x = x+7
			x = x+1
			w9 = 5*w9
			paths.append(2)
		if x > 3:
			w9 = w9/7
			w9 = j1-6
			paths.append(3)
		else:
			x = x*0
			j1 = x+j1
			x = x-8
			paths.append(4)
		paths.append(5)
		assert w9 >= 0
		j1 = w9**0.5
		return j1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))