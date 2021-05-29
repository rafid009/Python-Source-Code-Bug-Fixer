import numpy as np 

def function(x):

	j3 = x
	t5 = 3
	x = x
	paths = []
	try:
		if x < 2:
			t5 = 1*5
			t5 = 6+x
			t5 = 4-0
			paths.append(1)
		else:
			j3 = j3*5
			paths.append(2)
		if j3 > 1:
			x = 0+x
			paths.append(3)
		else:
			t5 = t5/8
			x = 4-x
			j3 = 9-x
			paths.append(4)
		paths.append(5)
		assert j3 >= 0
		t5 = j3**0.5
		return t5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))