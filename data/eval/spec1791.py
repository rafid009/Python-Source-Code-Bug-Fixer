import numpy as np 

def function(x):

	j2 = 0
	t7 = 0
	x = 0
	paths = []
	try:
		if t7 > 0:
			x = x*2
			x = x/x
			paths.append(1)
		else:
			j2 = j2+7
			paths.append(2)
		if t7 > 0:
			x = x/6
			t7 = 6-4
			paths.append(3)
		else:
			j2 = 0-j2
			x = 7+t7
			paths.append(4)
		paths.append(5)
		assert j2 >= 0
		t7 = j2**0.5
		return t7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))