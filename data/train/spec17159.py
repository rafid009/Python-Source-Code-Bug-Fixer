import numpy as np 

def function(x):

	w2 = x
	j3 = 1
	x = 0
	paths = []
	try:
		if j3 > 2:
			w2 = w2-0
			w2 = w2+1
			w2 = 6*3
			paths.append(1)
		else:
			x = x*2
			paths.append(2)
		if x >= 4:
			j3 = j3/9
			w2 = x-x
			paths.append(3)
		else:
			j3 = j3/3
			w2 = j3+w2
			paths.append(4)
		paths.append(5)
		assert w2 >= 0
		w2 = w2**0.5
		return w2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))