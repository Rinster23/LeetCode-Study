import unittest


class Test_MemoryModel(unittest.TestCase):

    # We will call this method from the method,
    # 'testPassingArguments' to show how arguments
    # are passed to a method and when/how they are
    # modified by that method.
    def exampleMethod(
            self,
            sname1,
            employeeNumber1,
            billingAmt1,
            accounts1
    ):
        # Just for this example, I have named the arguments
        # to this method with the same names as the
        # variables in the calling method, adding the
        # character '1' to the names so we can distinguish
        # them.

        # In the parent stack, 'sname' referenced a place on the heap
        # that contains the string, "Lee Maclin". In this -- the
        # child stack frame -- the reference was copied into 'sname1'.
        # If it references the same place on the heap, we know that
        # its value hasn't changed:
        self.assertEqual("Lee Maclin", sname1)

        # What we want to show now is that when a reference is
        # copied, it still references the same place on the heap.
        # We can demonstrate this again by making another copy
        # of 'sname1' and showing that it's in-memory id has
        # not changed.
        copyOfSname1 = sname1
        self.assertEqual(id(sname1), id(copyOfSname1))

        # We don't need the in-memory id to check whether
        # two references are the same. We can use the 'is'
        # operator as follows.
        self.assertTrue(sname1 is copyOfSname1)

        # We will now reassign sname1 to see how that affects
        # sname in the parent stack frame.
        sname1 = "Lee Maclin"

        # Is this a new reference? It is not! The compiler is
        # smart. It sees that we've used this string literal
        # before, so it gives us another reference to the
        # same string:
        self.assertTrue(sname1 is copyOfSname1)

        # Of course, we could make it a different name, say
        # "Bob Smith", and then we would get a new reference,
        # but we want to stick with "Lee Maclin" and trick
        # the compiler into making a new reference:

        p1 = "Lee"
        p2 = "Maclin"
        sname1 = (p1 + " ") + p2

        # This time, the string, "Lee Maclin" was the product
        # of a operation that the compiler did not forsee as
        # resulting in an existing string literal so it just
        # stored the new string in a different part of the
        # heap and gave us a reference to it.

        # We deliberately kept the value the same, so we can
        # separate the concepts of value and reference. The
        # value is the same but the reference has changed.
        self.assertEqual(sname1, copyOfSname1)
        self.assertFalse(sname1 is copyOfSname1)

        # We can check the parent stack frame to make sure
        # that 'sname' still references the original location in
        # memory. It does, which is to say that the reassignment
        # of 'sname1' did nothing to the variable, 'sname' in the
        # parent stack frame.

        # The same is true of reassigning any of the references
        # that were passed into this method: reassignment here
        # does not change references in the parent stack frame.
        employeeNumber1 = 2
        billingAmt1 = 508.37

        # We now want to change one of the elements in the
        # list referenced by the variable, 'accounts1'.
        self.assertEqual([549, 289], accounts1)
        accounts1[1] = 300

        # Does this change what we see when we examine the
        # 'accounts' variable on the parent stack frame?
        # It does. Both references are looking at the same
        # place on the heap. We just changed what resides in
        # that part of the heap so both references should
        # see the change.

        # We leave this method by returning a reference to
        # a new string.
        return "Bob Smith"

    # Heap vs stack and identity vs value
    def testRefVSValue(self):
        # We create a list of three integer values.
        zz0 = list((1, 5, 2))

        # This method -- 'testRefVSValue' has a
        # stack frame, a data structure for keeping
        # track of variables. As we create more
        # variables, space for them is allocated
        # on the stack of this method. All of these
        # variables are references to places on
        # the heap where objects are stored. 'zz0'
        # is a variable on the stack frame of the
        # 'testRefVSValue'. 'zz0' references a list
        # object on the heap.

        # When we exit this method, the variables
        # on its stack disapper but the objects on
        # the heap to which they were references
        # will disappear only when there are no
        # more references to them. That's the job
        # of the garbage collector, a piece of
        # code that automatically frees memory on
        # the heap when there are no more
        # references to it.

        # 'zz0' is a reference to a place on the
        # heap that contains a list object. We
        # will now copy this reference into 'zz1'.
        zz1 = zz0

        # 'zz0' and 'zz1' are both references to
        # the same place on the heap, a place that
        # contains a list object. We can confirm
        # this by comparing the in-memory id of
        # 'zz0' to the in-memory id of 'zz1'.
        self.assertTrue(id(zz0) == id(zz1))

        # This is the equivalent of using the 'is'
        # operator to check whether the two variables
        # reference the same memory space:
        self.assertTrue(zz0 is zz1)

        # We can do something that modifies that place
        # in memory.
        zz1.append(3)

        # That change is visible via both references:
        self.assertEqual(3, zz0[-1])
        self.assertEqual(3, zz1[-1])

        # ..and the two variables are still references
        # to the same object on the heap.
        self.assertEqual(zz0, zz1)

        # A list is a mutable sequence, which is why
        # we were able to modify it in place. But
        # what if we do something that creates new
        # references, for example as follows?
        sorted1 = sorted(zz0)
        sorted2 = sorted(zz0)
        # In this case, the values of the two new
        # lists are the same:
        self.assertEqual(sorted1, sorted2)
        # ..but they reference two different
        # places on the heap:
        self.assertFalse(sorted1 is sorted2)
        # If we modify one of those places:
        sorted1.append(100)
        # The two lists will neither reference the
        # same places in memory NOR contain the
        # same values:
        self.assertNotEqual(sorted1, sorted2)

        # Make sure you understand the difference
        # between modifying objects to which we
        # have two different references and
        # modifying one of two different places on
        # the heap that both originally contain the
        # same values.

    def testPassingArguments(self):
        sname = "Lee Maclin"
        employeeNumber = 1
        billingAmt = 450.23
        accounts = [549, 289]
        sname = self.exampleMethod(
            sname,
            employeeNumber,
            billingAmt,
            accounts,
        )

        # The following references didn't change. They
        # were passed into 'ExampleMethod' by being
        # copied into variables on the stack frame of
        # 'ExampleMethod'.

        # Inside 'ExampleMethod', some of the variables 
        # on its stack frame were reassigned to be
        # references to different locations on the heap.

        # Those reassignments did not impact the
        # references on the stack frame of this method.
        self.assertEqual(1, employeeNumber)
        self.assertAlmostEqual(450.23, billingAmt)

        # 'sname' was reassigned from being a reference
        # to string "Lee Maclnin" to being a reference
        # to the object returned by 'ExampleMethod' so,
        # again, the difference we see with 'sname' is
        # not a result of something that happened inside
        # 'ExampleMethod'.
        self.assertEqual("Bob Smith", sname);

        # 'accounts' references what it referenced before
        # we called 'ExampleMethod'. It references a list
        # on the heap. However, inside 'ExampleMethod',
        # we used 'accounts1' -- a reference to the same
        # list -- to change one of the values in that list.
        # We can see that change via the original 'accounts'
        # variable.
        self.assertEqual([549, 300], accounts)
