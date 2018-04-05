from Variable import *


class Main:
    """
    This program is supposed to get the uncertainty.


    This is the BSD Licence for Sympy which is used in this program

    Copyright (c) 2006-2017 SymPy Development Team

    All rights reserved.

    Redistribution and use in source and binary forms, with or without
    modification, are permitted provided that the following conditions are met:

      a. Redistributions of source code must retain the above copyright notice,
         this list of conditions and the following disclaimer.
      b. Redistributions in binary form must reproduce the above copyright
         notice, this list of conditions and the following disclaimer in the
         documentation and/or other materials provided with the distribution.
      c. Neither the name of SymPy nor the names of its contributors
         may be used to endorse or promote products derived from this software
         without specific prior written permission.


    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
    AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
    IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
    ARE DISCLAIMED. IN NO EVENT SHALL THE REGENTS OR CONTRIBUTORS BE LIABLE FOR
    ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
    DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
    SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
    CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
    LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
    OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH
    DAMAGE.



    Numpy Licence (Used in this program)


    Copyright © 2005-2017, NumPy Developers.
    All rights reserved.

    Redistribution and use in source and binary forms, with or without modification,
    are permitted provided that the following conditions are met:

        Redistributions of source code must retain the above copyright notice,
            this list of conditions and the following disclaimer.
        Redistributions in binary form must reproduce the above copyright notice,
            this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
        Neither the name of the NumPy Developers nor the names of any contributors may be used to
            endorse or promote products derived from this software without specific prior written permission.

    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS “AS IS”
        AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
        MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
        CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY,
        OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
        LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER
        IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
        THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

    """

    def __init__(self):
        self.known_variables = []
        self.unknown_variables = []
        print("Welcome to the Uncertainty finding Program")
        self.get_constants_variables()
        self.get_variables()
        for answering_round in range(25):
            if len(self.unknown_variables) is 0:
                break
            self.solve_unknowns()
            # print("Answering round", answering_round)
        self.print_variables()

    def get_constants_variables(self):
        while True:
            try:
                number_of_constants = int(input("How many measured variables: "))
            except ValueError as e:
                print(e)
                continue
            break
        for const in range(number_of_constants):
            self.known_variables.append(Variable())

    def get_variables(self):
        while True:
            try:
                number_of_variables = int(input("How many derived variables: "))
            except ValueError as e:
                print(e)
                print("Invalid Input!")
                continue
            break
        for variable in range(number_of_variables):
            self.unknown_variables.append(DerivedVariable(self.known_variables))
        print(self.unknown_variables)

    def solve_unknowns(self):
        for variable in self.unknown_variables:
            if variable.value is not None:
                print("Added", variable.name)
                self.known_variables.append(variable)
                self.unknown_variables.remove(variable)
                continue
            variable.value, variable.uncertainty = variable.solve_for_value(variable.equation,
                                                                            self.known_variables,
                                                                            variable.required_symbols)

    def print_variables(self):
        for variable in self.known_variables:
            print(variable.name)
            print("Value:", variable.value)
            print("Uncertainty:", variable.uncertainty)


Main()
