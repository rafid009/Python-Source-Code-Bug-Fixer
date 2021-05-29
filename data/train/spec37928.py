import numpy as np 

def function(x):

	w8 = x
	j7 = 8
	paths = []
	try:
		if x > 8:
			j7 = 4+1
			x = x/6
			paths.append(1)
		else:
			j7 = 3*j7
			w8 = j7*w8
			paths.append(2)
		if w8 > 0:
			w8 = w8+8
			j7 = j7+0
			j7 = w8*8
			paths.append(3)
		else:
			w8 = 5/x
			x = 8*0
			x = j7*j7
			paths.append(4)
		paths.append(5)
		assert w8 >= 0
		w8 = w8**0.5
		return w8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))