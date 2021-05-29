import numpy as np 

def function(x):

	j5 = 6
	t9 = 0
	x = x
	paths = []
	try:
		if j5 >= 4:
			t9 = t9+x
			t9 = t9+j5
			paths.append(1)
		else:
			j5 = j5+x
			x = x+x
			paths.append(2)
		if x < 4:
			j5 = 2-t9
			paths.append(3)
		else:
			t9 = 5+t9
			j5 = j5*0
			paths.append(4)
		paths.append(5)
		assert t9 >= 0
		j5 = t9**0.5
		return j5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))