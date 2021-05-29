import numpy as np 

def function(x):

	j9 = x
	t9 = x
	x = x
	paths = []
	try:
		if x > 4:
			x = 6+x
			x = 5+x
			paths.append(1)
		else:
			t9 = x/4
			j9 = j9*j9
			t9 = t9/6
			paths.append(2)
		if x < 7:
			x = 9-6
			x = 9*4
			paths.append(3)
		else:
			t9 = t9+9
			paths.append(4)
		paths.append(5)
		assert t9 >= 0
		t9 = t9**0.5
		return t9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))