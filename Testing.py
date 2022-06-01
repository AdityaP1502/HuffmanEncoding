"""
                                        Testing Module
"""

from Datastructures import Queue, Tree, minHeap
from random import randint
from HuffmanEncodeAndDecode import HuffmanEncoding
from memory_profiler import profile
from time import perf_counter

class Testing:
    """
    Class for testing performance and creating random testcase to test the algorithm
    """
    
    def timeis(fnc):
        def timeit(*args, **kwargs):
            start = perf_counter()
            fnc(*args, **kwargs)
            end = perf_counter()

            print((end - start) * 1000, 'ms')
            
        return timeit
    
    @classmethod
    def createRandomTree(cls, n : int) -> Tree:
        """Create Random Tree

        Args:
            n (int): # Non - Null Element in the Tree
        Returns:
            Tree : Test Tree
        """
        
        vals = [randint(0, 1000) for i in range(n)]
        chars = [chr(randint(32, 126)) for i in range(n)]

        # create n randon pair of char and integer
        arr = list(zip(chars, vals))
        
        # initialize the main root
        root = Tree(arr[0])
        temp = root
        del arr[0]
        
        stack = [root]
        
        i = 0
        
        while len(arr) > 0:
            root = stack.pop()
            
            # randomize the null location
            null = randint(0, 1)
            if null == 1:
                # left node is null
                root.right = Tree(arr[i])
                del arr[i]
                stack.append(root.right)
                 
            else:
                root.left = Tree(arr[i])
                del arr[i]
                
                stack.append(root.left)
                
                null = randint(0, 1)
                
                if len(arr) == 0:
                    break
                
                if null == 0:
                    root.right = Tree(arr[i])
                    del arr[i]
                    
                    stack.append(root.right)
                               
        return temp
    
    @classmethod
    def measurePerformance(cls, testCase : str) -> str:
        """Measure the memory used in creating huffman encoded message

        Args:
            testCase (str): Testcase to measure the performance

        Returns:
            str: Memory Consumption Report
        """
        @profile
        def measureMemory():
            encodedMessage, huffTree = HuffmanEncoding.encode(testCase)
        
        @cls.timeis
        def measureTime():
            encodedMessage, huffTree = HuffmanEncoding.encode(testCase)
        
        print("Performance Report")
        
        # can't seem to finish for a large text
        print("Memory Report")
        measureMemory()
        
        print("Time Report")
        measureTime()
        
    
    
if __name__ == "__main__":
    # testTree = Testing.createRandomTree(10)
    # testEncodedTree = Tree.encodeTree(testTree)
    # print(testEncodedTree)
    
    # testEncodedTree = "|(j,25)||(S,584)||(~,46)||(>,611)||(:,723)|(%,614)|||(a,235)|(Q,392)||(,,671)|(V,773)"
    # testTreeDecoded = Tree.decodeTree(testEncodedTree)
    # print()
    
    # arr = [1, 2, 3]
    # queue = Queue()
    
    # for i in range(len(arr)):
        # queue.insert(arr[i])
        
    # for i in range(len(arr)):
        # queue, elmt = queue.pop()
        # print(elmt)
        
    # test for minheap
    # arr = [["a", 1], ["c", 3], ["f", 3], ["g", 10], ["e", 2]]
    # arr = minHeap.heapify(arr)
    # for (i, elmt) in enumerate(arr.heap):
        # arr.heap[i] = Tree(elmt)    
    
    # newArr = [["", 3], ["", 11], ["", -1], ["", 4], ["", 6]]
    # for elmt in newArr:
        # node = Tree(elmt)
        # arr.insert(node, lambda x, y: x.val[1] < y.val[1])
        
    # print()  
    # for elmt in arr.heap:
        # print(elmt.val)
    
    text = """All rights belong to Tappei Nagatsuki, the original author of the Re:Zero series. This
is an English translation of the free web novel which is available at:
http://ncode.syosetu.com/N2267BE/216
This is not a professional translation. Some mistakes, both grammatical and logical,
are inevitable. Also, be advised that translators have a predisposition for personal
preference and the names and terminology may differ at times from what was used in
the anime or is used in the fandom at large.
Credit for this document belongs to Anon who can be contacted at:
ankaa.burner@gmail.com
https://mega.nz/#F!VNdzDYYK!nK9fNU3LeprlZSbRAnlsRg
ARC 4: ETERNAL CONTRACT
PHASE 6 CHAPTER LIST
Chapter 118: The Day Alpha Orionis Smiled 3
Chapter 119: Back Then, Even Now, Love Unchanging 19
Chapter 120: Elior Forest, Glaciated Evermore 35
Chapter 121: Help Him 75
Chapter 122: Booming Reunion 95
Chapter 123A: Guthunter VS The Shield of Sanctuary 110
Chapter 123B: Happiness Reflected on the Water 122
Chapter 124: Listen Up, Stupid 138
Chapter 125: The Roswaal Mansion Battle 153
Chapter 126: Attack of Guiltilaw, Ebony King of the Woodlands! 165
Chapter 127: The Final Day of Roswaal Mansion 182
Chapter 128: Love You to Your Blood and Guts 195
Chapter 129: —Choose Me 205
Chapter 124B: You Reflected in the Mirror 244
Chapter 125B: Starting as Revenge 257
Chapter 126B: We'll Next Meet at a Tea Party 272
Chapter 127B: Never Quit 283
Chapter 130: Faces in the Snow 300
Interlude: Each Gives Concession 319
Interlude: Emilia Faction • Warlock • Spirit • Spiritualist 334
Appendix: Advent 358
3
CHAPTER 118: THE DAY ALPHA ORIONIS SMILED
Emilia walks leisurely, with practised gait, along the unmarked trail with its tall tall trees.
She steps on grass, treads on earth, taking care not to trample on any flowers hidden beneath the
bulging roots. She feels the hard ground beneath her feet, but Emilia finds it strange—after all, she
is dreaming.
Nevermind how it goes in an ordinary dream, here she can feel the texture of the tree-bark, smell
the sweet aroma of the flowers, and feel the warmth of the breeze.
Emilia: “It's a dream world, but I can feel everything like normal. Why is that?”
Echidna: “Dream world, would be an entirely figurative descriptor for it. This is a place constructed
from the memories of the TRIAL's challenger, which drags in only the consciousness, a space fitting
for the appellation 'alternate world',. These are things withdrawn from the memory of you, the
challenger, so of course your senses can interact with this world. Conversely, if I attempt to touch
the ground or perhaps the trees, I won't feel any tactile sensation.”
Emilia: “So that's it. ...Can I go on a rampage, and turn the forest into a hodgepodge?”
Echidna: “What a barbaric and witchlike idea. Indeed you have tactile sense, but you can't influence
this world. To add, you and the living beings recreated in this world can't even touch each other.
Though, if the TRIAL were in another form then it would possible.”
Emilia: “Another form?”
Echidna: “Full of questions, aren't you. How about using your own head for once? Seek and you
shall find. Though for you, constantly spoiled and fawning on men as you are, I'd say it's outside
your capacity.”
Emilia: “Hmp...”
Emilia takes the lead, the WITCH OF GREED following behind while keeping a fixed distance.
Echidna gives her venomous lecture, sneering at Emilia's ignorance while looking thoroughly
unimpressed. But, despite that animosity, her statements are legitimate.
Emilia puts her hand to her mouth and thinks.
There is a difference between touchable memories and untouchable memories. A method for Emilia,
with only her mind present in this world, to touch the people who walk about these memories.
Emilia: “I thought about it but I couldn't get it. Tell me the answer.”
Echidna: “...”
Emilia: “What's wrong? Do you have a tummy ache?”
Echidna: “Your attitude gives me pyrosis. While it certainly feels unpleasant, if you exclude him
and my friends, the only one who could inspire such emotion in me would probably just be you.”
Emilia: “Echidna, you have friends.”
4
How nice, is the nuance in Emilia's muttering. Echidna sighs.
It seems she did not take Emilia's statement with the nicest of interpretations. Emilia hesitates on
how to reword it to make it communicate properly, when,
Echidna: “The regrets of the past that you glimpse in the TRIAL do not consist of only a single scene
for everybody.”
Emilia: “Erm?”
Echidna: “There are pasts fixed on a single moment of time which you regret. And differing from
those, there are also ongoing... for example, pasts where you regret your relationship with
somebody. In the second case, the recreated past will not be a single isolated scene, but will instead
recreate those characters as they are inside the challenger. You could speak with them, touch them,
even make happy love with them.”
Emilia: “...Okay. So that's how it works.”
Emilia nods in comprehension.
Indeed, REGRETS can have these distinctions. Some people will regret that they got in a fight with
somebody, and some people will regret everything that came in the aftermath.
Which to conquer is entirely dependant on the person.
Emilia: “You don't like me, but you answered my question for me.”
Echidna: “Because I'm just sooo nice a person, is the kind of misunderstanding I'd loathe for you to
make. I've done nothing humiliating enough for you to regard me favourably. That I wind up
answering these questions is entirely a result of my disposition.”
Emilia: “Right, right.”
It doesn't put her in the most jovial of moods, but Emilia has more or less figured out how to
interact with the icy Echidna.
Echidna definitely hates Emilia like one would hate a serpent, but Emilia cannot dislike Echidna.
She doesn't know her well enough for that.
Reasoning backwards, it means that Echidna knows Emilia well enough to hate her this much—but
she will has no chance to ask about it here.
???: “—Huhu! Ahahha! Here! This way!”
Emilia: “Eep!”
The sudden and loud voice of a young girl calling from behind surprises Emilia.
She freezes, when the little girl circles around her to run past from behind her to before her and
away. It shocks Emilia that she had managed to come so close without Emilia noticing, but she
promptly senses that this was not because of her own negligence or inattention.
The girl who overtook Emilia runs about, her long silver hair flapping in disarray.
Amethyst eyes, a well-worn children's vestment. She dashes confidently around the forest, her face
as she laughs very familiar to Emilia.
This person is her young self—back when she knew no REGRET, Emilia in a bygone time.
5
Echidna: “Utterly ignorant, but it's still astonishing how dumbly blithe she looks.”
Emilia: “Don't start saying things about little me too. And... we'll find out soon whether or not that's
anything bad.”
Such is Echidna's prejudiced judgement of the frolicking young Emilia.
Feeling a throbbing in her temples after objecting to Echidna's appraisals, Emilia grimaces.
Her contract with Puck has ceased, and her sealed memories are resurrecting one after another.
Her days spent with Mother Fortuna. Juice's group and how they brought supplies to the village.
The seal, and the FAIRIES who helped her escape the Princess Room. And, the day that she met Juice
who she wasn't meant to meet, and they became friends.
Emilia: “How did I manage to live without memory of these things, like it was completely
normal...?”
Emilia's memory was fraught with holes, but Emilia had lived without finding anything strange
about that at all.
Who knows what would have happened if she noticed the pitfalls, but without the TRIAL'S
involvement? There would be no recovering from it. Perhaps Puck, who would've known Emilia's
abnormal state better than anyone, didn't tell her about it because he understood that.
Pieces of her reviving memory still remain sleeping beyond the ajar door.
She had not been able to spy their entirety before challenging the TRIAL, but that was fine.
Here, in this TRIAL, all of Emilia's sealed memories will likely be revealed.
She can figure that something inside her will change definitively after having seen them.
Emilia: “But I'm not scared of that any more.”
Echidna: “Crying and bawling you cling to men or your father. Are you going to stop making
decisions typical of the filthy woman you are?”
Emilia: “I know they'd probably forgive me... but I don't want to do that, and for me or for Subaru
to feel disillusioned because of it. I don't want to be weak, and rationalising that I can stay weak.”
Echidna: “...Do whatever you want. All I'm doing is stockpiling yet another result in my memory.”
No matter how much spite Echidna spits, nothing can shake Emilia's nerve now.
Perhaps having perceived that over their conversation, Echidna resignedly closes her mouth.
The witch's comments have abated in their fury. Emilia gives a sigh and devotes her attention to her
past.
In front of her is Emilia, running about guilelessly. And,
???: “Please wait, Emilia-sama. It is perilous to traipse the area in this way.”
Emilia: “I'm not in danger, I'm fine. You're the one with scraped knees, Juice.”
6
Juice: “No injury to myself is anything for concern. But any injuries you may sustain are dire. Not
even my death would constitute recompense for wounds imposed on your sumptuous skin.”
Chasing the frolicking Emilia is a tall man in black habit—Juice. His stern face gives rise to a
definite gentleness and affection as he softly chides Emilia, who continues capering heedless of his
warning.
???: “Juice. The way you said that actually made it sound sooo dirty.”
Juice: “My intentions in speaking had been otherwise... never would I consider Emilia-sama in such
a manner.”
Juice is addressed by woman following behind him as he follows Emilia—a woman with short
silver hair, sharp eyes and beautiful looks.
Having spotted her, Emilia's throat feels to cramp.
Emilia: “Mother Fortuna...”
Although aware that this healthy sight of her mother is only occurring in a memory, Emilia cannot
keep herself from feeling the urge to cry.
Emilia loved her. Respected her more than any other. Even after all this time, Emilia considers
Mother Fortuna a member of her family at least as precious as Puck.
Fortuna goes to stand beside the worried-looking Juice, casting him a glance.
Fortuna: “And that's not just for Emilia, it'd sound that way no matter who you said it to. You're
supposed to be getting on in years by now, Juice.”
Juice: “Age is something which presents rather little significance to me. Speaking in reference to
living for a long duration of time, by my view even yourself and Emilia-sama would be infants.”
Fortuna: “I'm an infant by his view... hrm.”
Fortuna lowers her gaze as she mutters displeasedly.
Juice's brows furrow in concern, but Fortuna does not respond. Instead Emilia toddles back to them,
her cheeks puffed out.
Emilia: “Aaugh! Mother Fortuna, Juice, how come you're not chasing me! We're playing tag! You
have to chase!”
Juice: “Ah! My deepest apologies, Emilia-sama. The failing of this negligent Romanée-Conti, to
persist lifelong and evermore...”
Fortuna: “Don't spoil her like that, Juice. —Emilia, you do remember why your mother and Juice
started chasing you, yes? Girls who don't think about what they've done annoy your mother sooo
much.”
Emilia: “Eep!”
A hint of anger slips into Fortuna's smile, prompting young Emilia's shoulders to hitch.
7
She thinks back on why the two were chasing her, and realises that she has needlessly riled a
hornet's nest. Her face pales as she giggles in an attempt to distract from the issue, then turns and
breaks into a run and—
Fortuna: “No luck. Mother Fortuna caught you.”
Emilia: “Awuh! I'm sorry Mother Fortuna! It's not what you think! The fairies wanted to play, and
said to go outside, and so...”
Fortuna: “Girls who blame other people, or rather fairies, also annoy your mother. Do you
understand, Emilia?”
Caught in a hug from behind, Emilia panics while Fortuna speaks to her in whispers. Young Emilia
stops struggling and hangs her head dejectedly.
Emilia: “I'm sorry, Mother Fortuna. The room was so boring, and Juice is my friend so I wanted to
see him, and I just went out.”
Fortuna: “And then you ran away because I spotted you. You knew that you did something bad.
That was something you sooo shouldn't have done.”
Emilia: “I know...”
Fortuna: “You mustn't break promises. Keeping promises is important. Promises are a
representation of trust, and breaking them means betraying that trust. Don't do it.”
Close to tears, Emilia attempts to look down—when her face is caught between two hands, and she
is forced to look properly into that pair of amethyst eyes.
Fortuna: “Emilia, promise me. You'll keep your promises from now on.”
Emilia: “Mmhm... yes, I promise. I'm so sorry, Mother.”
Fortuna: “Alright. Everything's fine then.”
Having heard Emilia's teary pledge, Fortuna holds her darling daughter to her chest.
She tenderly strokes sobbing Emilia's silver hair, accepting her child's maturation with a gentle sigh.
When,
Fortuna: “Juice? What are you doing over there?”
Juice: “I-I have... w-witnessed, far too brilliant a sight... the tears... beyond my control...”
Juice squats in the shade of a tree as he presses a handkerchief to his face, bawling. Apparently
hearing that mother-daughter conversation had sent him over the emotional edge.
Seeing Juice cry both in her recovered memories and during the TRIAL leads Emilia to remember
that he was a weepy drunk. A warmth unfurls through her chest.
Fortuna: “But anyway, Emilia. These fairies you mentioned are...?”
8
Leaving aside Juice as he blows his nose with the kerchief, Fortuna gets back to a part of Emilia's
testimony that bothered her. With the topic of FAIRIES raised, Emilia looks up at Fortuna from
within her embrace, her eyes still red.
Emilia: “Oh, they're...”
Emilia: “Fairies, come here.”
Young Emilia reaches out her arm as she speaks to the world.
As if her pale fingertips were a perch, several glowing lights appear, drifting over to convene
around her hand.
Both Fortuna and Juice look shocked to witness the sight.
Fortuna: “It couldn't be, minor spirits? And so many of them. ...How?”
Emilia: “...? I talked to them, and lots of them came out. They come out when I'm playing in the
Princess Room now.”
Juice: “To conduct this sum of minor spirits at such an age... Emilia-sama, it seems that you possess
distinguishable aptitude for spiritualism.”
Emilia: “Aptytoode, for spiritualism?”
Juice: “These who you call fairies are beings known as minor spirits. Extant ubiquitously
throughout the world, open your heart to them to converse and form a contract. Those who are
favoured by spirits, and borrow their strength to achieve the extraordinary, are referred to as
spiritualists.”
Emilia: “I can be one of those?”
Juice: “Certainly. Proceed to mature in good health, favoured by spirits as is presently so...
undoubtedly, many spirits, and more powerful spirits, will come under your direction.”
Emilia's face beams as she hears Juice's explanation.
But Fortuna stands up, and nudges her elbow into Juice's side.
Fortuna: “Hold on, Juice. No funny talk. Going off saying that managing a few minor spirits makes
you a spiritualist... and, Emilia doesn't need it.”
Juice: “So might be how you opine, but Emilia-sama shall not remain a child indefinitely. It will
happen that she cannot stay at your side. My belief would find its additional necessity in her
establishment of herself as herself once that eventuality comes.”
Fortuna and Juice, arguing over where Emilia's education should be focused.
Watching their exchange from aside, the older Emilia inevitably has to think it.
Emilia: “Mother Fortuna and Juice are like a mom and dad.”
Fortuna: “Wh!?”
9
Without a trace of ill will in her expression, young Emilia states the exact thing that older Emilia
thinks.
Emilia watches Fortuna's face redden while agreeing with the fact that, yes, her younger self had
thought the same thing.
Fortuna: “Okay, Emilia, don't say anything weird. Your mother and Juice have known each other for
a very very long time, our relationship isn't one you can talk about like that.”
Juice: “Exactly, Emilia-sama. Fortuna-sama and myself have known each other for a very long
time... in fact, it would have been since being in the company of your mother and father...”
Fortuna: “—Juice.”
Fortuna starts with a frantic explanations, but Juice's loose lips lead her tone to plummet. Juice
seems to sense his mistake as he puts his hand to his mouth.
Juice: “Forgive me.”
Emilia: “Mother, and father?”
Fortuna: “I'm sorry, Emilia. We'll talk about that another time. But anyway you go back to the room.
I haven't forgiven the fact that you snuck out.”
Emilia: “Hrmp... You're so mean, Mother Fortuna...”
Feeling that Fortuna is trying to fudge the conversation, Emilia puffs out her cheeks to display her
displeasure. But Fortuna appears stubborn, and puts her hands to Emilia's puffed cheeks, pressing
down to make her expel the air.
With the air puffed out of Emilia's mouth, Fortuna goes down to match Emilia's eye level.
Fortuna: “Be a good girl, behave. This isn't the last time you're going to get to see Juice. I'll, erm...
make another chance for you to see him.”
Emilia: “Really!? You promise? No going back on it?”
Fortuna: “Oh, no, this girl. Just where could she've learned to be so fussy?”
Fortuna gives Emilia a wry smile as she brings up the previously-covered topic of promises, before
taking her in an embrace.
Fortuna: “Yes, I promise. This is a promise between you and me, and it's sooo important.”
Emilia: “...Okay then. I'll go back to the room.”
Young Emilia gives Fortuna a trusting nod.
Released from the hug, Emilia runs over to Juice before she can start her return to the Princess
Room. She extends her hand to Juice, smiling.
Emilia: “See you, Juice. Promise that we'll meet again.”
10
Juice: “—Yes, assuredly. May we make audience again in the future. I shall be awaiting the day.”
Juice takes the small, extended hand, completing the handshake.
With her smile met with a smile, Emilia nods and nods and nods before releasing her hand and
announcing her goodbye.
Young Emilia readies to return to the Princess Room—
Echidna: “Here they are.”
Whispers Echidna, having silently watched over everything until now.
Emilia hears Echidna clearly and raises her head, looking around to try and determine what Echidna
is referring to—and spots it.
Emilia: “—”
A white young man.
White skin, white hair. He wears a simple shirt and pants, nothing ornate about him. His face does
have its looks, but even said he is lacking in anything defining, his appearance utterly banal.
He could mix into a crowd and disappear instantly with how he epitomizes all lack of individuality,
but his presence right here, right now, makes him seem an abnormal kind of outsider.
Fortuna: “...Who're you!?”
Fortuna in the memory also notices the man, immediately holding Emilia close as she voices her
clear caution.
The man leans against a tree trunk and runs his hand through his white hair.
Man: “Don't you think it follows reasonable sense that when asking a person for their name, you
begin by introducing yourself first?”
The reply makes Fortuna's eyebrow twitch.
Seeing this, the man's mouth twists, the atmosphere he emits dismal.
Man: “Who, is one of those questions where when you give this response I can only think it as stale
and trite but, now that I've actually wandered into a context fitting for that kind of thing why aha I
can indeed understand why people have the urge to say this. Here are fellow persons for the first
time making the presence of the other. Our standings are supposed to be definitively equal as we
begin in our efforts to establish a relationship, but now we have a condescending someone trying to
extort a name unilaterally. I wonder if it's occurred to you. That you're unconsciously,
unsympathetically, and by your own accord treating me as inferior, has that occurred to you?”
Fortuna: “...For a man, you sure love talking.”
Man: “For a man, is where your prejudice shows though and indicates how ignorant you are to
comparative examples of men. And first of all what right do you think you have to take these
creatures called MEN, a class which includes more individuals spread throughout the world than
what is conceivably countable, and compare me to them? This attitude of yours... it's giving me a
little trouble to overlook. It's all lacking in any degree of reasonable courtesy. It's taking this
individual I am, taking my rights, and disregarding them.”
11
It appears that Fortuna's every word has made the lunacy in the man's speech escalate.
With the man growing more and more dangerous, Fortuna exposes her wariness as she braces
herself for combat. But the one to pull the breaks is Juice, standing beside her.
He looks up at the white man, his expression stern as he opens his mouth to speak:
Juice: “Regulus Corneas! For what reason are you here! We had an immutable promise that I would
be the only one involved in this affair!”
Regulus: “Call it an immutable promise or call it whatever you want, it's all just you going off
saying things yourself and presuming things yourself in what is actually just a normal agreement.
Look at you trying to push people into submission with that domineering phrasing of yours, what
great and pompous drivel you've started spewing from your spirit mouth. Trying to restrict my daily
actions, even though I'm not permitted any kind of perfidious behaviour anyway... so that's what a
spirit is? Have you ever considered putting a stop on the infringements you're making to my mind
and person?”
Juice: “Nothing you say presents an answer! If you were displeased with the agreement, we could
have discussed it at church! What have you appeared here for! And who told you that this place
is...”
???: “—This has happened on my instruction.”
Juice's voice trembles in rage as he yells at the displeased young man, Regulus.
But cutting into their argument, never once before heard in this altercation, comes a woman's voice.
Everyone watching the scene has their own reaction to that voice.
A shiver arises in Juice's eyes, Fortuna's eyes blaze in fury, young Emilia shakes her head as she
tears up in her mother's arms, Regulus crafts an ominous smile.
Emilia as she watches the memory swallows her breath, while Echidna merely closes her eyes.
She comes forward, this single girl.
This character standing beside Regulus as he looks down at Emilia, Juice, and Fortuna, is a girl so
beautiful that all who see her would tremble.
Her long, platinum hair gleams sweetly as if sunlight given form, flowing to her slender neck and
streaming down her back.
Long eyelashes border her eyes, their shade so deep a blue that they seem to entrap the world, her
looks so overwhelmingly attractive that even a god would hesitate to touch her fingers, with all her
perfect pulchritude.
Her petite frame is adorable enough that even having the wind cradle her appears risky. What garbs
her is merely a single white cloth, and the whole aura of it suggests that the world would permit
nothing else to touch her skin.
The presence she holds is not that of an ordinary person, and her appearance is not what an ordinary
person would have.
Her voice possesses an almost magical allure, binding the minds and bodies of those who hear it,
12
nobody present here capable of saying anything any more.
Girl: “Is there something wrong? Cardinal Betelgeux Romanée-Conti?”
Tilting her head, the girl fires her question.
Being looked at by her, being talked to by her. Just the fact that any one of her actions are aimed at
oneself is enough to inspire an overwhelming euphoria, such that death would not be an aversive
prospect, the sensation unavoidable.
Although she knows that this is the past, Emilia feels her mouth rapidly going dry as she looks at
the girl.
—This thing is dangerous.
Juice: “Why are you... no, Regulus Corneas! Why have you brought her here!”
Juice grits his teeth, rejecting the emotions swelling up inside him.
—This thing, is dangerous.
Regulus: “Do you think it's possible for me of all people to pull any such stunt as 'bringing people
places' with how it infringes on the will of others? It is by her own volition that we are in company.
Your attempts to make all of this my fault are yes an amazing exhibition of prejudice. I'd appreciate
you not to go off passing your unasked-for judgements on this human being that I am.”
Girl: “Cardinal Regulus. He is rattled. Do not fault him too much.”
The corners of Regulus's mouth tremble in a frantic attempt to keep ecstasy from showing on his
face as he bows respectfully.
It's strange.
Regulus is overwhelming, alien. That he is so obediently obeying her will illustrates beyond any
parallel how abnormal this girl is.
Juice looks up at the girl, his eyes trembling in shock and confusion as he shakes his head.
Juice: “That is... remarkably, cruel... Pandora-sama...”
Juice's breathy voice leads the girl to smile faintly.
This girl's smile, blessed by the world and harbinger of even greater felicity. The girl, Pandora,
answers all the gazes aimed at her with a tolerance that permits everything.
She spreads her arms wide, as if her small reach will cradle everything in existence.
Pandora: “Now, shall we begin? —For the fulfilment of cardinal desire of us witch cultists.”
Fortuna: “PANDORAAAAAAAAAAAAA!!”
With young Emilia protected behind her, Fortuna thrusts out her arms to generate a blue magic
circle before her. Icicles materialize with overwhelming momentum, their aim set directly on
Pandora.
13
Pandora: “Goodness.”
Fortuna: “Be impaled, and apologize to my brother and the rest!!”
Pandora casually puts her hand to her mouth. Fortuna strikes.
Each of the icicles is as large an adult's arm, and their number is near to twenty. They form at
speeds fast enough to be continuous, shooting one after another—spearing into the astonished girl
before exploding into white vapour.
The crackling of shattering ice rains upon the crackling of shattering ice without end, the white
smoke cloaking over the surroundings as Fortuna regardless relents not a second in her attack.
Young Emilia's mouth gapes open with Fortuna standing before her, her beautiful face twisted in
rage as she hoists up her arms.
Fortuna: “AaAand now—!!”
Following the motion of her arms as she swings them down, a ball of ice massive enough to
decimate the forest trees plummets down from above. Its aim is true as it slams into the spot where
Pandora was, white demise drilling itself into the forest ground, marking the grave.
Not even the older Emilia has anything she can say about Fortuna's overwhelming magical prowess.
Even supposing that Emilia had Puck's help, like hell she could handle magic that proficiently. She
had never made low estimations of her mother, but learning that her strength was greater than what
she remembered makes her shiver.
However,
Regulus: “Say... you were paying me absolutely no attention during any of that, were you? You
weren't paying me even the slightest thought and you still opted for an attack that would entangle
me in it, honestly don't you find that suspect? Do you know what it means? What it means is that
you infringed upon my presence, my life, my rights.”
Immediately following the protracted complaint, the massive ball of ice shatters to pieces from the
ground-up.
The shards of ice-crystal scatter through the air, dreamlike, the sight of Regulus casually standing
there being overwhelming abnormal. The sight of Pandora standing beside him uninjured, also.
Regulus makes a show of easily brushing off his coat. Despite the ferocity of the attack he sustains
not a single injury, in fact not even his clothes are sullied in the least. Pandora adjusts her bangs
slightly, disrupted by air pressure as they are.
Most likely Regulus, standing before Pandora, had protected her—but it's all preposterous. Emilia
has not a clue as to what happened.
Echidna: “So that's this generation's Greed. Considering what an impossible fluke of a meeting it is
for me to be witnessing this, it really is very fascinating.”
Emilia: “You know what that was?”
Emilia addresses Echidna, who has moved out of the tree-shade and into a spot where she can better
observe the fight. Echidna glances at Emilia, her eyes narrowing.
14
Echidna: “I can make a guess, but it's far from anything definite. If we can keep watching this for a
little longer, I might be able to figure out what's going on, but... It doesn't seem that circumstances
will allow for that.”
Emilia: “What do you...”
Echidna: “There they go.”
Although frustrated, Emilia directs her gaze forward.
Even with Fortuna's offensive, the fight has produced zero results.
Seeing Regulus stepping forward and looking displeased, Juice stretches out his arm.
Juice: “Fortuna-sama, I ask that you take Emilia-sama and withdraw! We are presently powerless
against Regulus Corneas!”
Fortuna: “You...! That woman is right there, and you're telling me to stand down!?”
Juice: “Consider the situation! Who is it that you are protecting in this instant!”
Fortuna: “—!”
Juice bellows at the belligerent Fortuna. Fortuna's face stiffens in shock as she glances behind her,
to find young Emilia holding anxiously onto her mother's clothes.
Emilia: “M-Mother...”
Fortuna: “Emilia!”
Juice: “Please withdraw. From there, rescue the village. The followers who accompanied me to this
place share me in my feelings. They will surely aid you.”
Fortuna: “If we do that, what will you do?”
Fortuna bends down and holds Emilia to her chest, while Juice speaks calmly.
She stands up with Emilia in her embrace, looking anxiously at Juice.
Juice: “—Please calm your worry. I am not remaining behind absent of any plan.”
Juice, although exuding tension, responds to Fortuna's concerned gaze with a smile.
Seeing it, Fortuna closes her eyes.
Fortuna: “I'm coming back to help you.”
With that, Fortuna breaks into a run through the forest, Emilia in her arms.
Emilia struggles in her grip, peeks her head out from over Fortuna's shoulder.
Emilia: “JUICE!!”
15
Juice: “—”
Juice turns to glance at Emilia, his expression somehow relieved as he raises his hand.
With that, and with Fortuna and Emilia sprinting deep into the forest, Juice disappears from the
couple's view.
Emilia: “...It's strange. Me, I was taken away, so I shouldn't be seeing what happens here.”
Echidna: “Don't disparage my architecture of these worlds of memory. Your memories may be the
starting point, but the construction comes from my algorithms and takes reference from the Book of
Wisdom. To an extent, it's simple to compensate for the events which you haven't seen. Although...”
Standing aside the bewildered Emilia, Echidna's gaze tracks the path of Fortuna's escape.
Echidna: “Speaking for the sake of overcoming your TRIAL, it's correct that we follow them. What
do you think? Should we transition over?”
Echidna indirectly announces that Emilia ought to follow Fortuna. Which rationally speaking is a
correct statement. The TRIAL is concerned with Emilia's past, so she should be prioritizing whatever
young Emilia is seeing and doing now. But,
Emilia: “Echidna... that kind of sounded like you're trying to make me go that way.”
Echidna: “...”
Emilia: “Me overthinking... isn't it. Your phrasing and attitude just then was weird.”
Echidna: “...Whatever you think is up to you. And also, this side's moving again as well.”
Echidna goes without answering Emilia's question, her expression blank as she steps back a small
distance. Her retreat is probably to avoid getting showered any side-damages from the imminentlystarting
fight.
No matter how terrible the damages are, nothing will affect Emilia or Echidna. But if anything
alters the surroundings, they can not avoid the impact that will have on the earth they are standing
on.
Regulus: “Well wasn't that cool of you, Betelgeux. But whose permission do you think you have to
be doing these things? Do you have any idea at all why I'm here? Think about it in any way you can
possibly conceive, and it's obvious I'm here on business. Not with you, with the other one. You
getting in my way here means you're obstructing me from doing what I ought to do. It's infringing,
my rights.”
Juice: “Say anything you wish, Regulus Corneas. But, with my being at stake, I must not allow you
any passage further!”
Regulus: “Well said. Not that I could give less of a care about the founder of the Witch Cult, but
how wonderfully said, when it was some smidgen of past contributions that landed you in the seat
you're occupying. How can you possibly believe that you have any hope of beating me, properly
chosen into my seat as I am?”
16
Juice: “That... I will now present.”
Regulus's anger intensifies over the course of his egotistical strings of logic. Juice responds quietly.
His hand reaches into his vestments, his expression steeled with resolve. To Emilia it looks the
expression of a man resolved for DEATH.
Emilia: “No... Juice, what are you doing!?”
Emilia's vicarious experience of her past has led her to remember her nickname for him.
With the situation such that he is resolved for death, Emilia promptly reaches out her arm in an
attempt to stop him. But the present Emilia has no means to influence the past.
Her outstretched hand passes through him, feeling no touch of the palm that she had grasped in her
youth.
Regulus: “That's...”
From his pocket, Juice withdraws a small, black box.
Regulus's brows furrow at first, but he promptly seems to guess at the thing's identity as his eyes
shoot open wide. With Regulus showing shock for the first time, Juice's resolute gaze pierces
through him.
Juice: “You should be able to sense it. Your hands have also held it once before.”
Regulus: “I am aware. Very aware, and so my jaw's too busy gaping at your abject stupidity for me
to speak. Perhaps you were keeping that hidden on your person thinking it'd be your ace or
whatever else idea you've come up with, but couldn't you tell from the moment you had it anywhere
near you? You! Are unqualified to have that! It wasn't anything else, it's the thing that's decided
that!”
Juice: “...Indeed, my compatibility with it is none. Owing to that, I have merely held what was
entrusted to me and nothing else. However, it also serves for the sake of junctures such as these.”
Pandora: “Cardinal Betelgeux Romanée-Conti.”
Juice responds quietly to the infuriated Regulus.
Pandora, not having moved an inch from her original spot, cuts into their conversation.
Juice raises his head. Pandora's face is tranquil.
Pandora: “Happy travels.”
Juice: “—”
No hostility or goodwill or ill will or nothing, just simple words of blessing.
And so being, Emilia cannot prevent her horror, and neither can Juice.
The blessing almost looks to have butchered Juice entirely as he grimaces, enduring the pain. He
twists the box in his hand, taking off the lid.
Inside the box upon his palm is a black, squirming SOMETHING.
17
Juice: “I beg you forgive me, Flugel-sama.”
With that, Juice presses both the dark something and the box to his chest.
Instantly, the something snaps onto Juice's body like droplets of water, compounding in volume
explosively to envelop him wholly.
It's as if Juice is being absorbed by some viscous creature. Emilia shrieks in silent grief as the
SOMETHING shrouds Juice's body, constricts him.
Regulus: “Imbecile.”
Spits Regulus, for the first time phrasing his judgements succinctly.
His scornful gaze is fixed on Juice, enveloped in the SOMETHING as he hoists his arms to the
heavens, his mouth agape and shrieking. Not as if in pain, not as if in joy, but as if some other
emotion is throwing his being into disarray.
Emilia: “—”
A baffling sound joins the shrieking.
The sound of someone clapping their hands.
Pandora: “Magnificent.”
Whispers platinum Pandora as she gives her applause.
As she watches Juice, swallowed and panting in the wake of the emotional torrent, her cheeks
redden in ecstasy.
The slight hitch in her breathing is, unmistakably, because the scene is exciting her.
Regulus: “Pandora-sama?”
Emilia is not the only one with questions about Pandora's attitude, for Regulus speaks.
He furrows his brows at the clapping Pandora. She glances back at Regulus with her cheeks still
red, aborting her applause to point at Juice.
Pandora: “Cardinal Regulus Corneas.”
Regulus: “Yes.”
Pandora: “He is coming.”
Instantly, Regulus flips to hang upside down, and goes flung hurtling high into the sky overhead.
Regulus: “Wha—?”
It's the same kind of infantile violence as grabbing a doll by the leg and flinging the thing away.
Regulus has not a clue as to what is happening either, making a dumb noise as he hits the apex of the
throw—only to slam back down to the earth. Having obviously transcended terminal velocity in his
fall, it seems he had been thrown with his LEG STILL GRABBED.
Helpless, Regulus smashes to the ground head-first.
Out thunders the echoing boom as the earth bursts apart, the trees caught in the crash falling and
18
falling in sequence toward Regulus's point of impact. The secondary attack pins Regulus beneath
the lumber, silence falling upon the forest.
Emilia falls speechless, her blank mind working frantically to figure out what on earth just
happened.
She didn't see a single thing. But supposing there is something that she did make out—
???: “I am sure I did... INFORM.”
Fallen to his knees and robed in black vestment, blood streams from the man's eyes as he gazes
forward.
Glaring at the gaps between the trees and the rising plumes of dust, breathing ragged and having
turned his resolve into a victorious bet, is this man.
Freed from the agony of being shrouded in black SOMETHING, he stands.
He is—not Juice. This man, is Betelgeux Romanée-Conti.
Betelgeux:
“I will not allow you to pursue them... you shall pass—NO FURTHER!!”
19
CHAPTER 119: BACK THEN, EVEN NOW, LOVE UNCHANGING
Streaming tears of blood and gritting his teeth, Juice shrieks.
Emilia cannot stop the goosebumps from running down her spine.
Until a moment ago, a black SOMETHING had been trying to subsume Juice's body. It has stopped
gorging on the outside of him, and presently squirms within him.
Juice's body spasms, pitches, beneath his black vestments.
The blood seeping through the thick fabric gives suggestion of how gruesome his state is, and
informs that an unimaginable nightmare is unfurling in his interior.
Emilia: “Juice...”
What on earth did Juice put inside him?
And what was that attack that toppled Regulus? It was like she couldn't see what was happening,
and gives Emilia a sense of deja vu.
It's almost as if, just a little while ago, she had witnessed the exact same—
???: “You have proven your resolve magnificently. Cardinal Betelgeux Romanée-Conti.”
A breezy female voice interrupts Emilia's thoughts.
The calm speaker is Pandora, looking down at Juice as he breathes raggedly and spits blood. Even
while watching Regulus shunt into the sky, her tranquil countenance had remained utterly unshaken.
Pandora: “You have done well to subsume that witch factor, being that you are unqualified. With
my name as Pandora, I confer to your resolve and to your ironclad will the seat of SLOTH.”
Juice: “Do you believe that I desire any SUCH SEAT? My present desires total merely to one. Without
a moment of regret for my sacrifice, the safety of that family!”
Fortuna and Emilia are gone from the warzone.
Juice had resolved to stake his lifeblood on their escape. Pandora's brows perk up in surprise, when
a redness flushes her cheeks, her smile intoxicated.
Pandora: “Love. Very wonderful.”
Juice: “It is an emotion that you will NEVER UNDERSTAND!”
Pandora, persistently transcended and aloof. Juice, prepared to fight to the end.
He supports himself painfully on one knee as he raises his trembling arm, forcing his bloody eyes
wide as he screams:
Juice: “Authority of SLOTH—Unseen Hand!!”
Overwhelming pressure bursts from Juice's position.
But Emilia's eyes cannot discern the nature of this force. Juice had merely extended his arm and
yelled, yielding no visible changes in the world.
Even so,
20
Emilia: “The forest's being torn down!?”
Throughout the area surrounding Juice, as if beset by invisible serpents, out spreads the aftermath of
destruction. Trees snap, earth shatters, clumps of dirt and grass scatter through the air.
Juice: “Aaau... aaaaAAAAAAAAAA!!”
All while indiscriminately ravaging Juice's surroundings, the destruction answers to his scream as it
directs it path toward Pandora. Although faced with demolition akin to an oncoming giant, trampling
over the woods, she shows no indications of moving from that spot.
So being, the destruction proceeds on its course, capturing the small Pandora and—
???: “Say.”
Juice: “—!?”
???: “I came here, I'm present here, so what do you think you're doing in moving the situation along
without paying the slightest of mind to me? Giving and wantless as I am, I still have to think that
about now's a suitable enough time for me to be angry.”
The instant the invisible serpent reaches Pandora, a white figure cuts into the attack's path.
His hair fluttering, Regulus's raised hand has stops the shockwave. An impact which would kill any
ordinary person washes over him as he simply stands there, absolutely nothing happening to him. Or
even that is understating it. He had been slammed into the ground with a force strong enough to
burst the earth apart, his body supposedly buried in the soil, and forget about injuries: there isn't
even a speck of dirt on him.
Emilia: “No way...”
Her hand to her mouth, Emilia is speechless.
His safe return from Fortuna's surprise attack she could at least understand. If he possessed combat
ability far exceeding that of Fortuna, then perhaps he had managed to defend against the lethal
attack.
But Juice's invisible strike presents a different story. There is no white fog to obstruct Emilia's view
this time—she had plainly witnessed Regulus be thrown into the air, and slammed into the ground.
He had, undefended, been slammed into the ground.
There was still some million in one chance that it hadn't wounded him.
But the absolute lack of dirt or soil or whatever filth on him is beyond any explanation.
There's some kind of trick, preventing attacks from—no—preventing outside effects from
influencing Regulus.
Juice: “Regulus Corneas!”
Regulus: “Can I say how unpleasant it is? The factor has not acknowledged you, and there you are
ignoring your bodily collapse to force the thing into submission. You don't think that's an insult to us
who reached our seats by way of proper process? That it doesn't wound the unwavering speck of
pride I have in myself?”
In line with the swing of Juice's arm, Regulus's face rebounds.
21
His neck rotates as if he's been punched, but when he promptly returns his head to proper position,
not a trace of the blow besmirches his face. He simply furrows his brows in displeasure, undefended
as the consecutive punches proceed to batter him.
Echidna: “I don't think staying here will show us any particular developments.”
Juice's offensive to Regulus' defensive as he mercilessly repels the attacks.
Emilia watches her old friend staking his life in the battle, when Echidna addresses her from behind.
Emilia glances back, glaring the expressionless witch.
Emilia: “You're telling me to leave? But look at what happened to Juice, how frantically he's
trying!”
Echidna: “Though, the question of whether his efforts are going to reach a desired result does leave
some room for debate. And unfortunately, I have no intentions of debating with you. It doesn't
interest me to torment the weak, and hearing even one extraneous syllable out your mouth is the
pinnacle of unpleasant.”
Emilia: “Then it should be fine for us to stay quiet and watch. I'll...”
remain here, and see Juice's resolve through to the end.
But when she goes to make that assertion, Emilia's own heart keeps her from saying anything.
The hand fails to touch anything at her chest, and so she recalls why she came here. It was to
challenge the TRIAL and overcome her past, is why.
Emilia is currently witnessing her legitimate past, which she wanted to forget.
Juice's fight here assuredly did happen, and perhaps its outcome is what she ought to watch over,
rather than what became of Fortuna and young Emilia.
—But that would be taking Subaru's feelings, having seen her off, and Juice's feelings, having
attempted to secure Emilia and Fortuna's escape, and betraying both of them.
What happened to Fortuna and Emilia after Juice presented them their escape?
She needed to unearth more of her slumbering, unrecovered past, and reveal the answer.
Echidna: “It seems like even your deficient brain can understand which decision is wiser.”
Emilia: “...You're right. Let's follow me and Mother. Will Juice...?”
Echidna: “Don't worry, it's a battle between Cardinals of Sin. The scales won't tip in either of their
favours so easily. It's another story supposing that someone else joins the fight... but, it's
inconceivable that she would involve herself in battle anyway.”
The ferocity of Juice and Regulus' fight compounds.
Blood trails from Juice's eyes, his nose, his mouth. Correspondent with the escalation of damage
ransacking his insides, the unseen destruction he manipulates shoots up in accuracy and force.
But Regulus remains so unchanged and ordinary that it's abnormal. Even with the destruction
showering his undefended form, he merely stands there with a bored expression, looking down
upon Juice's resistance.
It practically feels like, if he chose to go on the offensive, the situation's trend would instantly shift.
22
Pandora: “Hauauh...”
Echidna's gaze spears through to Pandora, heart racing and expression aroused.
Indeed, it seems that she is not going to involve herself in the fight. A beautiful girl faced with an
abnormal battle, panting rather sexually—leaving all that strangeness aside,
Echidna: “I'm changing the scene. —To you and your mother, escaped into the forest.”
Emilia: “—oop,”
Echidna raises her hand and clicks her fingers.
Everything in Emilia's vision warps as the forest scenery shifts, the false feeling of the ground
beneath her feet being covered over with something new abruptly leading her to stumble.
She raises her head. No destruction has reached this section of the forest, this familiar spot.
???: “No! Mother, no! Please don't leave me!”
Hearing the shrill voice of a crying child, Emilia jerks her head up.
What she faces is a familiar tree—with its inside hollowed out and re-purposed into a room large
enough to shelter a small child, what herself and her mother called the PRINCESS ROOM.
Fortuna and crying young Emilia are conversing outside its entrance.
Emilia clings to Fortuna's chest. Fortuna grasps her daughter's shoulders, and frantically,
Fortuna: “Please listen to me, Emilia. Everything's okay. I'll come... yes, I'll deal with this quickly
and come right back. So please stay hidden here while I'm doing that. Please.”
Emilia: “No! I don't wanna! Mother Fortuna, you're making a face like Juice did! Like Juice did,
what're you gonna do! L-leaving me, what're you... going to...”
Emilia's little hands cling desperately to keep her mother from escaping.
Fortuna should be easily capable of untangling herself from a child's grip if she wanted to. Her
reasoning for not cruelly untangling herself from Emilia's hands is evidenced by her amethyst eyes
as she gazes at Emilia.
Fortuna is Emilia's mother. So she cannot bat away the hands of her crying, clinging daughter.
Emilia: “Don't leave me! Let me be with you! I won't tell lies any more! I won't break promises! I'll
be a good girl, I'll be a good good girl... so don't leave, me...”
Fortuna: “Emilia... Emilia, Emilia, Emilia!”
Not wanting to be separated from her mother, and willing to sacrificing everything so that she does
not have to separate from her mother, Emilia shrieks. Fortuna, her expression breaking down with
emotion, hugs her daughter tight. If she does not press her daughter's face to her chest as she is,
she'd see it.
Her daughter would see her mother's expression, see the overflowing and unceasing tears, see the
teardrops wetting her mother's cheeks.
23
Emilia: “Mother, Fortuna...”
Young Emilia had not seen her mother crying, but older Emilia clearly did.
Emilia had never imagined that her perpetually noble, marvellous, strong, respectable, not even
weak in the slightest mother, had ever been so wounded and assuaged with sorrow that she cried
such feverish tears.
As she watches her mother cry, the onlooking Emilia hits her limit.
Unable to put her hands to her cheeks in time, the tears in her eyes arise one after another.
Having seen this, having seen her mother's face in this instant, she understands.
Not that she had ever doubted it, but truly in this second, she is again convicted.
Emilia: “Mother Fortuna... was, my real mother...”
Her birth mother, whoever she was, doesn't hold any significance to Emilia now.
As if Fortuna's insistence that she was just a substitute could ever make Emilia forget that she was
her real mother.
Although spoken by precious and respected Mother Fortuna as they were, those words alone were
ones that Emilia could not accept.
Emilia: “I love you, Mother Fortuna...”
As if anyone could say anything to make this feeling bend.
???: “Fortuna-sama—!”
A man's voice calls out to Fortuna from behind as she holds Emilia close.
Fortuna wipes her face with her sleeve, hiding her torrent of tears as she turns to face the speaker.
Her gaze lands on an elf man in lightweight dress.
He is one of the elves who lives in this village, and someone who Emilia knows too.
Fortuna: “Arch, how is the village?”
The man runs over while Fortuna questions him in regular voice. The man, Arch, looks to have
noticed that Fortuna was crying, but goes without touching on the topic and shakes his head.
Arch: “It's the same everywhere. The Cardinal's subordinates and the village's men are reciprocating
the fight, but...”
Fortuna: “Isn't looking good, then.”
Fortuna lowers her gaze, biting her lip at the poor state of the battle.
Emilia looks anxiously up at her mother, saying nothing as she grips her clothes and trembles.
Arch notices her shaking.
Arch: “It's okay. You don't have to be scared, Emilia. Believe in all us villagers, us adults. And
besides, your mother is a very strong, very scary person.”
Emilia: “Mm, mm...”
24
Fortuna: “Arch, was that 'scary' really necessary? Geez...”
Fortuna crosses her arms in indignation. But she does nod to Arch's indirect words of consideration:
We can't stay utterly pessimistic about this, and gazes at the Princess Room.
Fortuna: “Hiding her here won't work any more, will it.”
Arch: “Frustrating as it is, staying in the forest means they'll find her before long. Could their goal
be...?”
Fortuna: “The seal deep in the woods, likely. Where did they find out about it? And even that
woman!”
Fortuna seems to have particular hostility toward Pandora's presence as she bites her lip in
frustration, before giving a strong shake of her head.
Fortuna: “It's fine, but anyway, I'm going. I'm the strongest fighter in this forest, this isn't the time
for me to be dragging feet over here.”
Arch: “No! We will be the ones to fight! Fortuna-sama, you take Emilia and exit the forest!”
Fortuna: “What will running away accomplish? Have our peacelands stolen from us... that logic
isn't going to stop me. Us losing isn't the problem here. The problem here is having them disclose
the seal!”1
Fortuna beats back Arch's yells with an even stronger tone.
And, embarrassed that she snapped back at him,
Fortuna: “I'm sorry.”
Fortuna: “I know you resent me. There was honestly no reason for all of you to get wrapped up in
this. When Emilia and I came... placed burdens you didn't need.”
Arch: “No! As if there could possibly be any one of us who thinks that!”
Fortuna: “Arch...”
Arch responds ferociously to Fortuna's regretful voice, as if this alone is something he must not
allow her to say. His face reddens, his long elfin ears tapering back in fury.
Arch: “Please stop constantly excluding us from your problems! With our long lifespans, perhaps it
may have only felt like the blink of an eye... but even so! We spent the same time together, saw the
same things together! Have you forgotten that!?”
Fortuna says nothing.
1 The word used for 'disclose' more commonly means exposing something hidden to the public, but has a second
meaning of 'graverobbing' which might(?) have potential to be the correct meaning in this context.
On reflection if you take it extremely literally 'disclose the seal' works fine for both meanings. WONDERS of language.
25
Arch: “Who could possibly think ill of you! When we have great debts to you, your brother... to
Emilia's mother, how could you ask that we shamelessly forget what we owe!”
His emotions detonating, Arch pleads Fortuna while practically in tears.
The yet-young elf breaths raggedly as he falls to his knees, sniffling as he looks up at Fortuna. She
closes her eyes in silence.
Fortuna: “I'm sorry. —Once again, I've invalidated the family I live with.”
Arch: “Fortuna-sama... I-I may have, said too...”
Fortuna: “No, it was important that you did. I'm sorry, Arch. And thank you.”
Fortuna gives kneeling Arch her thanks, and presents him her hand. After a moment of hesitation,
Arch takes Fortuna's hand and quietly stands back up.
Fortuna turns to face Emilia.
Fortuna: “Emilia. You Mother has an important role she has to fill to protect everybody. We're going
to be separated for just a little bit.”
Emilia: “D-don't, Mother. I... I...”
Fortuna: “Please. It's only for a little bit, so please listen. Go with Arch, and leave the forest. This
forest is... going to be, sooo dangerous soon.”
Speaking to Emilia, who borders on tears as she shakes her head, Fortuna glances back to Arch.
Her determined amethyst gazes makes Arch's skinny body go rigid.
Arch: “For-Fortuna-sama... I,”
Fortuna: “Arch. You're still young, and have a future. Please take Emilia, and... I know it's a hard
world to live in, but there has to be hope.”
Arch: “I... don't say these things as though it's the end! I-I'm staying in this forest to the last, with
everybody!”
Fortuna: “Please, Arch, Emilia. She's my, my brother's, my sister in law's, daughter.”
Arch: “—!”
This was merely the voice of a frail woman, absent of Fortuna's strength and nobility.
Hearing the voice of this woman and mother, Fortuna, tears stream down Arch's face.
Arch buries his face in his hands as he sobs.
Arch: “It isn't fair...! When you hear something like that, you know it's impossible to refuse...! I,
want to fight with everyone! But!”
Fortuna: “I'm sorry. For pushing everything onto children, please forgive us.”
Fortuna puts her hands on the shoulders of the crying young elf, begging for forgiveness.
26
Arch says nothing, but accepts Fortuna's request.
Now, the people that Fortuna must persuade here amounts to only Emilia.
Fortuna: “Emilia”
Emilia: “No! I, I wanna be with you, Mother! Please! I ask please! Please, let me be with you! I
don't wanna, be alone...”
Fortuna: “You're not alone at all. Listen closely.”
Emilia bawls, unreceptive. She puts her hands over her ears, trying to shut out every word of her
mother's goodbye, which makes older Emilia want to pull her young self's cheeks taut.
Not to punish her for disobedience. But so that she cannot escape from a single syllable of any of
the words that Fortuna is going to speak.
Fortuna: “Emilia.”
Fortuna squats down. Hugs Emilia.
She takes Emilia's arms in her grasp, stops her from plugging her ears, and when her daughter acts
out by pressing her head against her, Fortuna nuzzles her cheek against her daughter's silver hair. As
though touching something, someone, more beloved than any other, taking care so that they will not
break.
Fortuna: “Your Mother is always right there with you. Right there when you close your eyes, in
your memories. Right there when you cradle yourself, in your heart as it grows warm. Right there
when you call out, beneath the same sky that your voice echoes. You and Mother are always
together. Always, always, forever... together.”
Emilia: “Liar. Liar, liar, liar... You're lying, Mother...”
Fortuna: “Emilia. —Promise.”
Emilia attempts to discard her mother's words as being mere consolation, when Fortuna looks her in
the eye and speaks. The word PROMISE leads Emilia to swallow her breath, shut her mouth.
Led by Fortuna's gaze to her outstretched palm, young Emilia too, places her palm to Fortuna's.
Fortuna: “Emilia and her Mother will always be together. That's what I promise you.”
Emilia: “Y-you'll, really... be with me?”
Fortuna: “Yes, really. More than anyone else in the world, your Mother loves you, sooo much, Lia.”
The tender call of 'Lia' is what makes the dam of tears for young Emilia, for old Emilia, burst.
Sobbing and bawling, two Emilias present and past.
Emilia: “Mother Fortuna... l-love you too... love you, love you...”
Emilia: “I love you. I love you, Mother Fortuna. Love you, sooo much, love you, treasure you...”
The emotions of the two Emilias overlap as they frantically answer to the love given to them.
27
They strain their voices, press their bodies close to her, to show that should they do otherwise they
will fail to convey, fail to express, all of these feelings in their hearts.
Fortuna: “Love you, Lia.”
On her cheeks, eyelids, forehead, Fortuna's soft warm lips touch her.
Although permitted to share touch, to share embrace, Fortuna had been late to learn how to express
love as a mother, and never would do such things—making this the moment that Fortuna truly, from
the bottom of heart, first accepted herself as being Emilia's mother.
Fortuna: “—I'm counting on you, Arch.”
Arch: “...Understood.”
Having conveyed her absolute love to her daughter, Fortuna stands and calls for the young man.
Arch receives the bawling Emilia from Fortuna, holds her firm, and gives Fortuna one big bow of
his head.
Fortuna: “Get away safely.”
Arch: “I will... Yes, I will! I won't let Emilia... won't let this girl be hurt by anybody!”
Fortuna's cheeks relax in relief.
She points to a road deeper into the forest.
Fortuna: “That way. I'm begging you.”
Arch: “—”
Arch breaks into a run, toward where Fortuna is pointing, saying nothing.
In his hold as he sprints through the forest, Emilia peeks her head out from behind his shoulder—to
sight her mother as she grows distant. She cries out, but makes no sound.
Fortuna's sharp eyes soften so tenderly,
Fortuna: “—I love you, Emilia.”
※ ※ ※ ※ ※ ※ ※ ※ ※ ※ ※
Held by Arch, Emilia looks frantically in the direction where her mother has disappeared.
Like she's begging, that consistently staring like this might make her vanished mother reappear.
Like she's hoping, that perhaps she'll come to follow them.
Arch: “Emilia!”
Emilia's stubborn spirit communicates well to Arch as he holds her small form.
Arch's face turns into a mess as he considers what to tell her young heart, having undergone
separation with Fortuna.
28
Echidna: “—I'm surprised.”
Says Echidna to Emilia, the two running side-by-side in pursuit of Arch.
Still affected by the parting with her mother, and not quite suppressing her weeping, Emilia
questions Echidna using only her gaze. The white-haired witch shrugs.
Echidna: “That you didn't stay behind there, and followed your past self without hesitation. I was
certain that it'd be like before when watching Sloth, that you'd protract the scene with your mother
so girlishly.”
Emilia: “...I know I told you before. I'm here to watch my past through! Mother, and Juice, and
everyone... that's why they...”
Echidna: “Mmhm, mmhm. Said something unasked for, didn't I?”
Looking like she did not get the answer she wanted, Echidna shakes her head.
Even Emilia has to feel irritated with Echidna's callousness, but before she can mention it, young
Emilia buries her face in her hands.
Emilia: “Why? Why? How, come this... happened? I-it's, because I... I, broke my, promise... and left
the, room...”
Arch: “No. No, Emilia. It's not your fault at all! It's not Fortuna-sama's fault, it's not anybody's
fault! There's no need to blame yourself!”
Emilia: “But then, how come? How come, we're separated? Mother... and Juice too, how come... do,
do they hate me? Lots of, heaps of people, hate me so, this's why it...”
Her incredibly sudden parting with Juice and Fortuna has cornered Emilia's heart right to the
precipice of breaking.
Thinking back on what foreboded this situation, and on her own actions, young Emilia sinks into a
sea of self-invalidation.
She broke her promise. She left the room she wasn't meant to leave. She knew about the seal she
wasn't meant to know about. It looks like everything that caused this started by her own deeds.
Emilia: “Should I've... stayed there, stayed in the room? If I did, would, nobody be gone... and I
could, be with everybody?”
Arch: “Emilia...”
Emilia: “Was, I a bad girl...? Is everybody, in the world going to, hate me... and, I'll be alone?”
Arch: “No... No, Emilia! Nobody, there's nobody out there who hates you. The world isn't here to
hurt you. ...The world's here so that everybody can celebrate you!”
Arch frantically tries to persuade the bawling Emilia.
Part of is an attempt to stop Emilia's crying, but a larger part is much like a wish—because he
himself would like to believe it.
29
Arch's shouts strike older Emilia's heart.
It wasn't just Fortuna and Juice. He and the other villagers had all protected her, loved her, reached
out to her to make sure she wasn't alone.
It was not until this exact instant that she truly remembered: it had always, always been like this.
???: “You over there—!”
With a sharp shout, somebody slinks into the space before Arch as he runs.
The black-robed character bounds out from a gap between the trees, which prompts Arch to stop
immediately and for his gaze to grow wary. But the man raises his hands in response.
Man: “Wait, don't panic! I'm one of Cardinal Romanée-Conti's fingers!”
Arch: “The Cardinal's...!”
Hearing Juice's name from the puffed man in the robes makes relief arise on Arch's face. The man
approaches after seeing Arch lose his wariness, and notices Emilia.
Finger: “That girl... then, Fortuna-sama couldn't possibly be...?”
Arch: “There's no need for concern. She's... She has merely entrusted me with Emilia, and left us
together. Fortuna-sama is the most skilful of any of us in the village. She will surely defeat the
trespassers, and...”
Finger: “...Though I find this hard to state, I'm afraid that's a difficult prospect.”
The man lowers his gaze, his voice weak.
Arch raises his brows. The man sighs, his expression grave.
Finger: “We have confirmed the presence of the Cardinal of Greed, and our Cardinal has entered
into combat with him. Were that the only problem, and we repelled the extremist members of the
faith, it might be possible for us to drive them away, but...”
Arch: “Some other issue has...?”
Finger: “—The witchbeast BLACKSNAKE has been loosed in the forest.”
Arch: “—!?”
Arch is stunned.
He shakes his head in disbelief, gesturing to the forest.
Arch: “That's ridiculous, impossible! The Blacksnake is even less controllable than the White
Whale or Sizeable Hare! It's not the White Whale, under Gluttony's command, or the Sizeable Hare,
whose course can be guided... the Blacksnake is just a natural disaster which listens to nobody! A
catastrophe among catastrophes! How!”
Finger: “...The Witch Cult's Pandora-sama has accompanied him. Pandora-sama cannot go so far as
to control the Blacksnake with her authority, but she can lead it to a destination.”
30
Arch: “Pandora? That isn't a name I've...”
Finger: “She exists in secrecy! In the Witch Cult she is taboo not to be spoken, neither by the
Cardinal's faction of moderates nor by the extremists. Now she has come here.”
Arch's shock keeps him from saying a single word.
Arch's failure to sink into despair results from the heartbeat of the life in his arms. Results from his
knowledge that he is not permitted any pessimism.
Arch: “Fortuna-sama has stated that I am to lead Emilia to her escape. Regardless of what may
happen to the forest, this girl... this hope, must be protected!”
Finger: “...I will accompany you. Although I cannot say how much this frail person of mine can
assist.”
Arch's persistent will to fight leads the man's crestfallen look to recover into determination.
He casts his robe open, revealing rather stout muscled legs and for his age, breaking into a run as he
takes the lead along the path out of the forest.
Finger: “We'll proceed while taking care to avoid the extremists. Now, if we can just exit the forest,
prospects should be—”
brighter. But in that exact instant,
Something entangles the leg of the man in the lead, leading him to fall. He topples onto his side as
Arch cries out and panickedly runs toward him.
But the man shouts to the approaching Arch,
Finger: “Stay back!!”
Arch: “—!?”
Finger: “My blunder... but to think it came so quickly!”
The man uprights his fallen body. But, upright himself is all he does. His legs, for some reason, do
not move an inch.
Beneath his overturned vestments—marks like black burn wounds besmirch his exposed shins.
Finger: “It's the vile tongue of the Blacksnake! Flee!”
Arch: “But!”
Finger: “I am already beyond saving...”
The man's face rapidly begins to change in appearance.
His skin from the neck up steadily drowns in dark, mottled marks, the eyes of his gentle-looking
face bulging open, eyeballs close to falling out as his face sinks in.
His fingers claw at his mottled neck, his mouth spilling massive quantities of yellow froth.
Finger: “ghb, bgbhgh... ahgbh, bgh...”
31
Immediately following his agonized moan, his eye sockets, his nostrils, his ears, his mouth, every
single orifice begins leaking with dingy blood, strangling his life to nothing as it gushes away.
While of course it goes for Arch, with Emilia also being subject to witnessing the pitiful death,
neither can keep their usual composure. Even Echidna's expression looks scrunched up in pain.
Arch: “Potpourri of Pestilence... Witchbeast of Blight, the Blacksnake!”
His voice strained, Arch states the name of the man's killer, the beast.
While surely it could not have been in response to that call, a forest silent but for Arch and Emilia's
breathing abruptly becomes host to another noise.
The slopping, of a large animal licking its lips.
The slithering, of something long and thin slinking across the earth.
The noise is on a ridiculously incorrect scale, and it's hard to really pin down. But it almost
resembles the noise of a serpent faced with prey, its tongue flicking out, as it squirms across the dirt.
Arch: “—Fuck!”
Having guessed the true identity of the sound, Arch realises that himself and Emilia are right in the
middle of the Blacksnake's hunting ground.
Although aware that yelling only acts to their disadvantage, he has to yell. He can think of no other
methods to rebel against the thing.
Although unsure of where to run, Arch sprints away from the man. He has not a single thought for
Fortuna's directions any more. Right now, he must escape from this threat. Must protect that what
must be protected.
The frantic resistance of that young elf—
Arch: “Ahg—”
—is cruelly crushed as a vile, black tongue ensnares his right ankle.
The areas of bare skin which the tongue licks are besmirched with dark, mottled burn scars.
The instant he sees it, Arch aims his open palm at his foot.
Arch: “...FULA!!”
Without hesitation, he fires a blade of wind to sever his scarred leg from the shin down.
He loses his footing, and props his falling body on a tree trunk. Blood spurts from him, the
agonizing pain soldering his brain as he endures, gritting his teeth so hard that they fracture.
Arch: “Humaauh!”
A crack sounds through the air as Arch's severed stump begins freezing over. White mist transpires,
Arch shrieking as he forces his bleeding to stop.
His gruesome deeds stun older Emilia silent. Instant decisions, counteracting the pain. And his
strength of heart, having not released Emilia from his hold even after all of this.
32
Emilia: “Arch...?”
With her head pressed to his chest, young Emilia had not witnessed Arch's actions. Neither did Arch
have any intention in the least to let her see them.
Even with his face covered in cold sweat, he gives Emilia a clumsy smile.
Arch: “It's... nothing... I'm... all fine!”
Although his speech falters, Arch replies so as to not let Emilia sense anything is wrong.
But cruel fate laughs ever on at the spirit of this noble man.
His leg has been severed, his frantic deeds done to plug the bleeding of his stump—as the uninjured
portions of his frozen leg look to dehydrate, fissuring like a plane of earth bereft of water, the
damage spreading.
It's as if Arch's leg is dying like a dry wasteland. And it isn't stopping at just the leg.
Arch: “...Emilia. Do you see the white flowers between those two trees?”
Emilia: “...Mm.”
Arch squats down the with the tree supporting his back. Having alighted to the ground, Emilia looks
where Arch is pointing, and nods as she spots the white flowers.
Arch wipes the sweat from the brow. Hides his agony.
Arch: “Can, you run to those flowers? Run, past the flowers... go straight... go straight, ahead...”
Emilia: “I, can. I can. But...”
Arch: “Then, get running—”
Although confused, young Emilia now recognizes that Arch is in incredibly irregular straits, her
amethyst eyes wavering.
Wavering because she will be alone. Because again, she will lose someone.
Arch: “Everything's okay. Emilia, you, won't be alone...”
Emilia: “Arch...”
Arch: “Now, run off. No matter what you hear, don't look back... run!”
Arch's sharp command makes Emilia's shoulders hitch, and with that, Emilia runs. She withstands
the urge to look back, instructed as she is not to do it.
Arch's words, Fortuna's words, Juice's words, all echo through Emilia's brain.
So that she can believe: If she does everything as she is told, everything will go back to normal.
So that she can convince herself: keeping by instructions is the only hope she currently has.
Running away, leaving him behind, Arch watches Emilia disappear into the direction of hope.
He gives a long sigh. Rolls up the sleeve of his jacket.
33
The dehydration has already covered his legs and waist, having come as far as his abdomen.
He can move neither of his legs, and in fact it seems that just touching them will be enough for
them to shatter and disintegrate.
Once the dehydration reaches his chest, gets to his heart, what will happen?
He hears the slithering of the beast, faced with prey.
He hears a slithering, noise like it's plotting to take the fleeing girl, the forest's hope, the
significance of Arch's expenditure of the faint life he had left, and steal it.
Arch: “Like anyone could let you get away...”
The slithering stops its retreat.
As if it has regained interest, in the still-living prey.
The noise approaches. Meaning, although he senses that end is approaching, Arch's cheeks relax.
The fact that death is looming in on him means that death is growing distant from the girl.
Arch: “I know she'll be okay, Fortuna-sama.”
The end slithers closer.
He hears it, and although exposing himself to mortal danger beyond parallel, Arch's pride in his
achievements leads him to smile.
Arch: “—”
That smile, even though parched arid, remains without ever going dry.
※ ※ ※ ※ ※ ※ ※ ※ ※ ※ ※
—Emilia has long passed the white flowers.
Emilia: “Hahh... hahh... hauhhh...”
Her breathing hitches as she demands long strides from her little legs while dashing through the
forest.
All while thinking about her mother and Juice and Arch, focused on the idea that running in this
direction Arch indicated is the best thing she can do, not going to consider anything else.
Emilia: “Auhh... aaaaauah!”
She shakes her head.
The tears flow. Desperately, she keeps the sobs from pouring out her lips.
What was happening, and why was it happening?
Everybody knew something, and she didn't know anything.
She didn't know what to do, didn't know a thing. Was there nothing she could do?
Who were the people attacking Fortuna, Juice, Arch, and the others? What could she do that would
34
make them go away? For what goal did they—
Emilia: “The, siel...”
Yes.
Fortuna and Arch had mentioned something. And Juice's talks with Fortuna surely indicated that
this object was something important.
Meaning, their goal was?
Emilia: “—auh,”
Emilia's feet as she runs suddenly strike air, and losing sight of the ground, she comes to realise that
she has entered into sloping basin.
She immediately reaches out to try and stop herself, but the steep incline gives no aid to the small
girl, and on the heels of her momentum Emilia trips, tumbles, falls.
Normally, perhaps she would cry from the scrapes and bruises and stand back up.
But this time, with both her body and mind entirely fatigued, the strike of Emilia's head against the
ground leads her to fall momentarily unconscious.
Emilia: “I...”
All of this, when she needs to do something. All of this, when she thinks she's figured it out.
With the flame of duty kindled in her little chest, her consciousness aborts.
—The story shall leave the side of the girl, temporarily to return to the scene of the fight.
To see two fates, and see how they conclude.
35
CHAPTER 120: ELIOR FOREST, GLACIATED EVERMORE
—The site has already changed so drastically that you could forget what it originally looked like.
Destruction like a rampage of giant, frenzied serpents. All trees felled down to nothing, some
severed from their roots and dancing violently through the air.
Several craters, too deep to sight the bottom, lie gouged open on the fractured earth. The ruin is so
exhaustive that the entire region could imminently cave in and transform into a pit to hell.
All of this destruction is the work of one man, standing in the dead centre of the devastation.
Blood spills fresh from his face, his breath faltering while he nevertheless manages to keep himself
upright. He has taken SIN unfitting to him inside him, his life whittled away in exchange for power,
this desecrater.
He is Juice—Betelgeux Romanee-Conti.
Juice: “—”
He breathes ragged, his face so lost of colour that it has transcended the word 'pallid'.
But even so, he has regained more calm than what he had at the beginning of the conflict. It seems
like the raging SOMETHING has, for the moment, accepted the uncomfortable environment as its
temporary lodgings.
His bones and flesh have already been ravaged from inside, but control of the body is now entirely
entrusted to Juice, the power acting as equivalent for rent having increased in strength and accuracy.
Wielding this authority, overwhelming destructive power.
Unseen Hand's strength is immense, allowing him to extend his arms to places he cannot touch, let
his fingertips contact what he cannot contact, sending power crashing into someone he should have
no hopes of opposing.
Juice's power, leader of the Witch Cult's moderate faction as he is, will never match that of the
extremists what with their militaristic bent. And that goes double when discussing the person who
possesses the greatest ability for combat in the cult, Cardinal of GREED Regulus Corneas.
That Juice is managing to somehow face Regulus without instantly being turned into gory paste is
unmistakably the achievement of the witch factor he subsumed.
But, Juice's frantic resistance has,
Juice: “How do... you, FIND,, THIS...”
Glaring ahead with his bloodshot eyes, Juice strangles out his voice as he holds his trembling arms
aloft.
Unseen Hand's unrelenting, uninterrupted storm of concentrated violence. Having been endlessly
battered around by the thing, the enemy vanishes beneath the dense plumes of dust,
Regulus: “Oh, you're done?”
When the smoke resides, it reveals Regulus merely standing there, looking bored with his finger in
his ear.
His figure as he stands there rigorously probing his ear could conceivably be detached from the
36
environment from how absolutely none of the assault has affected him. As if he had been pasted
onto the scene of the annihilation in post-production.
Juice: “Even with... all of this!”
Regulus: “How about toning it down and taking a moment to realise? To realise the discrepancy. To
realise that between you and me, there is a clear power discrepancy. And you can disregard however
good your compatibility against me could hypothetically get, because that isn't even the issue here.
There's nobody out there who can beat me, or can wound me. You can go ahead and subsume a
witch factor, and then go ahead and bring the Dragon and Sword Saint along with you, it's still not
going to work.”
Juice: “...Perhaps you may, say so... although it rather appears that I have... purchased from you,
CONSIDERABLE TIME.”
Regulus: “Because there's no need for me to get into a panic to overtake you. Aren't your eyes
telling you? I'm just here as a chaperone. Do you think I'd go out of my way to come to this kind of
place if I wasn't? Being in my mansion surrounded by my wives is enough to glut me for the
minuscule fraction of peace I desire. But, well, I have to say I'm starting to get bored.”
Regulus slowly steps forward.
He walks calmly through the transmogrified forest, descending from his position until his eye level
matches that of Juice, and gives an easy swish of his arm.
It's like he's swatting an insect. Juice braces for anything to happen.
Calling within himself, he sacrifices his flesh and blood to the dark, squirming thing to gain power.
He takes in a breath, ready to use the push welling up from inside him to batter Regulus around,
When Juice's arms go flying through the air, severed at the shoulders.
Juice: “Wh!?”
Regulus: “What a dull reaction. With how you've been annoying me, don't you think it's simple
courtesy to at least writhe in a form of agony that's fun to watch? Though I suppose there was no
point expecting anything.”
Juice: “aaaaaaAAAAAAAAAHHH!!”
With his arms splaying blood about the surroundings as they tumble across the ground, the eyes of
the disarmed Juice shoot open wide as he shrieks.
The cut at his shoulders is sloppy, leaving an ugly wound as if a beast's fangs have mangled his
arms off. His right arm is gone from the shoulder down, his left arm severed about halfway down
his humerus.
Juice convulses in gruesome pain.
Bloody froth spills from his mouth, the excess of pain leading him to grit his teeth so hard that he
breaks tooth after tooth after tooth. His legs, already lacking in strength at the best of times, falter
and drop him down to his knees. His forehead hits the ground, despair creeping over Juice's
expression.
37
Regulus: “In the end, your resolve or your determination or your whatever and so on and all those
other things I suppose we're going to talk about, well here you see what they amount to. And it's the
same for everyone, so don't bother worrying about it. There's nobody out there who can live while
carrying more than their arms' capacity. Live while satisfied in your own little world, fulfilled,
focused only on your own concerns. According to what's fitting to your calibre. And you don't even
have arms to hold anything now... the conclusion here is obvious, don't you think?”
Juice: “AAAH! AAAAAAahhh...”
Regulus: “And being entirely honest, it's not like I'm enjoying this. You might see me tormenting
you like this and perhaps think that I'm some kind of sadist who feels pleasure when inflicting pain
on others, but actually that would be an incredible misapprehension, and a great insult to the
personality what I possess. I'm not doing this because I want to do it. There's nothing in my life any
more that I do because I want to do it. Fulfilled as I am, regardless of whether the nuance is a good
one or a bad one, my preference is to reject the influence of anyone else. I am without want. I am
fully fulfilled. You don't have any right in the slightest to resent me. I was simply walking along,
and you were simply in my path.”
The spouts of blood dampen in their velocity, Juice's screams transforming from something loud
into something quiet.
With the quiet, ragged puffs of his breathing, Juice's form as he expels bloody foam spasms like an
insect seconds away from demise.
Regulus's words carry no malice, or hostility, or anything at all.
Because as far as he cares he is stating the absolute truth, and no reason exists to pair it with any
emotion of any form. Regulus has no need to hide anything, and so truly believes this.
Juice's desperate deeds had influenced Regulus Corneas so little that his bangs did not even sway in
the resultant breeze.
Regulus: “Speaking in full sincerity, this was all very anticlimactic. I was being called along which
had me thinking that something would happen, and... well, not that there's ever been a situation
which hasn't resulted in an anticlimax for me, but if I'm getting summoned I'd at least like for you to
show me something that can hope to counterbalance to the effort I put into walking around.”
Pandora: “I give my apology, Cardinal Regulus. I have put you through the pains to accompany me,
and the trip has failed to meet to your expectations.”
Pandora addresses Regulus as he looks down at the nigh-withered Juice.
She had also kept through all of Juice's onslaught with Unseen Hand while standing stock still in the
very same spot that she had first appeared.
Just like Regulus, her outfit has not changed an inch. Not a speck of dirt pollutes the white cloth
enshrouding her small, thin frame, the purity of the garment preserved, and her beautiful face
suffers not a single wound.
Regulus: “I do not mean to say that you are at fault, Pandora-sama. I'm just saying that all these
forest people and the idiots in the moderates are unanimously pathetic. Trash without even the
slightest intention to improve themselves. They're not like me, sitting at heights where the very
concept of improvement carries no necessity, they have these attitudes while being mundane rabble
whose lives are over if they ever stop struggling. They're rejecting the idea of meeting their own
capacity, and from my perspective as GREED I have to say that level of desire is inconceivably
38
shallow.”
Pandora: “It is not the case that every person in existence can consider matters in the same way that
you do, or reach the same domains that you have. You are more special than anybody else, and
satisfied in that self of yours. You are perfected and glorious. While they are imperfect and also
glorious.”
Regulus: “I'm not the most favourable when it comes to debates. I have no compunctions against
receiving your praise, but I cannot say that I'm seeking commendation either. Though, there was no
need to bring myself and the Blacksnake alongside, was there? You could easily dominate this forest
on your own, Pandora-sama.”
Somewhere right now in this forest, there exists the pestilent witchbeast.
The presence of the repugnant and malicious thing prompts Regulus's disgust, all without him
realising that from anyone else's perspective, he would deserve to be thought of in the same manner.
Pandora nods.
Pandora: “If we are considering in terms of overturning their resistance, then it would indeed be
possible for me to achieve it by myself. However, those are not the terms in consideration. As I
assuredly did not come here for the purpose of harming the inhabitants of this forest.”
Regulus: “This is what you're saying after bringing the indiscriminate Blacksnake here and leaving
it to its devices? I'm sure that you're being entirely genuine about not meaning to cause harm... so
have you then rationalized that fatalities are simply unavoidable?”
Pandora: “When pursuing a noble goal, it is essential that some lives be given as sacrifices. But
even so, one cannot disremember the zeal to rebel against even that wicked fate. I believe that the
beauty of such spirit cannot be invalidated.”
Regulus: “You're diverging from the point, but essentially you're talking about killing people to
achieve your goals. Ahahaha. If that's all we're discussing, then I'd call it preferential to state it
plainly and clearly. Compared to making me waste a day of my time racking my brain pointlessly,
far more preferential.”
Pandora: “I feel very fondly about your approach.”
Pandora gives an enchanting smile. Regulus shrugs.
Regulus lowers his gaze back to Juice, who will probably die if left alone, and begins walking over
to deliver the finishing blow.
Regulus: “Well it's not like I think you'll die from that body dying, but pulling your insides out and
keeping you trammelled does make our operations easier. Though it's pretty strange to be talking
about trammelling someone who doesn't have a body.”2
Regulus raises his leg, ready to stomp down and smash Juice's skull to bits. But right before he can
make contact, a voice cuts into the scene.
???: “AL HUMA!!”
2 Doesn't have a body → more accurately, doesn't have a head or neck. I'm 99% sure this futzing doesn't matter at all
(the 1% is the chance that Juice is the mysterious kind of spirit that has pinkies or something) but hey.
39
Obeying the canto, matter takes in the world's mana to achieve form.
Appearing alongside the explosive noise is a ball of ice so giant that it encompasses all of the
visible sky above. The trees are felled and the sky's panoramic is easily observable, but the only
thing to observe is a vast sheet of pale blue ice.
Regulus: “Ahh... I swear, nobody can give it a break.”
Regulus looks up to see the continent of ice floating above him, ad clicks his tongue.
Immediately, the immense ball of ice plunges down from directly above him—
—The earthquake, and the unavoidable shockwave, batter Regulus entirely.
This explosion of air and rumbling of earth exacerbates even further the collapse of this forest only
describable as a 'disaster zone'.
The sheet of ice shatters into fragments, with the crushed trees and boulders, the ground pulverised
under this incredible mass, changing shape once again within only this one single day.
Shard of white ice dance through the air, scintillating.
Among their gleam is a man toppled limply on his side, with a silver-haired woman dragging him.
Woman: “Juice! Juice, keep steady! This is... what am I meant to...”
Juice: “Fohr, tuna, sama... is that, YOU?”
A weak light returns to Juice's nigh-dead eyes.
His life still remains equally in danger, but he still manages to barely remain conscious. Fortuna
nods
Fortuna: “Yes, yes, it's me. Juice, you're...”
Juice: “I am, FINE... this flesh is, due to wither someday... The finger who trusted me, and entrusted
it to me, will understand... of more concern is, Emilia?”
Fortuna: “I left her with someone trustworthy and they fled the forest. She's fine.”
Juice: “I, see... I am, glad to HEAR SO...”
???: “—Except there's nothing to be glad about at all!!”
Just when Juice's blood-slaked face relaxes in relief, the voice of an enraged Regulus shouts over
him.
Having been stricken by a massive sheet of ice, Regulus's expression is furious. He combs his hand
through his bangs, his eyes hosting clear animosity.
Regulus: “The very second you come back, and just who do you think you are to pull this stunt? I
was seconds away from stomping that guy's head in, me, I was! With what right, with whose
permission, are you taking my... my my my my my my my my my my my my my my my my my
my my my my my my my my my my my mymymymymymymymymymymy!! Getting in!! My
way!!”
40
Screaming as if in tantrum, Regulus squats down and puts his hands to the ground. He proceeds to
swing his arms up, casting up dirt to dance through the air, the soft soil flying toward Fortuna and
Juice.
The quantity of scattered dirt is not especially much. It's the kind of thing a child would do,
throwing sand about a sandbox, the embodiment of crude and infantile anger.
Fortuna sights the dirt and ignores the stuff as she immediately focuses her magic for a
counterattack.
But,
Juice: “You mustn't! If you neglect... to evade, all the earth...”
Fortuna: “Huh?”
Juice interrupts Fortuna's canto, headbutting her to the ground. The two tumble across the earth
undefended, when Juice strains himself to use UNSEEN HAND and throw the couple further
backwards.
Rather than intercept or defend against the dirt, he opted that they tumble messily across the ground.
Just when Fortuna verges on yelling to question what the hell Juice is doing, she sees it.
The moment that the dirt and pebbles that Regulus threw hit the ground, out peals the staccato noise
of raindrops beating on a rooftop as COUNTLESS TINY HOLES BORE THROUGH THE EARTH.
Each hole is only the size of a grain of sand, but the density and piercing property of them present
an issue.
The mystery attack had by and large concluded by only gouging open the earth, but one fragment of
the assault did manage to hit a tree which still precariously retains its original shape.
This tree, with a trunk so thick that it's questionable whether Fortuna could loop her arms around it,
rips open with countless tiny holes and bursts into smithereens.
It's easy to envision that hitting someone, and them instantly exploding into bloodspatter.
And the most terrifying thing is,
Regulus: “Why the hell are you people dodging! Just take the attack, turn into gore, and go be food
for the bugs! That goes for you, Betelgeux, you pile of scum, and for that woman too. I was
thinking you might be okay to take as my 79th wife, and then you go and pull this rubbish!”
Regulus bends down, arms to the ground as before.
The most terrifying thing is, a deed of destruction on this calibre just meant throwing dirt around for
Regulus—and took no greater effort than that, child's play.
The enraged and belligerent Regulus had taken a direct hit from Fortuna's strenuous attack, for
nothing to happen to him. Aberrant, is the word to describe it.
Regulus Corneas possesses transcendental powers in attack and defence. And that incredible power
is locked up in a body that hosts an egotistical, infantile mind.
A dangerous entity, as if power identical to the Dragon were given to a petulant child—such is how
Fortuna judges this monster.
41
Regulus: “If you're not keen for being gore chunks, how about I pluck off your limbs and arrange
them as decoration! I'll make you regret having made a fool of me... of GREED!”
Pandora: “Please wait, Cardinal Regulus.”
Just as Regulus prepares to once again shower Juice and Fortuna in dirt, Pandora calls him to a stop.
With his hands still touching the ground, Regulus turns his head to look at Pandora. The rage remains
thick in his expression, and even when facing Pandora, who he had treated respectfully, he shows no
signs of discarding his anger.
Regulus: “...What, Pandora-sama? Right now, I am midway through shaking in uttermost rage as
my rights are being violated. You have some task for me, when I'm like this? What are you
conniving, trying to stop me? Take careful mind of your words, and, this instant, you answer me...”
Pandora: “Please settle your anger, Cardinal Regulus. I do not permit you to kill them here. Is there
nothing that you feel in seeing them?”
Regulus: “In seeing me right now, do you think I look like there's nothing I feel? —I go prostrating
myself and for this, don't get fucking carried away, you woman!”
Seemingly forgetting that they are allies, Regulus swings up his arm with his target being Pandora.
Up launches the spray of dirt, cutting straight through and decimating the trees in its path to strike
her. It hits, her body exploding into a splatter of blood and gore.
Fortuna: “...No way.”
Fortuna mutters in astonishment as she witnesses Pandora's evisceration. Someone she had loathed,
now killed ruthlessly due to a breakup of internal relations.
Fortuna had utterly believed that Pandora would have some ace to disregard even Regulus's attacks,
but here she is: strewn in scarlet chunks across the ground, fertilizer for the ruined earth.
Regulus: “This is what happens when you prattle bullshit at me. How come nobody can practice
any basic goddamn form of consideration? Don't get in my way. Don't obstruct my path. Don't
interfere with my actions. Don't rebel against what I do. Am I really asking for anything so
difficult? Say, what are your thoughts on this?”
Regulus turns to Juice and Fortuna, a shadowy gleam in his eye.
This was not the time to celebrate about a drop in enemies. If the enemy remaining after a drop in
enemies is a person of absolute strength, then the situation hasn't changed at all.
Fortuna had used the greatest power in her disposal to hit Regulus with that surprise attack.
And even after being hit with it, Regulus's body suffers no wounds and his clothes don't even suffer
a wrinkle. It's frustrating to admit, but Fortuna cannot defeat Regulus.
Juice has also been so cornered that his body has broken down. Even if Fortuna asks him to do the
impossible and fight on his deathbed, the combat is going to be one-sided.
All Fortuna can do is have them lure Regulus's fury, and buy time for her daughter to run.
Juice: “Let me, deal with this... Fortuna-sama.”
42
Fortuna: “But Juice, you...”
Juice: “No matter how... much blood I shed, until all of my bodies are deceased, I can... KEEP,
GOING. I-I, shall amass time, for you... to, flee...”
Fortuna: “Don't say these ridiculous things.”
Fortuna's cheeks relax as Juice attempts to upright himself in her arms.
It mystifies her that she can craft a smile at a time like this. She'd rather like to brag.
Fortuna: “You're telling me to leave you here and run? If I was going to do that, I wouldn't have
come back here. I parted with Emilia to come back here, telling me to leave now is impossible.”
Juice: “HOW, EVER... then, if so, why... have, you returned? I-I...”
Fortuna: “To keep you from dying. And if you do die, for me to be at your side.”
With Fortuna's amethyst eyes gazing on, Juice's bloody eyes wrench open.
Considerably lighter now that he has lost his arms, Fortuna draws Juice's body closer, to tell him
from within breathing range:
Fortuna: “In a world without you, in a forest you no longer visit, what is there for me? I'm weak. I
can't survive a long period of time without you there.”
Juice: “You are not weak in the...”
Fortuna: “I'm weak. I act strong when I'm around you and Emilia, that's all.”
With that, Fortuna helps Juice up.
Fortuna props the trembling Juice up so that he stands, her body close against his as she supports
him.
Seeing the couple standing in what could almost be an embrace, Regulus's face turns abjectly
disgusted.
Regulus: “Look at how fired up you are after such a protracted period of ignoring my question.
What on earth could be going on? What on earth could this be? After I showed you how incredible
the power gap between us is, after I taught you in such succinct and plain terms, how can you
possibly figure that you can do anything? What on earth are you people thinking?”
Fortuna: “Windbag of a man. After how our attitudes have demonstrated it, surely you can tell?
Thanks for all the lectures, but we've got only one response.”
Juice: “IN, DEED.”
Fortuna and Juice share a glance, and speaking together:
Both: “—Like we care, idiot.”
Their voices overlap, with Fortuna flipping Regulus the bird as a bonus.
With that, Fortuna and Juice scramble up whatever power they have available.
43
Regulus's face flashes crimson in fury.
Regulus: “...!! Very well! I'll take the two of you, butcher you into indistinguishable chunks, hurl
you into the Blacksnake's dingy maw—”
???: “What I told you was to wait, Cardinal Regulus.”
For the third time, an interruption to Regulus's plans.
Pandora's arm descends from above to press Regulus's head down, his body proceeding to sink into
the earth without any resistance. Buried chin-deep into the earth under a second, Regulus glares up
at Pandora as she lands beside him.
Regulus: “Just incessantly!”
Pandora: “Should it be necessary that I stymie your will, I shall. As of now, my goals in having
brought you here have been by and large accomplished. You have done far enough and I would
appreciate you go home.”
Regulus: “You drag someone along, but the second you're satisfied you demand they leave? Do you
think anybody could agree with these ideas of yours? Until I've settled this irritation of mine and
returned to being my usual self, I will assuredly never—”
Pandora: “I see. Then I will do it. CARDINAL REGULUS COULD NOT POSSIBLY BE HERE. HE IS IN HIS
MANSION, SPENDING HIS TIME WITH HIS WIVES.”
Regulus: “Wa—”
The next instant, just as Regulus goes to shout something, he snaps out of view.
It isn't that he's sunken entirely into the dirt. He has truly blinked, vanished out of this scene. In the
spot where he once was, the hole from him being plunged into the dirt is gone.
All as if affirming Pandora's statement, that HE COULD NOT POSSIBLY BE HERE.
Pandora: “Being that the racket has left the scene, we can now discuss at a more leisurely pace.”
Fortuna: “...Can I ask you something first? How come you're here? I know just saw you die a
minute ago.”
Pandora stands there as if this is entirely normal.
This girl, calm smile on her face, is supposed to be a scattering of gore. Fortuna glances over to
where her remains were strewn, and gulps.
Not a trace of the gory mess remains in the slightest. Just like how Regulus has disappeared, her
corpse is vanished.
Fortuna is utterly lost for words. Pandora tilts her head.
Pandora: “Could YOUR EYES HAVE DECEIVED YOU?”3
Fortuna: “—!”
3 The trick behind Pandora's powers and how they work has yet to be explained. This is how the line clicked in my
head, but it's questionable whether my phrasing gives any legitimate suggestion as to what her power is doing.
44
Fortuna shudders.
This should not be possible. But the world has reformed itself into a shape that supports Pandora's
words. Invalidating what Fortuna had supposedly seen, and overwriting it all with something
strange and unknown.
The corpse is gone, Pandora is resurrected. Regulus is gone, the aftermath of his deeds are gone.
Immediately after realising this, Fortuna looks aside and nearly screams at the shocking thing that
has happened.
As he stands beside her, Juie's arms—Juice's severed arms, are back to normal.
Pandora: “Since Cardinal Regulus is not here, the consequences of his actions have disappeared. It
is all very simple. Although, the mending of Cardinal Betelgeux's arms is a result of my
beneficence.”
Juice rotates his recovered arms in confirmation. Fortuna's eyes waver as she watches on.
Fortuna: “Juice, your arms...”
Juice: “They feel to move WITHOUT ISSUE. My body, also... the insides excepted, without issue.”
Pandora: “I have not rewritten so far as to change your ingestion of the factor. I would like to
commend this action of yours, and the actions of she who has returned for you. Please consider this
an illustration of my sincerity.”
Pandora is an emblem of hatred for Fortuna. That hasn't changed, and the moment she laid eyes on
her, she assuredly could not hold back her rage.
But Fortuna had not imagined that Pandora would be such a mysterious, unfathomable opponent.
She cannot come up with any clues as to what happened. She cannot comprehend what is going on.
Everything that happened today in this forest transcended Fortuna's imaginings. The one thing she
does understand is that, thanks to all of these incomprehensible happenings, everything is on the
verge of ending.
Juice: “Fortuna-sama, compose yourself!”
A roar cuts into Fortuna's stunned mind just as it begins to stall.
The pain of her slapped cheeks leads her to blink, and find Juice right there, looking at her. He
grasps her shoulders.
Juice: “I am sure that you have queries, and am sure that you are confused. HOWEVER, you must
leave that aside for the PRESENT MOMENT. What is crucial is to safeguard this forest, safeguard
EMILIA-SAMA! And... the defeat of that woman shall ACHIEVE SUCH!”
Fortuna: “—Juice.”
Strength returns to Fortuna's eyes. She glares at Pandora.
Yes. He's right. She might be strange and unknown, and the inability to anticipate what will happen
45
next is terrifying. But even so, Pandora had eliminated powerful Regulus from this scene, and
returned Juice's missing arms.
She has foolishly weakened own combat forces and rejuvenated the enemy. She might not even
have realised that she has cornered herself.
Fortuna: “You're exactly right, Juice. Wondering about what's happening can happen later. Now is
when!”
Juice: “We combine our strength, and DEFEAT HER! Should we repel her, the remaining cultists in
the forest also WILL WITHDRAW. —We can SAVE EMILIA-SAMA!”
The image of her daughter passes through Fortuna's mind.
She had been prepared for their previous goodbye to perhaps be their last. And she had indeed been
acting until now with that exact resolve. But now, she sees a new hope.
Emilia will be saved. By none other than Fortuna and Juice's power.
Fortuna: “—Frigid white, captor of time, magic palm of sheer ice.”
The magic which had stricken Regulus even now churns within Fortuna, seeking a place where it
may detonate. Her canto presents that power with form, with a target, as mana interacts with the
world.
Out sounds a crack as the sharp-tipped icicle forms, the thing large enough for multiple giants to
heft in concert, a spear of ice.
Its point aims at Pandora. Should it launch and strike her, she will be mutilated, her remains
scattering everywhere and freezing beyond any hope of repair.
Beside Fortuna, Juice hugs his shoulders as pressure surges from him as well.
The power runs frenzied beneath his tattered vestments, the wounds except those on his restored
arms reopening. Even in this grievous state, he will expend the whole of his soul for the sake of
those he believes in.
Faced with the manifestation of their powers, Pandora does not even take fighting stance as she
smiles.
Pandora: “Now, please do come. —Allow me to savour your resolve to its very limit.”
The couple's power quakes the world, all in an effort to rip apart Pandora's smile.
And,
※ ※ ※ ※ ※ ※ ※ ※ ※ ※ ※
Emilia wakes up in the basin and shakes her head, managing to recall her location as she glances
around the area.
Emilia: “Right... I...”
46
Herself, covered in mud, and unfamiliar scenery. Scraped knees, legs pained from excessive
running.
All of it weighs down on Emilia as she regains consciousness, with the panic constricting her chest
and her rejuvenated memories informing her that this is neither a lie nor a dream.
Emilia: “Mother... Juice... Arch...”
Precious people, who had all staked their own lives so that she could escape.
As she recalls their faces in sequence, Emilia remembers that she must do something. Everyone
who had tried to protect her told her to run.
That they want her to run dead ahead, and escape the forest.
But, Emilia also thought this:
There has to be something she can do for everybody.
Emilia: “That's, right... the siel, the siel!”
Seal. The word lingers in her memories from before losing consciousness.
The discussion a stern-faced Fortuna had had with Arch. About how the scary people had come here
searching for the seal in the forest.
The forest's seal lies deep in the deepest depths of the forest where Emilia lives, a mysterious door.
Leading to nowhere, just a metallic-looking door standing there in the middle of the woods.
The adults called the place the seal. Emilia knew its location.
Emilia: “Have to go there.”
Going there would not present Emilia with anything she could do.
She didn't know how to open the door, and she didn't even know what the word 'seal' exactly meant.
But she knew something extremely important was there, and knew its location—which was more
than enough for Emilia.
Considerations about what she might be able to do are not what spur her into action.
It is the hope, that going there will make things change, that pushes her forward.
Emilia: “The siel should be... but, which way was it?”
Having tearfully parted with Juice, tearfully parted with Fortuna, and ran around the forest in Arch's
arms, Emilia runs directly for an unknown place, alone.
This may be the forest where Emilia lives, but it is no longer the forest that Emilia knows. The
region that Emilia frolicked in was limited only to the village's surroundings. Forget about the seal's
location, she could not even put her finger on where her mother or Juice would be.
Emilia: “Auh, hah...”
Emilia wails at her own powerlessness.
She knew what she needed to do, but lacked the strength to achieve it. She has no mother to cling to
when troubled, here. She has to be the one to act and save her mother.
Emilia: “—Hm?”
47
Emilia's earnest feelings spur those watching over her into motion.
Emilia wipes away her tears, when dim lights pass by her face and lead her to blink. She looks up,
to find several glowing lights cutting into her vision.
Emilia: “The, fairies?”
Emilia calls them fairies. Fortuna and Juice call these supernatural entities spirits.
Supposedly lacking any language or will, the lesser spirits answer to the young girl's frantic plea.
The lesser spirits dance in circles before the paralysed Emilia. They all move in one direction then
back again, there then back again, over and over, demonstrating the course.
Emilia's voice trembles as she realises what the spirits are trying to say.
Emilia: “You're telling me, where to go?”
They don't reply. But they do bob up and down, as if in affirmation.
Emilia: “If I go that way, I'll find the siel? I'll be able to save Mother and everybody?”
The spirits strobe brightly.
Emilia wipes away her tears as she shakes her head.
This isn't the time to be bawling here forever.
Her mother and Juice and so many people had helped her, and when she started crying, even the
fairies came to cheer her up. After all of this, she cannot pardon herself to cower here endlessly.
Emilia: “Mm... mm, mhm.”
The spirits bob about, as if confirming whether Emilia is well. She nods in reply, and with her small
frame swaying, breaks into a run. She follows the spirits' guide, dashing desperately over the rugged
earth.
She passes over hollows, scales steep inclines, passes through the gaps between trees.
At many points along the path are areas that the spirits can travel through, but Emilia cannot. She
stumbles, branches scraping at her cheeks, tumbling mouth-first to the ground, which she spits out
before standing back up.
Her breathing labours, tears of fear and pain welling up again.
She sniffs her snot back up, wipes her tears with her muddy sleeves, gives her grazed knees a slap
and runs.
She withstands the pain and the hurt, running with all her might as the memories pass through her
mind.
Memories of her time spent living in this forest, ever since she first gained cognizance.
Fortuna was a stern mother, and never spoiled Emilia in the least. She wasn't Emilia's real mother.
Emilia had proper, real parents, like normal.
Such had been a common thing to hear from Fortuna, repeated over and over, which Emilia both
believed and did not believe. She had real parents. That made her happy. But Fortuna was also her
48
real mother. And as far as Emilia cared, that was unquestionable truth. It was because of today's
happenings that she truly understood that.
She remembers being scolded. She remembers nights where she would hold a crying, apologetic
Emilia, and sleep together with her. She knew that she would always stroke her head when she
woke up until got out of bed, so that Emilia would not be lonely.
Emilia knew better than anyone that her mother loved her.
Everybody in the village had been kind to her.
There had always been a kind of alienation, where it felt like they were keeping their distance, and
weren't sure how to interact with her. But even so, they never said anything that would hurt her, and
always treated Fortuna well.
She knew that even with the Princess Room, everybody had done their best to make sure it would
be a nice place for Emilia to spend her time. They prepared toys so that she wouldn't feel alone
while inside, and made lots of hand-stitched dolls for her. The count of dolls multiplied by the day,
and Emilia had long ago ran out of enough fingers and toes to even hope to play with them all.
All of those dolls, every single stitch of thread, was proof of their care toward Emilia.
Emilia had hated Juice at first.
Because everybody's distancing of her and locking her in the Princess Room always happened when
Juice's group was visiting. The adults were hiding things from her so that they could do something
fun. When she first escaped the Princess Room and witnessed Juice and Fortuna talking, and saw
Fortuna smiling at him, Emilia was jealous of Juice.
She thought she would never forgive him. But he had broken into tears upon meeting her. Cried and
cried, spilling tears of happiness, and Emilia forgave him.
After all, those were tears of warmth. She thought back on how peaceful she felt whenever Fortuna
hugged her, and patted Juice's head. She kept by his side as he cried so that he wouldn't feel alone
when the tears stopped. He's hopeless, she thought.
Just hopeless. She thought.
Emilia: “I... with everybody, again...”
She wanted to sleep with Fortuna again.
She wanted to invite everybody to the Princess Room.
She wanted to take that cheeky Juice, who was trying to protect Emilia, and definitely stomp on his
foot.
She wanted to see everybody again.
Emilia: “Because I'm, a good girl...”
The tears blur her vision as she runs, and after passing by a handful more trees—Emilia discovers
the seal she has been seeking, and,
???: “Welcome.”
A girl with platinum hair stands before the door, her arms spread to greet Emilia.
※ ※ ※ ※ ※ ※ ※ ※ ※ ※ ※
49
Girl: “Thank goodness. You were the first to arrive. I was glad to have finally found the seal, but I
could not locate the essential key. I am truly relieved to have found you safely.”
Emilia: “Why are... you here?”
The girl, Pandora, addresses Emilia with familiar tone and strange pressure. Emilia's throat trembles
as she asks her question, and Pandora gives a small clap of her hands.
Pandora: “Huhuhu, you must be surprised. It is all very simple. This seal is very important to me.
And so I have always been searching for it. It is one of the reasons that I have come to the forest
today. Which means that I need to be here.”
Pandora's response isn't what Emilia is looking for.
Emilia was trying to ask about Pandora's reason for being here, in this spot. When Emilia had last
seen her, Juice had been blocking her and Regulus's path.
If she's here, then that means Juice...
Emilia: “Why are... you here?”
Perhaps having noticed how close Emilia's heart is to shattering, Pandora's eyes widen. She puts her
hand to her chest as she seems to reflect on what she just said.
Pandora: “I apologize. The reply that I gave you was strange. I am not the one you are asking about,
you are asking about Cardinal Betelgeux and your Mother.”
Pandora is late to understand it, but she does wind up reaching the correct answer.
If Pandora had continued being mistaken, Emilia could have ended all this without her question
being answered. Even though she herself did not know what she was seeking, with all of this.
Pandora smiles tenderly.
It carries no malice or maliciousness, abounding in kindness, appearing an honest attempt to dispel
Emilia's anxiety.
Pandora: “Please do not be worried. You are concerned about Cardinal Betelgeux and your Mother,
both of whom are safe.”
Emilia: “Huh?”
Pandora: “There is no need to be so anxious, though it would have been best should you have asked
so originally. Neither I nor the members of the cult have come here to harm anybody in the forest. It
is as I have stated, I have visited as I have business with this seal. So being, I am not so foolish as to
create any unnecessary sacrifices.”
Pandora's words are kind, and thunk one after another into Emilia's overburdened heart.
If Emilia is going to trust what she's saying, then Fortuna and Juice are safe. Perhaps whatever's
happening to everyone in the forest is nothing as bad as she figured.
In fact, this girl had just said that she had business with the seal. Meaning, once she's done with that
business—
50
Emilia: “When you're done with the siel, will you please go home...?”
Pandora says nothing.
Emilia: “Wh-when you're done with the siel, will you please leave the forest and go home? Go
home without doing anything bad to everybody?”
Pandora: “—Why, of course. I have no desire for unnecessary sacrifices either.”
Pandora gives a deep nod, as if she's making a promise.
She then points at the seal, and tilts her head at the teary Emilia.
Pandora: “Which means that I would like for you to please give me the key. Provided that we may
open this door, we shall withdraw from the forest immediately.”
Emilia: “Key...?”
Pandora: “Yes. A key. Considering the form of a door which this seal has taken, a key is necessary
to open it. You would be in possession of that key.”
Emilia: “I, don't know anything about that...”
Emilia shakes her head.
She truly has no idea what Pandora's alluding to. She doesn't remember anyone giving her anything
like a key, and the seal had been kept secret from Emilia in the first place.
There is no possible way that Emilia could own a key for a seal which she had been kept in the dark
about. It doesn't even bear thinking, with how natural this conclusion is.
Emilia shakes her head.
Pandora also shakes her head.
Pandora: “There is no need for secrecy.”
Emilia: “I-I'm not keeping secrets... I really, really don't know! I don't have any key! I haven't been
given a key! Me, I can't open the siel!”
Pandora: “I see. —Then, I will have to dig through the forest so that I may find the key.”
Pandora's expression looks incredibly pained. She lowers her gaze.
While her actions and tone are sympathetic toward Emilia, her ironclad mentality means that she
will most likely do exactly the thing she is saying that she will. Emilia trembles.
If she cannot open the seal right here and right now, this girl will dig through the forest.
Dig through, is simple, vain decoration for it. Pandora is going to DIG THROUGH the forest, the
people living in it, Fortuna and villagers, and Juice's group to get this thing.
This is an abnormal entity.
So abnormal, that Emilia is convinced that not even Fortuna would be a match for them.
51
Emilia: “I-I'll open it! I will open it!”
And so, Emilia calls out before Pandora can start acting.
Pandora's face brightens.
Pandora: “You truly will? Thank goodness. So the key was in your possession after all. I had
thought it would be. After all, you cannot deny that you are the witch-child.”
Emilia: “A, witch's...?”
Pandora: “Indeed, yes. Now, if you would like to see to the seal? Provided that I may investigate
what is inside this door, we will stand down immediately.”
Handing the scene over to Emilia, Pandora waits elatedly for her to act.
While the term she mentioned does claw at her chest, Emilia cannot retreat and so steps forward.
Little Emilia can look up, and look up even further, but still not sight the top of the door.
It's like a giant door that a giant made so that a more giant giant could pass through. The idea that
tiny Emilia has to open this thing is some kind of empty, hollow fantasy.
She stands before the door. Standing is all well and good, but Emilia has no idea how to open it.
Back when she located the seal, Emilia went through all her usual ideas for how to approach the
thing. She has already tried pushing it, pulling it, climbing it, far and long ago.
Emilia's tiny form had not made this ancient door move an inch, and she could not even get the
thing to creak, much less open.
Today will be the same case.
She can reach out and touch it, but it gives not the slightest indication of moving.
Emilia: “Hahh... hauh, hahhh... ahh...”
Her pulse races abnormally fast, her blood churning sluggishly through her head.
Her chest flashes hot, and her thrashing heart could leap out of her mouth at any instant. But her
limbs are dead cold, heavy, as if stuffed with lead.
She has to move it but cannot.
If she does not open this thing, something terrible will happen to everybody.
And she knows this, but can't do anything.
Terror and despair bleach her thoughts stark white, crushing Emilia whole.
Pandora: “—Please consider thinking: I am a key.”
The voice is horrifically smooth as it slips into desperate Emilia's ear.
—I am a key.
As ordered, Emilia focuses on only that image.
Instantly, Emilia feels a weight in her hands. She looks at them. To find that she is grasping a large,
ancient, silver key.
52
Emilia: “A key...”
Pandora: “It is visible to you now? If so, then you indeed are the key.”
Says Pandora happily.
But there is something unnatural about her statement. It almost seems like Pandora cannot see the
key in Emilia's hands.
Emilia: “You... can't, see it?”
Pandora: “—. No, I cannot. That key will only be given to the hands of the qualified. I am certain
that in this world, there are only two people capable of opening that lock.”
Pandora seems to find that position enviable. And indeed, her gaze is not fixed on the key in
Emilia's hand. Although unsure what it means that she cannot see a key which is so perceptible that
it has weight, Emilia turns back to the door.
A sudden key—but Emilia can't find anything that looks like a keyhole.
This door does not even have a doorknob. And although the key is big, in pales in comparison to
this door. Can this grungy old key really open it?
Emilia: “—ah,”
When Emilia instinctively figures out how to use the key.
Searching for a keyhole is unnecessary. The door itself is like a keyhole.
This door is not running the seal.
It is merely acting as a cap for the seal. The door is not sealing anything. The seal is something
more insubstantial, operating inside of this door.
Pandora: “Now, please open it.”
Accepting Pandora's demand, Emilia takes a step forward.
Simply pressing the key against the door, and willing for the door to open, will be enough to open
it. By that alone, this door will be freed from its long, long post.
—If she opens this door, everybody will be saved.
Pandora: “...Is there something wrong?”
But the moment before she moves to press the key to the door, Emilia's outstretched arms halt.
Noticing how Emilia's fingers have stopped shaking, Pandora furrows her brows slightly.
Emilia goes without replying, instead staring at the key in her hands.
If she proceeds to press the key to the door, the seal will open.
But—
???: <Emilia. —Promise.>
Emilia hears in her mind the whispered words from her mother's goodbye.
53
Their conversation back then had not been about the seal.
But Emilia remembers. That she promised her mom that she would keep her promises.
She does not know about this seal. She mustn't know about this seal.
Emilia doesn't know about this place, and isn't meant to interfere with it.
She promised Fortuna. Her keeping her promise must get higher priority than anything else. She is
betraying her trust, and musn't do it.
Nobody will forgive Emilia if she is a bad girl. Nobody be able to forgive her.
And so, she must not open this seal.
Emilia: “I-I, can't open it...”
Pandora: “—Why is that?”
Emilia: “The promise... because, I promised. I don't have anything to do with the siel. I'm not
allowed to open it.”
Pandora: “I see. Promises are truly important things. I think it is very splendid and great that you
would like to keep your promise. However... they are also things which are dependant upon timing.”
Pandora matches her gaze to Emilia's, who shakes her head. She strokes Emilia's silver hair.
Pandora: “I suspect that this promise is one between yourself and your Mother. Your Mother is a
very wonderful person. She has taught you something venerable and correct. Your will is precious
and deserves to be upheld.”
Emilia: “A-and, so...”
Pandora: “But, it sometimes happens that there come times where you must make a decision which
will run contrary to a promise. Perhaps it is cruel that I am seeking a decision from you when you
are still young. However, fate and its looming decisions will not take into consideration the
circumstances of those it trifles. Fate loves those who resist in turn to its waves, and inspires hope in
the outcome of the decision. Which is the hope that you seek?”
Emilia: “Which, hope?”
Pandora nods, smiling maternally.
Pandora: “Yes,”
She presents her hands to Emilia.
Pandora: “First is the hope that you will keep your promise with your mother, proceed without
opening the seal, confront my party, and overcome this tribulation.”
Pandora raises her right hand, as if holding this invisible thing called hope.
54
Pandora: “And second is that hope that you defy the promise with your mother, open the seal, grant
the wishes of my party, and the situation will settle down with no further injuries.”
Pandora raises her left hand, again showing Emilia this invisible hope.
Faced with these two hands, Emilia goes rigid.
She cannot even recognize her breathing, with how her lungs feel to have frozen. Should she say
anything careless, Pandora may instantly withdraw both of her hands.
Unable to touch either of the hopes presented to her, perhaps it will end with them being taken away
from right under Emilia's nose.
—The terror grasps the young girl's heart firm, not letting go in the least.
Pandora: “Which hope shall you choose? —I leave the decision to you.”
The right hope. The left hope.
The hope resultant from breaking the promise. The hope resultant from keeping the promise.
Pandora's sweet and alluring voice.
Fortuna's kind and chiding call of her name.
She cannot even hear her heartbeat under all this noise.
Sound disappears from the world, leaving Emilia behind in a land without colour.
She's thinking. Deliberating. Her thoughts are blazing, her brain could boil any moment.
She focuses every bodily function she has into thinking, giving the impression that everything from
her neck down has died. She cannot hear her pulse, her limbs utterly motionless and alienated from
her will.
She can't choose, she can't choose, she can't choose she can't choose she can'tchooseshecan'tchoose.
Which choice will save everybody? What should she do that will help everybody?
What can she do that will make her everybody's strength? What should she do? Somebody, tell her.
Emilia: “—ah.”
Pandora: “I see. So that is your decision.”
Her thoughts solder, her vision clouds, when Emilia slips a small sound.
Seeing her decision, Pandora's long-lashed eyes lower their gaze.
—Emilia's fingers are touching Pandora's right hand.
The path to not break the promise, not open the seal, and hope for everyone's rescue.
Emilia: “I... promised, my... mother, I'd keep... my, promises, so... mother...”
Pandora: “Until the very end, you trust in your mother's words, your compass. The answer you have
reached following your indecision, and the result that your life has divined, shall I respect.”
55
Pandora nods in agreement as Emilia's eyes overflow with tears.
She releases her hand from Emilia's grasp. Emilia falls to her knees as Pandora looks on, gaze
merciful.
If Pandora wanted, she could have just pushed Emilia's hands to the door while she held key.
While that has nothing to do with whether or not Emilia would will for the door to open, being that
she had been seeking some kind of support, it may have been enough to send her over the edge.
Pandora knew that, but didn't do it.
That alone was something trustworthy about this utterly bizarre girl.
Pandora: “And so,”
Emilia: “...huh?”
Pandora: “Please respect my decision as I consider methods to open the seal.”
Emilia raises her head, stunned.
Pandora is not looking at Emilia. Her gaze is directed somewhere behind her. Emilia follows her
line of sight, to find a silhouette pushing away the shrub as it soars onto the scene.
With her short silver hair,
Woman: “PANDORAAA!!”
And covered in blood, it is Fortuna.
Compared to when Emilia last saw her, she is drowning in injuries. But even so, having been
convinced that they might never meet again, just knowing that she's alive is a relief for Emilia's
heart.
Fortuna: “Take this!!”
Apparently having not noticed Emilia's presence, Fortuna fires off six icicles, striking Pandora
without the least of mercy.
Emilia's body stiffens at the danger, when Pandora glides in to position Emilia behind her,
protecting her.
Pandora: “Beginning your offensive without first observing the area is very dangerous.”
With that, an icicle spears Pandora through the chest. Her thin waist, her right arm, her right light all
proceed to be impaled with icicles, with one last strike blowing off her platinum head.
Emilia shrieks as she witnesses Pandora's small frame be skewered with ice. Pandora's body
staggers, slumping back to land on Emilia.
Emilia catches the decapitated body as it gushes with blood. She screams. It's all too unreal.
Fortuna: “...Emilia?”
Hearing the scream, Fortuna whispers in dumb shock as she seems to come back to her senses.
Rather than accomplishment in having bested a detested foe, Fortuna's eyes waver in discord as she
registers that her daughter is present at this scene.
56
Fortuna: “Why is Emilia...? She was meant to have escaped the...”
Pandora: “To question why is a rather terrible thing. Your daughter was worried about you,
wholeheartedly hoping to help you as she ran to this site. How is it that you, her mother, can
proceed without praising her intrinsic purity?”
Fortuna: “—!”
Pandora's voice calls out from directly aside Fortuna.
Fortuna's amethyst eyes shoot open from both the unexpectedness of it, and at the fact that
Pandora's corpse has vanished from Emilia's arms.
Pandora: “When you look as surprised as you do, you truly do resemble each other. Parent and child
indeed.”
Fortuna: “—! Emilia and I aren't blood relatives! Her adorable face is from my sister in law!”
Pandora: “I give my apologies for that.”
Fortuna's mouth twists in rage as a sword of ice forms in her raised hand. Her sweeping slash slices
diagonally through Pandora's torso, spraying blood everywhere. Pandora collapses back-first and
limp to the ground.
Pandora: “Which means that her foster parent is her Mother. That being, you have not erred in your
methods of raising her. Your daughter has grown to be a very honest, good girl. Her true parents,
your sister and brother, would surely be overjoyed.”
Fortuna: “Don't you dare talk about my brother and sister in law!!”
The fallen corpse disappears as Pandora goes over, as if this is normal, to Fortuna. Fortuna swings
down her sword to bisect her, and slices off her head with the backswing.
She immediately glances behind her to kill the revived Pandora with a stab. She shoves her
backwards, where she slams into a treetrunk, pinned.
Fortuna: “El Huma!!”
A blanket of frigid mist shrouds the pinned Pandora, transforming her into an ice sculpture.
A humanoid sculpture is born, sealing Pandora—already beautiful enough to be a masterwork of the
gods—eternally in the forest as a belonging of nature.
Pandora: “This indiscriminate use of magic is only going to exhaust you. Would you like to take a
moment to calm down, and for us to reattempt by waiting for an opportunity to talk?”
Fortuna: “—! Tedious talk!”
The ice sculpture remains, with only Pandora inside having escaped and starting walking around.
Fortuna spins around to find Pandora standing there, and sloppily swings her fist to hit her. It isn't
even a magical attack. Just a punch resultant from vain struggle.
It strikes Pandora in the face as if drawn straight to it.
57
Emilia: “—aagh,”
Fortuna: “E-Emilia!?”
Blown away by her mother's punch, Emilia fails to catch herself and goes tumbling across the
ground. Having unintentionally beaten her daughter, Fortuna's face pales as she frantically rushes
over to the fallen girl's side.
Fortuna: “No! Emilia, I'm so sorry! I didn't mean to! That wasn't what I...”
Pandora: “This is the pain that you feel when hit. A pain equivalent to being hit has surely just run
through your heart. Are you beginning to understand how heartless your actions are?”
Her hands holding an uprighted Pandora, Fortuna's throat jars as she shoves the girl away. She
stands up and looks around to find Emilia standing beside the seal as ever. No traces of being hit
remain upon her white cheek.
Fortuna: “You've been saying so much nonsensical junk, over and over!”
Pandora: “But this time it was different, and soothed you. Are you unable to devote some fraction of
that emotion toward someone who you believe you hate? I am not telling for you to love everyone
out there in the same way that you love your daughter. But, there are some who change after
receiving only the slightest of care. If I could be part of that count, then I would like to proceed
without repeatedly presenting you any tragedies.”
Fortuna: “Who the hell do you think you are to demand kindness from me!? Emilia's parents...”
Noticing Emilia's gaze on her, Fortuna quickly shuts her mouth.
Emilia stares fixedly at her mother's tense face. When in presence of her daughter, no matter how
detested the enemy is, there are some things which should not be spoken.
Pandora: “Then here is what we shall do. Would you like to try being the one to persuade your
daughter? I have confirmed that she possesses the key, but it appears that she will not open the door.
Because she is keeping her promise with you.”
Fortuna says nothing.
Pandora: “If you rescind your promise, no chains will bind her stubborn heart. I promise that,
provided that I may undo the seal, we will leave this forest without doing anything further. Indeed, I
promise. I will keep my promise. ...Very nice words.”
Spoken with no hint of jest, and most likely her sincere thoughts.
But there do exist statements and actions which become overwhelmingly sardonic because of their
lack of ill will.
Fortuna has seen more than enough to judge Pandora's statements as so.
Fortuna looks at Emilia.
Emilia simply clasps her hands and waits for her mother to speak. Her hands look to be gripping
something, which is likely because she's holding the door's key.
58
Emilia has wound up recognizing the key. And if Fortuna utters a single word to render the promise
ineffective, she will likely open the door. Believing that doing so will save the forest.
Fortuna: “—Don't be stupid.”
Pandora: “Stupid, you say?”
Fortuna: “You'll stand down? You won't do anything more? How will you doing that benefit us?
With everything you've destroyed, everything you've ruined, all the things we had to protect that
you crushed underfoot, with even our pride broken and distorted... what's left for us!?”
Pandora: “Things may be born from places which are barren. Do you not consider that the
magnificence of life?”
Fortuna: “When it's the pillagers saying it, the words are empty and superficial!”
Fortuna roars, jabbing her finger out at Pandora.
Pandora tilts her head, not seeming to understand what Fortuna is saying.
Fortuna: “The struggle is beautiful. There's nothing more respectable than a will to live. —Stop it
with this facile talk. After robbing of us the peace we staked our lives to create, stop your
condescending speech. We had comfort and happiness and everything here. You're the ones who
ruined it!”
Pandora: “Our opinions appear to differ.”
Fortuna: “When your positions aren't the same, the sights you see aren't the same either. With how
you're always looking down at us from on high, I'm sure you see the sky as being a different height
from us!”
Spits Fortuna.
Pandora looks horrifically sad, but Fortune isn't going to respond to that. She instead keeps up her
caution toward Pandora as she dashes over to Emilia, who stands beside the seal.
After confirming that this is definitely her daughter, Fortuna falls to her knees and hugs the small
girl.
Fortuna: “Oh, Emilia... Emilia, I'm sorry. Why are you... where's Arch?”
Emilia: “Arch... told me, to run to the white flowers... so, me, I ran...”
Hearing this, Fortuna supposes the young elf's demise.
She hugs Emilia to her chest, keeping her from seeing her tears. Just how many had perished in this
forest due to the sinister cult's violence?
Indeed, this forest will never return to being what it was before.
Fortuna: “Emilia, Emilia... you did so well to keep your promise. You're amazing. You're amazing.”
Emilia: “Mother... Mother, I, I...”
Fortuna: “Emilia... you're my pride. My treasure.”
59
A clinging daughter, her mother hugging her.
Pandora watches on with her expression intoxicated. Her face almost looks like she is monopolising
the most beautiful sight in the world, all for herself.
Pandora: “I have enjoyed seeing this beautiful familial love. Mutual affection truly is magnificent.”
Fortuna: “That's disgusting to hear when you're saying it. —The seal's staying put. I'm not handing
her over to you. Get to being an icicle, and wither here.”
Pandora: “From your phrasing, would this not usually be when you advise that the other party
leave?”
Fortuna: “All I want right now is to dump the shards of your frozen corpse off the Cascades.”
Voicing curses that Emilia has never heard before, Fortuna once again begins honing her magic.
Pandora purses her lips, seeming pained.
And then.
???: “I have finally—CAUGHT UP!”
His voice sounding somewhat crazed, a man soars over the trees to arrive at this spot.
He leaps over the tall arbours, his momentum that of having been thrown, arriving on the scene with
his holy vestments slathered in blood. It's Juice.
Fortuna: “Juice!”
Juice: “Fortuna-sama!”
With just one call of the other's name, the two coordinate perfectly.
They stand positioned on either side of Pandora as she occupies the centre of the clearing, the two
of them commencing with their assault from both ends.
Fortuna's left hand grips Emilia's wavering right hand firm.
Emilia looks up at her mother's face.
—Her expression as her gaze pierces through enemy is so beautiful she could shiver.
Fortuna: “Al Huma!!”
Juice: “Unseen Hand!!”
Fortuna casts magic of the most powerful degree, while Juice calls upon all of the witch factor's
power at this final moment to utilize this occult ability.
The overwhelming powers surge forth, and—
Emilia: “—mother?”
—With UNSEEN HAND piercing her chest through, Fortuna's blood rains upon Emilia.
60
※ ※ ※ ※ ※ ※ ※ ※ ※ ※ ※
Strength drains from the hand clutching Emilia's as she witnesses Fortuna's body fall limp.
Juice: “NoOW is—THE END!”
Juice makes violent touchdown as he shouts, sweeping his battered arms hard to the side. As if
pulled along by that gesture, Fortuna's body dances through space along the exact same trajectory.
Her limbs go limp like a doll's, and her body tumbles across the ground as if discarded. Blood
shoots out from her convulsing form like a geyser, painting the grassland red in an instant.
Juice: “That did, PROVE EFFECTIVE. ...After all of this, assuredly...”
With a ragged sigh, Juice falls to his knees.
Emilia does not see how Juice yet gazes at the fallen Fortuna with caution.
She merely draws closer, gait tottering, to Fortuna as she sleeps prone.
A hole gapes open through Fortuna's back and breast, the damage so great that the innards of her
ruined body are visible. The force of the bleeding dampens, leaving Emilia sitting in a puddle of
blood.
She hugs her mother's pale head, somehow managing to set it on her lap. Red spots sully Fortuna's
pretty silver hair, and Emilia frantically attempts to clean her by wiping the grime away with her
fingers.
But Emilia's fingers are already dirty with blood, and the more she touches, the bloodier Fortuna's
hair gets.
Juice: “Fortuna-sama! Do not loosen your guard, I ask that you remain vigilant! Once I verify...”
Emilia: “juice?”
Juice: “—”
With a sharp breath, Juice heaves himself up with his palm faced towards Fortuna.
Hearing him, Emilia calls his name. After a moment of looking distantly at nothing, he blinks,
Juice: “Emilia-sama?”
He looks to have only now noticed the girl sitting in the pool of blood.
His gaze lowers down, to where Emilia's lap hosts the woman's head, her limp body lying there
uselessly.
His eyes, shoot open.
Juice: “...Impossible.”
His expression one of disbelief, Juice shakes his head.
Between his own plodding self, and the fallen Fortuna, there stands a platinum girl.
Pandora smiles at Juice as he looks on.
61
Pandora: “I am afraid that there is nothing to be done. YOUR EYES HAVE MERELY DECEIVED YOU.”
Juice: “aaaAAAHH... AAAAaAAAAAAAAAAHHHHHHH!?”
Putting his hands to his face, Juice ruthlessly drives his nails into his skin, carving out crimson
gashes.
The force is enough that his fingernails pare off, the bright blood from his gouged cheeks painting
his face scarlet.
Juice: “Impossible impossible impossible impossible impossible impossible!? Wh-what, what am,
what am I DOING!? What have I DONE? Why, whywhywhywhywhywhywhywhywhy!? Then for
what purpose have I... what... ahh! Ahhhh!? AaaAAAAAAAAHHHHHHH!!”
Juice had taken a witch factor into his body, and kept the thing's discordant power restrained by
force of will.
The most important support for that resilient will snaps away. Every single thing inside Juice
crumbles away.
Because the powers he had gained by risking his life had destroyed the one he had risked his life to
protect.
Juice suffers mental damage beyond any possible repair, screaming as he loses his sanity.
Juice: “For what purpose—did I do anything!?”
Pandora: “Everything, for love.”
Juice's eyes peel wide, froth spilling from his lips as he gazes at the sky.
Pandora's quiet voice answers the screams of his soul.
Pandora: “You have sacrificed your soul to save the person you love. This is not anything ordinary.
All of your long, long time spent supporting the Witch Cult was also for the sake of that love. All of
your deeds are the outcome of love. A most excellent, pathway of love.”
Juice: “Love... LOVE... love... love... love... love...!”
Pandora: “Exactly. There is no need to fear or regret anything. Everything was inevitable. It was all
according to the path of fate. The road had continued its course to lead to this point. EVERYTHING,
FOR LOVE.”
Juice: “For, love...”
As he deliriously mutters the words back, Juice's mind shatters to pieces.
Juice's eyes lose their colour. He is trancelike, motionless.
He mutters inaudible whisperings, endlessly, a living cadaver.
Seeing Juice's mind so utterly broken, Pandora gives a satisfied sigh.
???: “Emi, lia...”
Just as Juice's being shatters into tiny pieces, the flame of yet another life begins to dim.
62
Emilia: “Mother,”
Called by a voice so frail it could disappear, Emilia calls back in astonishment.
Her trembling arms reach out to draw her mother closer, to find that she had grown depressingly
light. At some point, the flood of blood has stopped its flow.
Which means that her mother is okay now, right?
Emilia is not immature enough that she can think this and protect her mind. Fortuna, too weak to
even move, plainly wears the face of a dead man.
Fortuna: “...I'm, sorry, brother...”
Emilia: “Mother,”
Fortuna: “I didn't... stay, by, a single thing, you... told me...”
Spoken like a child giving an apology, as Fortuna voices her regrets.
Blood no longer streams from her body, though tears pour from her eyes. Emilia feels the hot
teardops land on her fingers, and scrambles to gather them up.
Because Emilia inevitably feels that these compose the entirety of her mother's current strength to
live.
Fortuna: “I know, you'll... be angry, sister... I know you, won't, forgive me...”
As she listens to Fortuna mutter incoherently, Emilia finally realises.
Fortuna's amethyst eyes have not been reflecting any light for a long time.
She has long lost her sight, and they have degraded solely into organs for shedding tears. She is not
even looking at Emilia's face. She has not even noticed that Emilia is right beside her.
Emilia can touch her, can hug her, but won't reach her.
Faced with Fortuna as she sobs like a child and seeks forgiveness, Emilia—
Emilia: “—I forgive you, mother.”
Fortuna says nothing.
Emilia: “You're my... you were so good to me... and not even Father, or Mother, could beat you with
how you like me sooo much...”
Fortuna says nothing.
Emilia: “So you, don't have to apologize. You do not have to. Emilia will always, always love you,
Mother Fortuna. Love you. Love you, love you... love you...”
The dam bursts.
Her voice loses its usual tone, as the overflowing tears drip one-by-one onto Fortuna face.
Should teardrops compose the strength to live, then the final miracle here was the strength conferred
by Emilia's tears.
63
Emilia: “...Mother?”
Fortuna: “Lia.”
Her hand slowly reaches out, to touch Emilia's cheek.
A hand which should not be moving strokes Emilia's cheeks, her ears, tickles her hair. As if
touching something beloved, so as not to break it, lovingly.
Fortuna: “You big crybaby.”
Emilia says nothing.
Fortuna: “I love you, sooo much...”
The strength drains from her.
Her arm thuds to the ground.
Emilia senses that Fortuna's body has grown lighter.
Her body has lost its strength, and this should be compounding the weight on Emilia's lap, but
Fortuna as she lays in Emilia's arms has definitely grown lighter.
The most important part of her mother, which must not be shed, has been shed.
Even Emilia can understand that.
She has lost Fortuna, her mother.
Juice, Betelgeux Romanée-Conti, has lost his mind.
And Emilia,
Pandora: “Now, have you prepared yourself to choose the hope which follows the opening of the
seal?”
Ask Pandora after walking over to Emilia, who holds Fortuna's corpse close.
She watches Emilia sit, all while wearing that calm expression and waiting silently for her reply.
Finally, Emilia understands.
Emilia: “Open, the siel?”
Pandora: “Yes. Although highly unfortunate, your Mother, who you shared your promise with, has
passed away. There is no need for promises to bind you as fetters for any longer. What do you
think?”
Listening to Pandora as she speaks insane logic, as if it's normal, Emilia comprehends.
She knows what this demon wearing human shape was thinking in pulling this stunt.
This demon did what she did so that Emilia would break her promise.
Entirely for the sake of making Emilia lose sight of a promise's significance, Pandora had caused
Fortuna's death, tormented Juice's mind, and annihilated the forest.
64
Pandora: “Right, I forgot.”
Emilia says nothing.
Pandora: “I doubt that they will be necessary for you any more.”
Pandora reaches her hand out toward unresponsive Emilia's face. For dim lights to begin glowing,
encircling Emilia, before selecting Pandora's arm as their home and perch.
The minor spirits.
The fairies who had guided Emilia to the seal, and shown her the path.
And, why were they, going to Pandora?
Pandora: “Seeing as I doubted that you would come here on your own, I have enlisted their help.
They do not communicate with words, but they have been very reliable.”
Pandora smiles as she thanks the spirits, and with that, they dance through the air.
Since when had this started? Emilia cannot even tell.
Emilia's head wavers as she looks up at the seal's door.
It feels like the door is looming, pining to someday be opened, and watching Emilia. She feels the
weight of the key in her hands. She had thought that she had dropped it somewhere, but now it is
again in her grasp.
Pandora: “You do have the key. Then, you know what to do.”
Pandora gives a nod. Emilia slowly stands up.
She lowers her mother's head from her lap and silently sets it atop the grass. She twines her finger
through her bangs, arranging her prided mother's beautiful face nicely.
And,
Emilia: “Just die.”
—A blade of frigid wind whistles through the air, slicing Pandora's body to pieces.
Her spouting blood freezes in an instant. Flowers of frozen crimson bloom furiously.
With a single icicle standing central in their midst, out scatter the sanguine-flecked petals, a
masterpiece of ice and death.
Pandora: “That was rather dangerous. Where on earth is this all coming—”
Emilia: “Just die.”
Rods of ice spear down to impale Pandora's limbs, a spear of ice shoots up from the ground to
pierce Pandora from groin to crown, her frozen body screeching as it shatters into pieces.
Pandora: “Please calm down. I am sure that discussion will lead us to an understanding.”
Emilia: “Just die.”
65
Balls of ice close in from both sides, crushing Pandora between them and transforming her into a
splatter of blood.
Pandora: “We should stop. You are kind by nature, and not a girl capable of harming others. Has
your Mother never told you so?”
Emilia: “Just die.”
A spinning blade of ice slices through Pandora from the feet up, casting up a spray of red sherbert.
Pandora: “It would sadden your Mother to see you like this. Neither your legitimate Mother and
Father, nor Cardinal Betelgeux, would desire this.”
Emilia: “JUST DIE!”
White mist cloaks Pandora's body, transforming her into a sculpture of ice. The giant icy sword
which slams into her the moment after smashes rather than slices her with its force, beating the
Pandora sculpture to the earth.
But despite this storm of destruction and bloodlust,
Pandora: “This is something of a predicament. It appears that the effects were the opposite of what I
had intended.”
Emilia: “Just die, just die, just die, just die!!”
Bawling, swinging her arms, Emilia rains icy destruction upon Pandora.
But even as they all strike her, and she dies gruesome death, she continuously comes back fully
restored after only the space of a blink.
Emilia: “Hahhh! Hahhh! Hauhhh!”
Emilia is approaching her limit for using this excess of magic.
With her repeated casts of magic unfitting to her, red-faced Emilia's lower body begins to freeze.
The vast mana swallowed inside her young body is running rampant, and failing to escape outside
in time.
Pandora: “The manifestation of power surpassing your capacities, such that you cannot even avoid
damages to your own body, would be because of your bloodline. The blood of a witch cannot
escape that karma. —Perhaps this forest had been necessary so that you would not awaken to this
power.”
Emilia shakes her head in refutation of the noise. Her right led is entirely frozen, and it's
questionable whether she can even stand. She falls to her knees, her eyes brimming with bloodlust
as she glares at Pandora.
Seeing that pointed, ominous gleam, Pandora shakes her head.
Pandora: “This is unfortunate when I am standing before my dearest goal, but I believe that I will
66
withdraw for the day. It does not seem that you will be willing to listen to anything more about
kindly opening the door.”
Emilia: “Just die, just die just die just die, just die...”
Pandora: “I will regard this day as well enough finished with only the presence of your lineage, and
the creation of a new Cardinal of Sin. I will achieve my goal at another time."
Egocentric logic, disregarding of other and entirely self-centered.
Pandora appears to have washed her hands of the situation, when white flakes flit through her
vision.
Snow.
Emilia's outrageous magical powers are running amok, warping weather to the extremes and
making it snow.
At first it merely sprinkles down, but the snow progressively builds in force and strength, soon
coming cloaked with wind ferocious enough to call the whole thing a blizzard.
Pandora: “It appears that, whenever we next speak, I will have to begin by having you expel
everything before we may even face each other.”
Pandora looks down from the sky as she walks over toward Emilia, who breathes white puffs.
Although she witnesses a hated enemy approaching, Emilia cannot move. Her body has already
frozen up to her waist, and she cannot even raise her arms any more.
Pandora: “You have caused this frenzy of power, and will proceed to fall into a long slumber. Will
the mana of this glaciated forest be fully exhausted, or will an entity possessing power comparable
to your own counteract it? Whichever it may be, I suspect that you will spend more than a short
period beneath the ice.”
Emilia: “Just die, just die!”
Pandora: “I regret to tell you that I will not die. I suspect that both you and I will still remain
healthy by the time that the ice melts and we again meet. And certainly, once that time comes, we
cannot have things proceed in the vein that they currently are. And so.”
Pandora's white finger touches cold against Emilia's forehead.
Emilia's amethyst eyes seethe with loathing. Pandora smiles without any malice.
Pandora: “ALL OF YOUR MEMORIES LEADING TO THIS DAY ARE CONSUMMATED WITHOUT MY
PRESENCE IN THEM.”
Emilia: “—Ah,”
Pandora: “Feel free to supplement them however you wish. Indeed. You did your very best to keep
your promise. It would make me glad if that fact could be engraved in your heart, and you could
proceed to be as you presently are.”
With her body frozen up to her breastbone, Emilia's face recoils, her gaze unfocused and puttering.
67
Her eyes spin and drool trails from her mouth as Emilia's mind is ransacked.
It crumbles.
Indiscriminately and unfeelingly, the wallpaper of her memories is replaced.
The conversations she had fade into the distance, while insults she surely did not receive assault her.
Important, unfading—a promise.
She kept her promise, and that alone was something that she would never forget. And she would
never forget to keep her promises, either.
She kept her promise. The promise was kept.
Nobody had any reason to invalidate her for keeping her promise.
Pandora: “What conclusions shall your heart reach, and what smile will you give me when next we
meet? I will be eagerly awaiting our wonderful reunion.”
The blizzard rages through the forest. Pandora holds her long, dishevelled hair down as she starts
walking.
Having remained on his knees in a stupor, Juice is halfway buried in the snow. Pandora whispers
something to him. He stands up, expression powerless.
The two of them, Pandora and Juice, walk side by side as they leave the snowy forest.
Emilia can only watch them go.
The freeze has already reached her face, and her awareness remains only in her eyes.
Emilia lowers her gaze, and notices it.
On the ground before her, there is an unnatural lumping of snow.
As if, in the middle of this white snowscape, somebody is hugging her.
Emilia: “—”
Her mouth doesn't move. She cannot even close her eyes any more.
Her body is frozen, and her heart is freezing. Emilia's consciousness—
Emilia: “—ther,”
—then came to spend a century encased in the unmelting ice.
Until a spirit found her, a spirit who was searching for her, a spirit given life in this world entirely
for the sake of her.
—Until that time, Emilia remained frozen in the ice.
※ ※ ※ ※ ※ ※ ※ ※ ※ ※ ※
Having witnessed it all, and faced with the sight of her own frozen self, Emilia stands stock still.
68
She remembers everything that happened.
These scenes of the past, slowly unfolding ever since she had woken up.
All of them have been peeled of their superficial, false skin, and come flowing out.
Young Emilia had seen everything that day. She saw how Fortuna died in her arms, how Juice's
mind broke and went insane, and witnessed the perpetrator of all this evil.
And she forgot them, because of her own weakness and desire to forget them?
Echidna: “It would be a mistake to fault yourself for the falsification of your memories.”
The girl standing beside Emilia, Echidna, addresses her.
Just as Emilia had experienced her memories vicariously, Echidna had witnessed everything that
happened from start to finish.
She glances at Emilia, who gazes at the snow.
Echidna: “That thing you confronted was the WITCH OF VAINGLORY Pandora. She brandishes
superficial and self-serving logic, REWRITING events however her whims and pleasures dictate. The
dampening of her influence would be a result of time's passage, and your very own strength.”
Emilia: “My, strength...”
Echidna: “As you can see, your strength is so immense that you can't fully control it. If we are
speaking entirely in terms of combat, you surpassed Pandora even here, when you were young. But
battles aren't so shallow that you can prevail on strength alone. And especially not when Pandora is
a witch with a penchant for surviving.”
It isn't clear how far her knowledge spans, but it appears that Echidna knows about Pandora.
Although, her expression as she speaks with Emilia is as bitter as ever, and she doubts that she will
get an honest answer if she asks her any questions.
Emilia: “...You're not insulting me like you were before?”
Echidna: “That's the kind of thing about you that I hate. Of course I'm thoughtful enough to be
considerate toward someone who just remembered the death of their mother. Even if that someone
is a filthy licentious whore.”
Emilia: “Thank you.”
Echidna gives a sigh, speaking no further comforts.
Noticing that she's coming close to smiling at Echidna's attitude, Emilia realises that she has been
attempting to divert her attention from the grisly memory before her in a show of weakness.
These resurrected memories are utterly things which shake Emilia's perspective of the world.
Things which overturn Emilia's life from its very outset.
After all, Emilia was going to save everyone in the forest—and so was her reasoning for devoting
herself to the Royal selection, but,
69
Emilia: “I wonder if anyone's still alive... in this frozen forest.”
Emilia had witnessed both Fortuna and Arch's deaths.
The BLACKSNAKE's attack was information which had been absent in Emilia's memory. She knew
the beast's might, and the wicked characteristic it possessed.
The Witchbeast of Blight the BLACKSNAKE infects living creates with a hundred diseases just by
contact alone. And it places curses on the land it travels, transforming the region into a locality of
death where only witchbeasts can live.
—How many people had survived before the village was buried in snow?
And were those who survived and now encased in ice uninfected by the Snake's pestilence?
This was equivalent to Emilia losing her very reason to fight.
Indeed, she can agree with these memories being sealed.
Even had Pandora not interfered, perhaps Emilia would have wanted to forget about these events.
That is how utterly hopeless these memories are.
Echidna: “...Standing here indefinitely won't end TRIAL.”
Echidna gazes at the silent world of snow.
Echidna: “The past went along without any issues. Challenger of the TRIAL as you are, you must
have recognized your greatest regret. Now you need to present an answer.”
Emilia: “Present an answer for the TRIAL?”
Echidna: “The first TRIAL is beaten by demarcating an end to the symbol of your regret. Do you
affirm the actions of your past self, or reject them? If you are unable to fully accept this and reject
the question, this will all end without the TRIAL being accomplished.”
Emilia gives a deep sigh.
She has thought over and over about what she needs to overcome the TRIAL.
When faced with counterfeit memories, she had questioned herself as to why she was unable to
overcome them.
Losing Puck, and having to take over the parts of herself that she had entrusted to him, was what
first let the cap on Emilia's memories come loose.
Now, Emilia finally stands at the starting point for the TRIAL.
But even though her legs have reached the starting line, she has lost sight of the starting line in her
own heart.
She left the forest because she wanted to save everybody, save her mother.
It's turned out that those ideas weren't even idealistic ones, they were straight-out fantasies.
Her mother is dead, and she doesn't know if the villagers are safe.
If she loses the reason that she set out on this path, what remains for Emilia?
70
Emilia: “—That's already been taught to me.”
Just when it seems that her heart is beginning to waver, a hand reaches out from the light and stops
her.
A powerful arm, to pull Emilia forward when she is lost as to her destination.
Don't give up. Look forward, raise your head, watch me.
Over and over, again and again, he had said that to her.
He knew that Emilia was weak, but roared at her not to stay weak.
When Emilia shook her head and insisted everything was over, he said that nothing was damn over
and pulled her back up.
When Emilia wanted to give up, thinking that she was useless, he had baselessly asserted that she
was the best.
The pain from their teeth striking each other, and the warmth of their overlaid lips, lights a flame in
Emilia's heart.
Emilia: “Mother loved me.”
Echidna: “—”
Emilia: “I wanted to help Mother Fortuna. I wanted her to hug me again as we slept in the same
bed. I wanted to tell her, countless times, that I love her.”
Echidna: “Then do you regret it?”
Echidna is asking about the moment of Emilia's decision, with the two hopes.
Back then, if Emilia had taken Pandora's hand and broken the promise, perhaps Pandora's group
would have withdrawn from the forest, and Fortuna and Juice would not have been stolen.
IF, HAD I, SUPPOSING. Using those words to look back on the past, perhaps this would indeed be the
case.
Emilia: “I don't regret anything.”
Echidna says nothing.
Emilia: “I don't regret that I kept my promise, and stayed my ground back then. If there's anything I
regret, it's that I wasn't strong enough, and couldn't consider things more wisely. I'll never regret
that I stayed true to my Mother's teachings and didn't listen to Pandora, ever.”
After all, hadn't Fortuna told her?
That she was proud of Emilia, who had determined to keep her promise, and that she was her
treasure?
Those very words were a treasure, to remain inside Emilia forever.
71
Echidna: “Your fight hasn't lost its meaning?”
Emilia: “Nope. I... couldn't save mother. But I still don't know about everybody in the village.
Everybody might be waiting there, waiting for rescue under the snow. I'm the only one who can
save them.”
Echidna: “That land's been polluted by the Blacksnake. Even assuming that there are villagers alive
under the frost, I doubt that they will survive long while harbouring infection.”
Emilia: “That's just how you're imagining it'll go. A nasty kind of speculation. Everybody's waiting
for rescue under the snow. I'm gonna get them out of there quickly, and they'll all tell me off. And
then laugh, glad to be alive.”
Echidna: “Imbecilic delusion.”
Emilia: “No, it's a forecast for a happy future!”
Emilia steps forward.
She faces Echidna and she gestures to the snowscape.
Emilia: “I won't let you invalidate something that no one's even seen yet! I'm not going to accept
that the things my Mother left for me ended so sadly! I'm going to realise my Mother's ideals!”
Echidna: “Ideals? Your mother was searching for something?”
Emilia: “She said so. That one day everyone would leave the forest, and be able to live like normal.
Just like how Juice's group and all the villagers could get along, and how Subaru told me he likes
me, one day that world will arrive which my Mother and Juice were supposed to walk together!”
Echidna: “And the frozen villagers will be included in that world? After you trapped them in the
ice?”
Emilia: “I feel sooo sorry about that. I'll apologize over and over, and over and over until they
forgive me! And once they forgive me, I'll show them the world. Tell them that they don't have to
live in secret any more. That this is the world that Mother Fortuna was talking about!”
Echidna: “—”
Taking a deep breath, Emilia shouts.
They are no longer in the snow, but a world of white light.
Heedless to the absence of the prickling chill, and to the departure of the scene composed of her
regrets, Emilia raises her voice.
Emilia: “I'll shout myself hoarse as I holler my dreams, so that my Mother in the sky can hear it!”
Echidna: “—”
Emilia: “I am happy in the world that my Mother loved!”
72
The world fractures.
Seeing the fissures run through the white space, Emilia finally notices the change in setting. Her
eyes widen in surprise, and Echidna strikes her hands.
Together, in applause.
Echidna: “I see, understood. I didn't expect that I'd know what would happen, but this exceeds
anything I imagined. This pushy, complacent, hubristic, egotistic, hypocritical and forced purchase.”
Emilia: “Exactly. Anything wrong with it?”
Echidna: “No, I don't really care. But this is one of those points where you're exactly like your
mother.”
Echidna scrunches her pretty brows, when Emilia asks her question.
Because it sounds like,
Emilia: “My, mother... you don't mean Mother Fortuna, you know about my other mother?”
Echidna: “I know her. She's part of why I get so emotional when dealing with you. Though there is
still some kind of irrational resentment to it, as I lament: why does it always only happen with
you?”
Echidna gives a shrug, her form beginning to fade.
Emilia feels a vague kind of weight press down on her consciousness, a floating feeling like waking
up from a dream circling around her.
Echidna: “Here's the end. No matter how complacent the logic is, a settlement with your past is a
settlement with your past. All you have to do is dance clumsily around as you take your mother's
resolve to sacrifice herself and use it as your rationalization.”
Emilia: “You can say anything you want. Me, I've gotten used to your insults.”
Hand to her hip, Emilia shows off her composure to Echidna, who doesn't forget to give one last
jab. Echidna averts her gaze.
Echidna: “There's still two TRIALS left, but... frustratingly, I doubt they'll prove much of an
obstacle.”
Emilia: “They won't?”
Echidna: “Constant rationalizations are the nemesis of self-inquisition. These TRIALS, which intrude
on your interior, have terrible comparability with the present you. You could call it a boon resulting
from your utter neglect to think.”
Emilia: “When you talk in a way that sounds like I'm not thinking, it actually strings sooo much.”
Emilia bares her displeasure.
73
That said, their conversation here is close to meeting its end.
Echidna is practically gone from view, and Emilia's head is beginning to fog. She cannot keep
herself conscious any longer.
Echidna: “—I hate you.”
Emilia: “But I don't really hate you.”
What expression did Echidna make in this moment? Even though Emilia doesn't see it, she gets the
sense that she knows.
Her consciousness, ascends.
※ ※ ※ ※ ※ ※ ※ ※ ※ ※ ※
Emilia regains her conscious and groans, a hardness at her back.
Behind her is a wall. It seems that she has collapsed against it, and fallen unconscious with the thing
still supporting her.
She reaches out to touch the wall and checks the writing rudely engraved there. She runs straight
into an I LOVE YOU, and winds up smiling at the perfect timing.
Right now, Emilia wanted his words more than anyone else's to be the ones validating her.
Emilia: “—I'm sorry, Mother.”
Her smile twists, as her voice slips, choked, out of her mouth.
Her apology echoes through the dark room, as does the noise of her sniffling.
Teardrops stream one after another, unstoppable. Unendurable.
She had chosen to act strong, to be stubborn, and not let the witch see her cry. Inside this tomb,
where there are no worries of any onlookers, Emilia presses her face against the wall and cries
magnificently.
Emilia: “Mother... mother...”
The tears overflow.
They're truly from forever ago. Tears that she needed to cry one hundred years ago.
She had forgotten about it, and so had never been able to mourn her mother's death. In this small
chamber where no one will know about, Emilia proceeds to mourn exactly that.
So that once she exits, no one will know what her face looks like in tears.
So that she could end this, without the boy who told her weak self that he loved her seeing her being
weak.
74
She cries, and cries, and cries, and cries.
All while mourning the memories of her mother, her mother's affection, and everything she had
given her.
Emilia remains exactly like this, proceeding to cry with her face pressed to LOVE.
75
CHAPTER 121: HELP HIM
She wipes away her tears and pats her cheeks.
She combs her fingers through her hair, bordering on a mess as it is, and smooths out the wrinkles
in her clothing.
Did her face look horrendous right now?
Puck would usually be here to comment about Emilia's appearance, but he isn't. Though, the
misshapen crystal that Garfiel gave her does reassure her with its dim light.
Emilia: “...We won't be seeing each other's faces for a while.”
The crystal in her hand siphons her mana out from her fingertips.
It's an uncontracted Great Spirit, and all it's doing is resting there inside the anchor, but it still
demands an incredible load of mana. Had Subaru or Garfiel spent a full day accommodating that
mana drain, they may have been run utterly dry.
But even the forcefulness of this mana drain pales in comparison to Emilia's vast stores of mana.
Emilia has regained her memories, and remembered that she can use magic without a spirit's help. If
she focuses her attention on her gate, she can feel the outrageous current of mana circulating
through.
Emilia had been why Puck could manifest in reality. Puck would brag that it was happening using a
conglomeration of ambient mana, but most likely, a large portion of the feat drew off of Emilia's
unacknowledged mana stores.
All of it, so that Emilia would not have to face her forgotten memories.
Emilia: “You really are so overprotective.”
With a slight smile, Emilia raps her finger against the crystal.
Perhaps in protest, or perhaps smiling wryly, the crystal strobes its light in response.
Emilia: “...Okay. Mm, everything's fine now.”
Her mood has calmed down considerably, too.
Thinking about Fortuna or Juice makes her heart sting, and should she relax her guard, she will
definitely wind up crying again.
But Emilia cannot stay cowering forever.
She has things she needs to do. And they were surely things that Fortuna and Juice would expect of
her, and desire from her.
She exits the TRIAL room, and heads through the stone corridor, making for the exit.
Two TRIALS remain. Overcoming the first TRIAL isn't enough to make the door in the chamber
open. Most likely, she will need to complete all the TRIALS before it will.
The requirements to make the next TRIAL start are unclear. Exit and enter the tomb again?
Potentially a passage of time? Either way, the TRIAL did not heartlessly start on her during her
period spent crying in mourning. So it feels like re-entry is the requirement.
76
Emilia: “What would I do if Echidna does something mean to me? ...I think she was sooo mad at
the end.”
I hate you, she said. But I don't really hate you, replied Emilia.
Part of that comment had been revenge against Echidna and her constant belittling of her, but
considering that this witch was in command of the TRIALS, perhaps she could have used a little
more self-control.
Emilia: “I wish for you to please not be too mad.”
While praying for Echidna's good behaviour, Emilia heads for the tomb's exterior. Moonlight
spilling in at the end of the hallway informs her of the exit.
She instantly forgets about Echidna for now and raises her head cheerily.
That past she remembered was assuredly nothing trifling.
It still doesn't quite feel real yet, but it was definitely a huge and unshakable event which composed
part of the foundations of the character called Emilia.
But for now, all she wanted was to inform the people who believed in her that she had beaten the
TRIAL.
To see the person who said, You can do it, and tell them: I did it.
Squinting under the dazzling moonlight, Emilia exits the tomb—
???: “I welcome your return, Emilia-sama.”
Greeted at the square outside by Ram and her curtsey, not a single other person in sight, Emilia tilts
her head.
※ ※ ※ ※ ※ ※ ※ ※ ※ ※ ※
—We'll rewind time a little, back to when Emilia's TRIAL began.
While traversing the route to Roswaal's recuperation hut, intending to verify the guy's motives,
Subaru swallows his breath and stops still.
He can tell that Garfiel, walking beside him, also has his eyes shoot open in clear shock. For him,
this situation truly must be a bolt out of the blue.
Subaru had imagined some circumstances and possibilities beforehand, but even he cannot conceal
his surprise. While feeling some sympathy for Garfiel, Subaru sighs at the character blocking their
path,
Subaru: “I did think you'd be around... but actually seeing you makes me feel kinda defeated.”
???: “Now thert's a serprise. Goin' by what Roz-bo said, yer got eyes enough ter see through the
whole erv everything, Su-bo.”
Subaru: “That's him anticipating too much. Seriously, how huge are his estimations of me?”
77
From Roswaal's perspective, where he is aware of RETURN BY DEATH—or rather, the Redos, then
indeed perhaps it all looks like the doings of an omnipotent god.
But the power isn't that infallible. It provides absolutely no help in reclaiming what precious things
have already been lost. That's the sort of unhappy power it is.
Narrowing her eyes, the pink-haired girl—the look-alike for the Lewes who they parted with
outside the tomb, one of the Lewes Meyer doubles—smiles slyly.
Subaru had anticipated her existence and his reaction only amounts to him slumping his shoulders,
but Garfiel's reaction is dramatic. His eyes peel wide as he glares at the face of his grandmother,
Garfiel: “Th'hell... why th'fuck's there another granny here? There ain't more than one talkin'
granny, n' th'rest'v th'fellas who got granny's face're under my orders to...”
Lewes: “Everything has its exceptions. ...Right. If we say that the Lewes Gar-bo knows as the
representative of SANCTUARY is the place's overseer, then I'd be the caretaker of SANCTUARY's
faculties. A will inherited from Lewes Meyer, continuously protecting the place.”
Subaru: “Then speaking in terms of the system, you're against SANCTUARY's freedom. I thought it
was weird that none of the Leweses were against liberation and goading Garfiel. So the one who
secretly took that role... was you. —Lewes Omega.”
It's not Lewes who reacts to the name, but Garfiel. He glances back at Subaru, looking dubious.
Garfiel: “Ohmegah?”
Garfiel: “Hell's that, Captain. That name.”
Subaru: “When there's several of them and you don't differentiate them, it's hard to keep the Lewessans
straight. So just for expediency, we're calling the Lewes-sans we know Alpha, Beta, Sigma,
and Theta. But now there's obviously a fifth Lewes-san, OMEGA. Not thrilled with it?”
Garfiel: “No, I just mean that name's way too cool f'r th'granny... ain't fair.”
Subaru: “Basically. When there's more of you, I'll give you cool names too.”
Garfiel: “But there ain't gonna be more of me...”
It seems like Subaru's naming sense has appealed rather intensely to Garfiel. The two recognize this
unexpected point they have in common while Omega sighs.
Omega: “I dern't mind whatever yer gonner call me, but yer leaving me behind ter have a happy
chat. Since when have you two been such good friends?”
Subaru: “Men who trade fists with the evening sun as their backdrop are always pals. Even if comes
after getting decked following a four-versus-one. Right, Garfiel?”
Garfiel: “Well yer sure got over whatever goddamn guilt yer had, Captain.”
It seems like Garfiel still cannot really agree with losing due to force of numbers, but coming from
him, the jab is pretty poor. That aside, the joking around to buy time and think ends here.
78
Subaru faces Omega. She strokes her long hair.
Omega: “The look in yer eyes's changed. Not a kid ter drop yer guard around.”
Subaru: “This whole kid thing feels pretty fresh, not bad. Omega-san, do I have this right? You're
not like the other Lewes-sans, you don't have a rotation? I really don't want to have Gamma,
Ampersand, Dollar, and Pound show up too.”
Subaru goes off listing whatever signs he can think of. Garfiel's eyes sparkle.
While Subaru consciously ignores the admiring gaze of a fourteen-year-old, Omega strokes her flat
chest.
Omega: “Dern't worry. I'm the only one holdin' the role erv overseer. Without a spec'erv a doubt, I'm
the last Lewes in SANCTUARY with any sense of will.”
Subaru: “Not gonna go back on that comment? Going off who I know, up to 20,000 people with the
same face'll show up.”
Omega: “Now that has ter be going too far. SANCTUARY wouldn't be able ter hold us.”
His worst fears undermined, Subaru relaxes.
He furrows his brows at the calm Omega.
Subaru: “I mean it's nice that you're just telling us who you are, but... what happened? With how
you've been treated like a hidden gem up till now I was thinking entirely that you'd be in the
shadows. So why're you suddenly showing up now?”
Omega smiles.
Omega: “It ain't nothing tricky,”
Omega: “The peace between yer and Gar-bo meant yer figured out I exist. Yer might not've
actually got yer grips on me, but the second yer think that MAYBE SHE EXISTS, I lose. I showed up
figuring I'd behave nicely to face my judgement.”
Subaru: “Saying 'face judgement' is really overstating it. ...But there has to be more to it than that,
yeah?”
If Omega seriously wanted to achieve her goals, she surely could have played more of a hand. Even
should Subaru's group suspect her existence, until they manage to actually find her, she remains the
superior party.
Subaru: “Call it guerilla warfare or whatever, if you ever felt like being an obstacle, you could've
been. And your role is being the Joker to pull that off. Roswaal's been keeping quiet about your
existence this whole time, and...”
Omega: “Roz-bo's state is part erv why I'm showing up so nicely.”
Subaru: “Roswaal's, state?”
79
Subaru's eyes widen. Omega shakes her head.
There's something sardonic about that attitude, and cavalier.
Omega: “Yer take a look at Roz-bo as he holes up in his room right now, and yer'll figure out right
away why I'm thinking erv just giving up. And erspecially when I was helping him as SANCTUARY's
caretaker, with the idear that he'd steer the place int'er its correct form. ...Not gonna happen with
that.”
Being that Subaru knows the other Leweses, he finds Omega's dejected remark to be rather harsh.
Perhaps Garfiel interprets her comment as being strict too, for he does not interject about her
unsparing opinion of Roswaal.
Omega is tasked with being SANCTUARY's manager and caretaker. It's unclear when she first got that
role, but she's probably been active for much longer than Alpha and the others. Her current attitude
may have been built up over all that time.
Regardless,
Subaru: “Nevermind whatever you've been doing until now, is it safe for us to think that you're not
gonna get in our way any more?”
Omega: “Well, if yer follow my views on the correct steering, then I still got lotser things I'd like ter
interfere with. SANCTUARY's liberation ain't what Lewes Meyer wished fer... but, times are times. If
the era means that SANCTUARY stops being necessary, then my role isn't needed either. What's kept
me going until now wers essentially the thought erv not wanting ter be left behind.”
Omega's voice is somewhat sad, with anxiety peeking through about her role's end. This post she
has served for so long is reaching its conclusion.
Subaru doesn't know what exactly Omega feels when she reminisces on her life. While a good
portion would be a sense of will and volition, perhaps there would also be a sense of liberation
smattered there too.
Garfiel: “Stubborn, ain't ya. 'S a good thing t'be, granny.”
Omega crosses her arms and looks up at Garfiel as he clicks his fangs.
Garfiel: “'S same fer me. I was stubborn like yer were, granny Omega. N'my thing was even worse
than yers. But th'Captain used his strength, used his numbers, n' smashed th'whole fuckin' thing
apart. Was honestly thinkin' 'fuck this!'... but now I just feel damn refreshed.”
Omega: “Gar-bo...”
Garfiel: “'S what th'Captain said. SANCTUARY losin' it's barrier don't mean that th'world we live'n's
gonna be gone. SANCTUARY disappears, n' th'whole'v th'outside world becomes a SANCTUARY. 'N
there, both you n' my amazin' self got things we can do.”
Omega looks down, in thought.
Her expression loses its anxiety and her brows uncrinkle. Instead she looks to be scrutinizing
Garfiel's words, and he nods in satisfaction.
Subaru taps Garfiel's shoulder.
Subaru: “Garfiel, do you... have a fever or something? You are saying some super smart, super
80
embarrassing stuff right now.”
Garfiel: “Captain. Do y'think I got th'brains t'come up with this? 80% of what I just said's comin'
second hand from you.”
Subaru: “Seriously? I said that? Nononono hold on, oh crap, belated mortification.”
Garfiel gives an astonished sigh as Subaru squats down to the ground, ears red. He then faces
Omega again and swings out his arm, gesturing an open path.
Garfiel: “I get what yer sayin', granny Omega. N'yer basically answered what I was gonner ask.
Now's just ter question 'bout th'nefarious plot, n' showin' up in person t'see th'asshole who came up
with it.”
Omega: “Anything yer want. ...Wonder what I'll do.”
Mutters Omega. Subaru hums his agreement.
Omega had been keeping her existence a secret. Not even Alpha and the other Leweses noticed her
or what she was doing. Now that her role has ended, Omega can appear in public for the very first
time.
Subaru: “If you go to the tomb, Ram and Alpha-san's group... right now it's Theta-san. They're
waiting there. They've probably already figured out what's going on, so just go and talk with them.”
Garfiel: “They figured out what's goin' on, goddamn seriously? My amazin' self didn't figure a
single thing'v this.”
Subaru: “That's 'cause your head's running a whole lap behind.”
It's actually more baffling that he didn't get an idea of it, after that past conversation. All those times
where Garfiel's instinctive actions impeded Subaru's activities in SANCTUARY float through his mind.
Either way, Omega's anxiety is probably needless. Theta knows that there are many duplicates of
herself, and Ram probably knows about the duplicates too. They'll accept her.
So the problem is,
Subaru: “The mastermind of the nefarious plot, a face-to-face conversation with the boss clown.”
※ ※ ※ ※ ※ ※ ※ ※ ※ ※ ※
When he enters the room, Subaru has to wonder if he's even been here before.
Roswaal has been in this room ever since Subaru first came to SANCTUARY. This is the room he has
visited every time he has wanted to talk with Roswaal. He can even remember where all its
ornamentations are arranged, and yet.
Roswaal: “Weeeeeeeeell, if it iiiiiiiiiiiiiiisn't Subaru-kun. How nice of you to come. Even though
you must be veeeeeeeeeeeery busy.”
81
Subaru stands wordlessly with his hand still touching the opened door as Roswaal glances back at
him, and speaks in that aloof tone. He gives a joking kind of shrug, which prompts Subaru's heart,
for an instant, to want to think that nothing is irregular. But Subaru suppresses that thought and
instead faces Roswaal.
The room is an absolute mess.
The bookcase has been overturned, and the ripped white bedsheets lie dumped upon it. The bed is
broken in two, wood chips everywhere. The warlock stands in the middle of this destruction with
his hands dripping blood.
Seeing the splinter-wounds on his hands, Subaru recognizes: He just smacked the bed apart.
Garfiel: “Captain...”
Having also seen what a wreck the room is, Garfiel takes a half-step forward, placing himself in a
position where he can protect Subaru. Roswaal's abnormal state is not evoking a caution in merely
Subaru.
Garfiel's golden eyes are clearly wary. He stoops his body forward, so that he can immediately
suppress Roswaal should he do anything shady.
Roswaal: “Hoooooooow domesticated you've beeeeeeeecome, Garfiel.”
Says Roswaal mockingly, his lips twisting in malevolent crimson.
Keeping that smile, he closes one eye to view Garfiel only with the yellow.
Roswaal: “It's shocking how quickly you changed your tune. You're protecting Subaru-kun, which
means that you've been added to his merry band of friends. Aaaaaaand that you took your will of
wills, the love that you have held so long for your mother, and discarded it.”
Subaru: “Roswaal, you're wrong. Garfiel isn't allying with us because he had some change in his
feelings. He's just shifted his ideas a little, and...”
Roswaal: “Thaaaaaaat is what I'm saying is superficial. You are beaten up en masse and lectured,
and that's all it takes to change your stance. Your feelings are so weak that losing a fight is enough
to change them. Easily altered, shoddy.”
Subaru: “Roswaal!”
It is Subaru and not Garfiel who gets enraged with Roswaal's screeds of heartless words.
After finishing the intense fight with Garfiel, Subaru came to understand a fragment of his feelings,
a fragment of his mental pain. And also came to understand that it was assuredly nothing frivolous
or cheap.
Roswaal cannot be forgiven for trampling all over Garfiel's feelings.
Subaru: “You take that back! You don't have any right to mock Garfiel's feelings!”
Roswaal: “Call pliant what is pliant. Call brittle what is brittle. Is there any reason to be criticised
foooooooor stating facts? Your overreaction actually reinforces my statements' legitimacy. A
twopenny sketch where cheap relationships try to validate cheap feelings. Truly... an offence to the
eyes.”
82
Subaru: “—!”
Subaru moves to approach Roswaal in a rage.
But the one who stops him is in fact Garfiel. The one most wounded by Roswaal's insults, Garfiel.
Subaru can imagine how hurt he must be as he timidly turns to glance at his face.
However,
Garfiel: “Yer words ain't got a lotta punch t'em, Roswaal.”
Says Garfiel, his arms crossed in boredom and head lightly tilted.
The attitude shocks Subaru, and does the same for Roswaal.
Had this been a Garfiel from just a little while ago, he surely would have left himself to rage and
snapped at those words. But he, right now, disregarded them. As if he were bathing in a warm
breeze.
Garfiel: “I ain't able t'deny that 'm full'v half-measures. 'Till this mornin' I was on yer side, n' now
I'm on th'Captain's. Yer right when yer say it was a quick change'a tune.”
Roswaal: “After your perfidy toward your beliefs come the rationalizations, I seeeeeeeeee.
Goodness me, it appears that the strength you've validated all this time also proooooooooves
substandard in reality. Ten years... assuredly no short period of time, only for a handful of days to
alter your doctrines.”
Roswaal shrugs and shakes his head. A murky emotion rises in his odd-coloured eyes as he glares at
Garfiel.
Roswaal: “And that is what I'm calling cheap. If you really loved her, then your feelings would
never change their form. Do you believe that your ten years, and Emilia-sama's century, can be
handled so cheaply?”
Garfiel says nothing.
Roswaal: “All you did was interact with Subaru-kun for a handful of days. What could possibly
happen in this time? Did you create something with him which could rival your feelings toward the
one you love? Of course you didn't! No matter what you create with those at your side, it will never
compare to what you feel for your love! It won't rival it! That is what it means to love someone
most!”
Roswaal kicks a piece of bed which had fallen to the floor. It rebounds and flies toward Subaru and
Garfiel, but strikes neither of them as it instead hits the wall behind them.
Splinters of wood rain to the ground. Roswaal's assertions make Subaru hold his breath.
—Scour away everything except what is most important.
That is what loving something meant to Roswaal.
There is nothing precious he builds outside of the one he decides on, and he finds no necessity to
build up anything precious outside of that, either. His feelings toward that one thing are then
ironclad, and if opportunity exists for him to bring them to fruition, he will not hesitate in the least.
This is what Roswaal believes 'love' is.
83
The moment Subaru comprehends Roswaal's thoughts, Roswaal looks at him as if he noticed it.
His yellow eye churns with the outrageous zeal of love, consuming.
Roswaal: “Do you remember the terms of our bet? The bet that you presented. Once that bet leads
you to bind your greatest prepotency and become mundane, what can you do? You can do nothing.
Because you... you, are so inferior that you can't even manage mediocrity!”
Subaru says nothing.
Roswaal: “The potential for you to be a foolproof ace exists solely because you have that power.
Once you throw that away and become mundane, within a time limit you won't even be capable of
floundering at ordinary par! Nobody! After living with one another, is capable of overcoming
feelings engraved over time! It doesn't happen!”
Garfiel's decade of obsession with SANCTUARY and distortion of his love for his family.
Emilia's century, with a past so terrible that she wanted to forget, and guilt that she left behind.
And,
Roswaal: “A decade, a century, and my four centuries! Do you think I can tolerate for even a second
that you, nobody else but this mundane you, are the one to overturn that!”
Subaru: “Because feelings never change?”
Roswaal: “Exactly!”
Subaru: “Because you've had these feelings for a long, long time?”
Roswaal: “Yes, exactly!”
Nobody can overwrite their feelings. Feelings will never, ever, change or bend.
Finally, Subaru feels that he gets it. Finally, he feels that he understands Roswaal.
Roswaal wants his feelings to be validated.
He wants to validate somebody else's feelings, so that he can believe that this is what feelings are.
And so Roswaal wanted Garfiel to remain weak.
He wanted Garfiel to remained obsessed with his feelings, frantically protecting something that
wouldn't change.
Subaru: “Seriously, how come, Roswaal?”
Feelings for one single loved one.
For the sake of validating that, Roswaal is obsessed with what others are like when they have
feelings for someone.
Even though Roswaal should know better than anyone what it is for someone to feel something for
someone else.
Subaru: “How come you only see the weakness of love? If you know that loving someone without
84
end is a strong emotion, how come you only see the weak things about it?”
Roswaal: “—Because that's what I believe.”
Replies Roswaal, his voice strangled.
Incredible fury flashes through his eyes, as if he were glaring at the thing he hated most in the
world.
Roswaal: “Exactly! Like how you believe in others' strength, and expect things from them! I believe
that everybody remains consistently weak! They are weak, frail, minuscule people, incapable of
actualizing their love for their precious one outside of merely clinging to them, that is what I
believe!”
Subaru: “—!”
Roswaal: “I have gone four centuries without ever forgetting about her! The time we've spent apart
is infinitely longer than the time that I spent with her, and still she is emblazoned in my heart and
never going to leave! My heart is still in pieces from that day of our goodbye, nothing about me has
changed!!”
Roswaal steps forth.
Garfiel cuts in to stop Roswaal from approaching Subaru. But Roswaal puts his hand to Garfiel's
chest, looks down at him,
Roswaal: “Wasn't it easy? When you spent ten years giving heed to the shouts of love inside you,
and through that time believed in them obstinately, didn't you manage to bask in the feeling of
loving someone?”
Garfiel: “—! Bastard...”
Roswaal: “It's fine, entirely fine. It's what everybody ought to do. There is no person capable of
living in solitude! All live with feelings for another. And that is enough... so then why are you
attempting to alter your feelings. Attempting to betray them. Did you not love her!?”
Garfiel: “Yer got it wrong! I...”
Roswaal: “What changed you!? Your muscled body was defeated in a fight, and you lost? You spent
ten years for a malleable love, bent by the shattering of your fangs? Then the one disgracing and
desecrating your ten years is in fact you yourself!”
Garfiel knocks away the hand at his arm. He attempts to use the backswing to thrust Roswaal back,
but Roswaal wrenches himself aside and evades. Garfiel's eyes shoot open as Roswaal grabs his
arm and hoists him into the air.
Garfiel: “Hrah—!”
However, once Garfiel hits the peak of the attack, he puts his foot to the ceiling and manages to
overpower Roswaal's momentum, saving himself from slamming back-first into the hard surface.
He forces his body to flip around, giving him three points of contact minus his grappled arm. He
rewards this by yanking his grappled arm, pulling Roswaal closer, and ramming him in the chest
85
with a headbutt.
Roswaal: “Ghuh...”
Garfiel: “Ha! 'F I hadn't heard from th'Captain that yer can do martial arts too, yer'd've gotten me
good.”
Looking down at Roswaal as he falls to his knees, Garfiel gives a roll of his previously-grappled
arm.
He bares his fangs.
Garfiel: “Hey Roswaal. Yer sayin' things that an idiot like me ain't gonna understand. Yer can go on
about yer four centuries, but fact is yer a young guy who maybe ain't even thirty. N' I know my
amazin' self's sittin' at half'v that.”
Garfiel reaches out to grab Roswaal's collar, hoists the clown close.
Roswaal's face is twisted in pain. Garfiel scrunches his nose.
Garfiel: “But it ain't that my amazin' self's goin' with th'Captain 'cause I lost a fight. 'S true that
th'loss did smart. Yer said it, my amazin' stubbornness's been doin' me good fer ten years. My head
ain't mushy enough fer a loss t'turn that around.”
Roswaal: “Then why are you standing in this room...”
Garfiel: “'Cause th'Captain... actually, 's was Ram. Sh'told me this after I lost. T'go into th'tomb n'
look at th'TRIAL. N'so, ten years later, I saw what started these ten years'v feelin's.”
Roswaal: “Wha?!”
Shock flashes through Roswaal's expression.
Roswaal: “Impossible... you're, you're not capable of facing your past again!”
Garfiel: “Yer can say 'm not capable all yer want. I already went n' done it, n' saw what I saw. N'so,
I wound up understandin'.”
Roswaal glares at Garfiel, who shakes his head. That silent, focused gaze of his is waiting for
Garfiel to divulge what he learned.
But, Garfiel merely opens his mouth wide, and,
Garfiel: “I ain't gonna tell yer what I figured out. 'S a waste on you.”
Roswaal: “What!?”
Garfiel: “But I will tell yer one thing, why'm sidin' with th'Captain.”
Garfiel lets Roswaal go, sending him toppling down to a graceless landing on his behind, and looks
at Subaru. He sighs slightly as Subaru flinches at the intensity of it.
Garfiel: “'S cause of goddamn course yer'd rather team with th'people sayin' yer strong, we need
86
you, than someone makin' yer think yer gonna stay weak forever.”
With that incredibly reasonable logic, Garfiel looks away from Roswaal. He passes him by, to stand
beside Subaru with his arms crossed.
Subaru glances over at him. And away. And over. And away. And—
Garfiel: “What.”
Subaru: “...No, it's nothing. Counting on you.”
Garfiel closes his eyes, looking uncomfortable, when Subaru speaks and then squats down in front
of Roswaal. With his neck down and head drooped, he makes no attempt to look at Subaru.
Subaru: “Roswaal.”
Roswaal says nothing.
Subaru: “Garfiel saw his past. That might've changed his viewpoint, but that doesn't mean the
feelings he's had for his family for the last ten years weakened or wavered. The strength of the
feeling stays the same, but he's changed. You don't find that idea a believable one?”
Though he may no longer be obsessed with Sanctuary, Garfiel's feelings have not weakened in the
least. He learned that his unreciprocated love for his mother was actually mutual, and how great a
shock did that give him? Subaru couldn't know.
But who could think that Garfiel was weak, seeing him now? Though he had wavered, and likely
would lament.
Subaru: “And it's the same for you. We're not telling you to warp these feelings you've had all this
time for someone. We just want you to change how you demonstrate those feelings. If there aren't
going to be sacrifices for it, then of course we'll help you.”
Roswaal: “...I cannot tolerate that. And so what does it matter if merely Garfiel's feelings have
changed? For our purposes, yet another vital person remains.”
Subaru reaches out to Roswaal. But Roswaal does not attempt to take his hand.
He shakes his head, terrible at surrender, as he speaks about Emilia.
Subaru: “Emilia's not going to do what you want either. She's going to overcome it.”
Roswaal: “She cannot. She'll be crushed by her regrets, regret ever hoping that she could change,
and come crying and clinging to you... as suits her.”
Subaru: “Like there's a girl out there whose face's suited to crying. And actually, have you even seen
her cry?”
Subaru recalls Emilia in the tomb, before their argument.
She was carrying a heavy responsibility, and grieving the loss of her bond with Puck. Her
expression when Subaru glared at her, unable to hold back her tears.
Recalling it lights a fire in his heart.
87
An unbearable inferno of rage, burning him whole.
Subaru: “I have never seen a woman so fucking horrendous at crying before!”
Roswaal: “To be wounded, to be disparaged, that is the lot of half-elves like her. Sharing the same
birth as the WITCH OF ENVY is a congenital curse. It's inevitable that she be despised as a WITCH.”
Subaru: “Fuck off, what about her's a witch? This witch you're talking about doesn't goddamn
exist.”
Roswaal faces down.
Subaru grabs his collar and forces him to look up, his eyes pitched in anger as he puts them on even
eye level.
Reflected in Roswaal's eyes is Subaru, blazing with an unstoppable fury directed at the world.
Yes. Right now, Natsuki Subaru is sick of everything in the world.
What about Emilia was a WITCH? There wasn't any damn WITCH.
And if there was one, it would be—
Subaru: “If you're saying she's a WITCH! It's because you all made her one! You keep telling her that
of course she's weak, it's obvious she'd be hated, all because of her useless birth, and you are going
to make her into a WITCH!”
He recalls the WITCH's tea party.
The scenes flash through his mind—of the old witches, titled with sin.
Minerva, Sekhmet, Typhon, Daphne, Camilla, Echidna.
And he remembers Satella, who saw him off the moment the dream shattered.
Like he could forget her.
Her face—looked exactly like Emilia's.
Subaru: “Has anyone told her even once!? That when she's sad, when she's suffering, it's okay for
her to cry! That if she can't wipe her tears away, someone at her side will do it for her! Has anyone
told her even once that someone would be there for her!?”
No matter what horrible things she goes through, she accepts it as natural.
Surely her heart would have been filled with pain, and it would feel like the sadness could crush her.
But nobody had allowed her to cry, making her so terrible at crying.
Over repeated experiences in crying and crying and crying and crying, everyone learns to keep the
tears out of their voice, out of their expression, and themselves out of sight.
But she doesn't know that.
She had made it this fare without ever knowing that, and so she was terrible at crying.
A world that would do this, a world that had done this—was presently so loathsome to Subaru that
he could go mad.
Subaru: “If the obvious thing in this world is for nobody to take her side, then my presence is going
88
to change it! You think four-hundred year curses can't change, and I'm going to teach you!”
Roswaal: “—”
Roswaal's eyes shoot open as Subaru jabs his finger to the heavens.
By some bizarre turn, his posture right now, and Emilia's pose to the insulting witch, mirror each
other perfectly—
Subaru: “My name is Natsuki Subaru! Knight to the silver half-elf, Emilia!”
Once, Natsuki Subaru had crowed the exact same line without any preparation for it, and many
mocked his foolhardy determination. Thinking back, he had been even more useless back then than
he was now.
But there is one thing different between now and then.
Even if someone laughs at him for it, Natsuki Subaru will feel no embarrassment.
Subaru: “Emilia's doing it, Roswaal. This girl you think's so weak is gonna tear right through the
last hope you have left.”
Roswaal: “As if, she can..”
Subaru “The weakness you're clinging to's getting peeled off bit by bit, and all that'll be left'll be to
talk to you... I'm trusting that you'll finally start to listen.”
Even after hearing all of this, Roswaal's heart does not yield.
He's exactly right. Something built over four hundred years can't be altered with just a single word.
It's like how Garfiel's decade and Emilia's century required both words and actions to begin moving.
Roswaal's four centuries will be the same. The actions and the words of Subaru's group will, finally,
affect him.
Is what Subaru wants to believe.
Roswaal: “...Regardless of what anyone may do, my feelings shall not waver.”
Roswaal crawls past Subaru. He reaches out his shaking hand to grab a black book beside the
broken bed, and cradles it to his chest.
A legitimate, future-charting GOSPEL.
Garfiel and Emilia have outgrown the weakness that Roswaal believes in.
Omega and Ram have diverted from Roswaal as he attempts to establish his path.
The only HOPE that remains for Roswaal now is the gospel.
Once he has lost its writ, Subaru will be able to speak with Roswaal genuinely for the first time.
Roswaal: “I'll, make it snow...”
Subaru: “Do what you want. I'm crushing all your plans and crushing them unremittingly.”
With that reply to Roswaal's nigh delirious muttering, Subaru turns to exit the room. He nods at
89
Garfiel, who seems to want to say something, and the two leave the room together.
At the very end, Garfiel glances back to the room with Roswaal in it. And, perhaps seeing
something in him as he is left behind, whispers:
Garfiel: “Y'damn idiot.”
※ ※ ※ ※ ※ ※ ※ ※ ※ ※ ※
Their conversation with Roswaal over, Subaru exits the building and gives a sigh.
A deep one, wringing all of the air out of his lungs, expelling everything in him.
Subaru: “Crap. We were trying to make him stop the attack on the mansion, but it feels like we just
cornered him into doing it.”
Garfiel: “Started talkin' some nonsense crap 'bout makin' it snow, too. Didn't look like we were
gonna get a real conversation outta him... it ain't yer fault, Captain.”
Subaru: “No, I totally cornered him when we didn't need to. Even though I knew the second we
went in that Roswaal wasn't exactly in a normal state of mind, what the heck was I doing?”
Subaru feels like he finally understands Roswaal's principles and motives in earnest. And Subaru
has clearly given his response and feelings regarding them.
He did think it necessary to inform Roswaal that Emilia was going to clear the victory conditions,
so that he would acknowledge his loss.
But—
Subaru: “Doing that meant we lost out on the most important point...”
Garfiel: “'M tellin' yer, don't get down 'bout it. Ain't like my amazin' self got curious listenin' from
aside wonderin' what yer were gonna do, but what yer said ain't anythin' incorrect.”
Subaru: “I mean, that's the idea...”
Garfiel: “But anyway... that pose was so cool!”
Giving Subaru a smile, Garfiel promptly jabs his finger to the heavens.
Honestly, the pose has only ever gotten terribly negative reviews since coming to this world, so
finding someone who can empathise with it is the peak of happiness.
It's Garfiel's way of comforting Subaru. Probably. Hopefully.
???: “—Natsuki-san! Garfiel!”
When somebody calls to the two.
They glance over, to see Otto running toward them. He had been doing something else, and comes
to a stop before them.
Otto: “It looks like you're done speaking with the Margrave. How did everything go?”
90
Subaru: “Yeah. Got him to pick up the fight we put down.”
Otto: “Was that what we were attempting to do here!?”
What they were actually meant to talk about was the final trap that Roswaal set in SANCTUARY, and
try to make him change his mind about it.
They found out about Omega's presence on the way to Roswaal's, and Roswaal is too thick-headed
to change his mind about anything. Negotiations have failed.
Garfiel: “Hey, guy. Don't get on th'Captain's case too much. He did this super fiery awesome
backtalk. Put me in a good mood hearin' it.”
Otto: “Do you remember what you went there to do? This truly isn't a joke.”
Unable to refute Otto's complaints, Subaru reaches the peak of guilty reflection.
But Garfiel gives the dejected Subaru a boisterous slap on the shoulders, and raps his finger off a
dissatisfied Otto's forehead. He watches as Otto yelps, pitching back, and squats down to the
ground.
Garfiel: “Yer right, th'talk didn't go great. But all that was a back-up plan anyway. —I'll be doin'
somethin' bout th'trouble at Roswaal's mansion.”
Garfiel guffaws in reply to Otto's silent criticism.
He bares his fangs, and with a loud click,
Garfiel: “Leave everythin' t'my amazin' self. —I am th'goddamn strongest.”
※ ※ ※ ※ ※ ※ ※ ※ ※ ※ ※
Ram: “And so the three idiots and one clever dragon have departed by carriage for the mansion.”
Done with the story, Ram puts her hand to her chest with her expression rather exhausted.
It's a rare thing for Ram to display emotion when around Emilia, and surprises her a little.
Emilia: “I see then. ...Well, I guess they had to.”
Ram: “...Is that all?”
Emilia: “That's all. I mean, I am still a little... sooo just a little miffed that they weren't waiting for
me.”
All those talks, and they're not even around to see how she did. What's with that.
Emilia: “But it means they don't think I'm going to fail.”
If Subaru really was more worried about Emilia than anything else, then he would've stayed behind.
His absence here means that somewhere else, there is someone who needs his help more than her.
91
Since Emilia knows that Natsuki Subaru trusts in her, that's how it seems.
Emilia: “I wonder if he really does love me. What do you think?”
Ram: “Barusu has more feelings for you than he does for anyone else, Emilia-sama.”
Emilia: “...Huhuhu, thank you.”
Emilia puts her hand to her mouth and smiles, for Ram to lower her gaze in thought.
After a few seconds of silence, she looks up again.
Ram: “Emilia-sama, I must apologize.”
Emilia: “What's wrong?”
Emilia's eyes widen.
Emilia: “It's sooo uncommon for you to apologize.”
Ram: “I think the same. ...However, now is the first time that I bow my head to you sincerely.”
All of my curtseys up until now have just been poses, announces Ram. Emilia smiles wryly, while
Ram looks her straight in the eye.
Ram: “I... did not believe that you would come to stand. The TRIAL had broken your spirit, you lost
the Great Spirit who was your support... you even learned that Barusu had been keeping secrets
from you. I did not think for a second that you would rise to your feet.”
Emilia says nothing.
Ram: “However, even with all that has occurred, you have not yielded. When you left your bed, and
I realised that you had gone to the tomb... I at least recognized that I had been discrediting you.”
But even so, Emilia hadn't gotten back to her feet at this juncture that Ram is indicating.
She just hadn't tried to abandon the TRIAL. That alone was something that she never considered. She
could assert that.
Emilia: “And so you helped Subaru and Otto-kun?”
Ram: “I merely believed that my assistance would lead to a future worth seeing. It would be wrong
to perceive it as myself assisting them. The person I had been assisting was you.”
Emilia: “...You might be right.”
Subaru's words were indispensable for Emilia to get back to her feet.
And Subaru's defeat of Garfiel was necessary to prove those words. And defeating Garfiel required
Otto and Ram's help.
Looking only at the results, you could say that Ram aided Emilia.
Emilia: “Why did you do that for me?”
92
Ram: “—Because it is essential to demonstrate your own sincerity before making a request.”
Emilia: “—”
With that, Ram kneels before Emilia.
Whenever Ram demonstrated politeness around Emilia up to now, however insincere the sentiment
may have been, it was always by grasping her skirt and preforming a curtsey. Something within the
scope of a maid's duties.
But this time is different. This is the ultimate demonstration of politeness, where anyone living in
this world illustrates all the respect that they have.
Ram: “I ask of you, Emilia-sama. —Please save my master, Roswaal-sama.”
Emilia: “...Save Roswaal?”
Ram: “He is preoccupied with delusion. A curse of a delusion, which has kept his heart bound for a
long, long time. Perhaps I would have been happy even with that. Even should he never cast his
gaze upon me, and never regard me as more than a tool to accomplish that delusion, I would have
been happy.”
Still kneeling, Ram bares her heart to Emilia.
Beneath her expressionless mask, she may have been holding this wish the entire time.
Ram: “However, his delusion is no longer capable of taking form. The world has diverged from the
writ of the gospel, the basis for everything, and Roswaal-sama now clings merely to letters... I
request that you may destroy it.”
Emilia: “Will Roswaal be okay if that's destroyed?”
Ram: “I doubt so. He will likely be thrown into disarray. He may lose sight of his life's meaning and
suffer breakdown. But you are the only one, Emilia-sama. Who might be able to grant Roswaalsama's
delusion... his feelings, in a world diverged from the gospel's writ.”
Her head bowed, Ram pleads Emilia.
Half of her speech is failing to communicate clearly to Emilia.
Roswaal's gospel probably means that black book that he showed her. He had also mentioned that
the world was diverging from its text.
What would Roswaal do in a world different from what the book said? How could Emilia do
anything to do something about the hopes of a hopeless Roswaal?
Emilia: “What do I have to do?”
Ram: “—I ask for you to ascend to the throne.”
Emilia: “—”
Ram: “For you to be seated upon the throne of Lugnica. Once you achieve this, Roswaal-sama's
feelings will be fulfilled. Please teach Roswaal-sama that the day will come where his love is
93
realised. Give him reason to live for today, and for tomorrow.”
This is the first time Emilia has ever seen Ram so talkative.
And so.
And so...
This emotion flooding up in Emilia's heart, indescribable, is...?
These feelings, unstoppable, as someone who had thought her useless requests her aid, are...?
Ram raises her head.
The great love filling every inch of her small form glistens wet in her cerise eyes.
Ram:
“Please, Emilia-sama. —Help him.”
The quiet words make Emilia shiver.
It feels like a shock to her bloodstream, enough to imagine that a hand is jolting her heart once,
twice.
After the shiver races through her body, only one thing remains inside Emilia.
Blazing hot in her heart, solely a sense of duty.
Emilia: “I honestly don't know how me being Ruler will save Roswaal.”
Ram: “...”
Emilia: “And I don't think I can truly understand what your feelings are, either.”
Ram: “...”
Emilia: “But.”
Returning Ram's silent gaze, Emilia takes a breath.
Hesitation is gone from her heart. Anxiety is gone from her mind.
Her soul blazes hotter than ever before.
Emilia: “This is the first time you've ever requested anything from me.”
And so,
Emilia: “I'll do it, Ram. You believe in me, and I want to answer to that.”
94
In this instant, the things that Emilia ought to do and wants to do overlap so perfectly that there is
no need to deliberate. She says with a smile:
Emilia: “And that's definitely something I'll need to start, right here.”
95
CHAPTER 122: BOOMING REUNION
Holding her breath, the girl creeps though the darkness with her footsteps mute.
She draws her small frame even smaller than usual, paying heed to the rustling of her clothes. Her
hand stays over her mouth, for if she fails to physically obstruct it, she'll let slip her wheezy
breathing.
She truly wishes that her heartbeat's incessant pounding could shush itself too.
The auburn-haired girl, Petra, walks through the finally-familiar mansion anxiously, as if lost in an
unfamiliar world.
In this instant, she is truly grateful for the fluffy carpeting over the floors. She found it laborious to
walk on, but it's thanks to it that she can walk without producing any noisy footsteps.
She pledges to herself that, should she get another chance to clean them, she'll put all her gratitude
and diligence into their washing.
Should she not allocate her attention into unrelated topics like laundry, her barely-moving legs will
come to a stop. Even now she was proceeding at the slow pace of a caterpillar, so what would
happen if she stopped completely? Just thinking it terrified her.
She presently loathed the length of this long, stretching, endless corridor.
Petra had been overjoyed when she was accepted to work in this large mansion.
Although near to the village, Petra considered this mansion an extremely faraway place. It wasn't a
problem of distance. It was a problem of social position.
The governor and lord of the mansion the Margrave would come to Arlam Village during his spare
time.
Although nobility, he assumed no pretentious airs, and he laughed off and forgave the impolite
remarks of children. Petra had never heard the villagers badmouth the Margrave except on the topic
of his dress.
And Petra had not particularly paid special focus on the Margrave either.
But she had always admired the size of his mansion.
Being from a small village and with two normal parents, Petra would never reach this place. While
she had talked about wanting to go to the Capital and make clothes when she grew up, that was
merely a dream she created that was appropriate to her standing. She knew from childhood how to
give up on reaching for things that she would never attain.
When Petra was unexpectedly given a chance to work at the mansion.
And to add to that, she would be with someone who saved her life and she felt some feelings
towards. Which fact delighted her more? Keep it secret, but the latter one just slightly wins out.
Regardless, her employment in this mansion was the start of a dreamlike life for Petra.
While the expansive hallways, abundant rooms, and extensive time spent on cleaning did dizzy her,
the hectic days brought joy to Petra's life.
This place of aspiration and dreams now chilled her to her core with how it terrified her.
96
Petra doesn't know what happened, or what was going on.
What she does know is that she had finished her work, as usual, and has just had dinner alone with
her senior maid, Frederica.
Petra stood on a stool was she cleaned the dishes, while Frederica collected the meal which had
been meant for Beatrice-sama. They had failed to get it to her.
Petra has never seen Beatrie even once. She did sometimes wonder whether she really existed, but
seeing that Frederica, Emilia, and Subaru seemed to know her, Petra went along with it without
saying anything.
The lords of the mansion, somewhere far away.
Ignoring the servants Petra and Frederica, two people remained in this mansion. One was the
unseen Beatrice, and the other was the girl called Rem.
Neither of them would eat meals, which somewhat dissatisfied Petra.
But Petra pitied the sleeping Rem, and she could not forget how carefully Subaru treated the girl.
Subaru's expression as he gazed at Rem's face was incredibly vivid, so emotional and anguished
that Petra hesitated to even feel jealous.
And so—
Petra: “...I gotta save Rem-san.”
This unwittingly-voiced verdict alone spurred Petra's actions.
After Frederica disposed of Beatrice's dinner and Petra cleared away the dishes, Frederica instructed
Petra to double-check the work itinerary for tomorrow alongside other things.
Petra truly wanted to help Frederica with the leftover work, but being still midway through her
physical development, Petra's body would not withstand the fatigue of late nights. That Frederica
acknowledge Petra's enthusiasm and then send her off to bed was the usual way of things.
But tonight, while on the way to her room, something irregular happened.
—All of the lights in the mansion turned off.
Surprised by the sudden darkness, Petra clung to nearby Frederica. Frederica took her tenderly in a
hold, and after speaking words upon reassuring words, held her breath.
Petra would never forget how the atmosphere froze.
She had experienced this heavy aura before. The anxiety coursing inside her led her to strengthen
her grip on Frederica, who quietly drew her hands away.
Frederica: “Petra. Be a good girl, listen to me. —Use the stairway behind us, and exit. Without
making any sound, silently, as fast as you are able, flee.”
Petra: “B-but what about you?”
Frederica: “I'll follow soon behind. Once you have exited the mansion, run to the village. After we
safely reconvene, we will wait until morning to tidy everything up.”
97
Frederica faced forward as she spoke her gentle words.
She then pushed Petra lightly behind her, creating distance between herself and Frederica. The
misty air hid the moon back then, providing her with absolutely zero sources of light.
Petra sensed Frederica stepping silently forward.
Simultaneously, Petra obeyed Frederica's instructions and set out down the corridor, her path
opposite to Frederica's. She managed to reach the stairway, and just when she thought to proceed
down, remembered.
Petra: “This is... just like the forest.”
She remembered where she had experienced this heavy, freezing atmosphere before.
This was the aura from two months ago, when she and the other village children had entered the
forest.
The aura she had felt when in the middle of a forest full of bloodthirsty witchbeasts, with her life in
peril.
Petra: “—I gotta.”
The instant she realised that, Petra's feet proceeded not downstairs, but up.
She remembered Frederica's instructions. She did feel guilty for violating them.
But she could not leave Rem in a mansion identical to that forest.
Because she remembered how Subaru had brought her out of those terrifying woods back then.
Petra: “—ah,”
After thinking back on those scary memories, Petra senses that she is near her destination.
Make no sound. Go unnoticed. By stubbornly adhering to those rules, her sluggish journey reaches
the end of its path.
Just reaching Rem's room did not make small Petra capable of carrying and fleeing with her.
Petra had been so overwhelmed by urgency that she had not even considered that fact. She merely
though that, should she reach Rem's sleeping room and confirm that she was there, everything
would work out.
A sense of duty unfitting to her small stature, and the terror of knowing that death was near,
harangued her.
Nobody could fault Petra for failing to notice the obvious.
Just a few more steps, a few more meters, two rooms away, and there it would be.
Almost no distance at all left to reach her destination.
Her hear pounds so loud it could explode, the noise of her breathing slipping out between her
fingers.
Just a little further, just a little more, just a—
—Reaching the room, Petra looks up.
98
And that's when it happens. When, outside the hallway window, wind blows aside the clouds that
block the moon.
Moonlight beams in through the window, bringing colour to a once-dark world.
And Petra sees it.
???: “My, what an adorable maid.”
A woman so dark as to meld into the shadows stands directly in front of her.
Between Petra and the door, just three steps away.
She is a tall woman, with long hair.
Her sensual clothes display her voluptuous body gregariously. Her hand gives her braid a flick as
she calmly approaches, all exceptionally erotic.
Provided that you fail to notice the large, gleaming knife in her free hand.
Woman: “From what I'm told, I have two targets with one more appended. You're the little maid,
aren't you?”
Petra: “...au,”
Woman: “You're shivering? Don't worry. —Your guts are bound to be pretty. Girls with futures
always have beautiful entrails.”
Petra has no idea what she is saying.
But she does know that her advance is synonymous with the approach of death.
Petra knows this, but her feet freeze in too much terror to move.
The slender woman holds an unfittingly large knife.
Once that thing strikes her, Petra's life will be messily reaped.
And yet,
Woman: “Good girl. ...I'll send you to meet the angels.”
Heartlessly, the woman raises her knife, the shivering girl as her target.
The blade slices through wind, cutting into Petra's belly—soon.
???: “PETRA!!”
A large silhouette swoops in from the other end of the corridor, cutting into the space between Petra
and the knife, sparks flying alongside shrill metallic noise.
Petra's protector, their long blonde hair fluttering, is a very familiar character to her.
There is only one person with a back so large and dependable that it does not seem that of a woman.
Petra: “Big Sis Frederica!”
Frederica: “You naughty girl, Petra. I told you to flee... you are going to get a scolding after this.”
Petra: “Y-yes m'aam!”
99
Says Frederica in a stern tone as she glances back at Petra.
Petra trembles at the words naughty girl, nodding several times at Frederica's back in tears.
Woman: “You're the big maid? Big did indeed mean big.”
With the two having their exchange in front of her, the knife-wielding woman retreats a short way
and tilts her head. The way her braid sways with the movement doesn't match with the woman's
strangeness, seeming somewhat comical.
Frederica: “My large size does bother me, you realise. Likely from my father.”
Woman: “Then your father was big. And when you're that big, you're bound to have superb guts.
I'm excited.”
Frederica: “Your hobbies cannot be called tasteful.”
Woman: “Women's guts are brighter and more vivid than men's. I'll do a comparison with yours,
and teach you that.”
Frederica jabs her arms out in front of her as she takes combat stance.
Her hands come adorned with clawed cestus, which are likely the weapon which parried the
woman's strike.
They make use of Frederica's large, powerful build, so you could call it a weapon suited for her,
but...
Frederica: “Frustratingly, this is not going to prove an adequate match.”
Woman: “You do look like you have some ability to you, but probably, not as much as me. After an
experience in the Capital where I practically died, my skills have gotten better.”
Frederica: “I see. I find myself rather wishing to curse whoever failed to terminate you.”
Cold sweat rises on Frederica's brow.
The overwhelming grisliness radiating from this woman makes Frederica feel the strength disparity
with just a glance. She looks like she is merely standing there, doing nothing, and yet a thick aura of
death exudes from her.
How many lives did she reap to radiate this ghastliness?
Frederica: “Petra. This time, truly do leave the mansion. I shall stall her.”
Petra: “B-But, Big Sis...”
Petra glances at the door to the room beside them.
With that, Frederica comprehends why Petra disobeyed her orders and came here.
And so,
Frederica: “I would not know who has commissioned you... but it would appear that Petra and I are
listed as targets.”
100
Woman: “Yes, you are. You, the little maid, and the spirit girl. I'm not exactly satisfied with the
numbers, but I've never opened a spirit's stomach before, so I'm excited for it. I was just a step
behind last time and didn't manage to do it.”
Frederica: “You certainly divulged that information smoothly. Does this not disqualify you as a
professional?”
Woman: “I don't mind it. Your mouth's going to stop working soon, and if you're thinking to
complain to my employer, then I just have to keep you quiet.”
Frederica: “How deranged.”
This conversation could give someone a headache.
Frederica senses that speaking with the woman any further will be pointless. Regardless, she had
managed to get the answers that she wished to hear.
Frederica: “Petra. She is targeting yourself, myself, and Beatrice-sama. Do you understand?”
Petra: “—Yes, m'aam.”
Petra nods as she wipes away her tears.
With that last exchange, and this statement, Petra supposes Frederica's intentions.
She's a smart girl. A good student. Someone Frederica doesn't want to die.
Frederica: “Leave!”
Petra: “Yes m'aam!”
Petra practically trips over herself as she breaks into a run.
Immediately, the black-garbed woman throws something at her. Four knives, slicing through wind
as they loom in on Petra's back. Their superb aim is brilliantly disgusting, and a snap of Frederica's
cestus barely manages to deflect them.
Shrill metallic noise peals out as all the thrown knives rebound, thrown off course.
Petra does not even look back as she flees. She trusts Frederica entirely. And she has to answer to
her demands.
Woman: “She's a good girl.”
Frederica: “Yes, she's my pride!”
Frederica swings her left cestus at the woman, who dodges by tilting forward slightly. However,
then targeting the stooped woman's stomach, Frederica unleashes a kick.
Frederica's kick drills through the air, capable of destroying walls. Unlike her normal human mother,
Frederica's father was a half-blood from a lineage of fighting creatures. While she did not entirely
approve of the blood coursing through her veins, she was thankful for its strength this time.
The kick slams into the woman, her eyes wide. She immediate brings her free hand up to block, but
101
the kick will be more than powerful enough to snap those skinny arms of hers and—
Frederica: “Wh!?”
Woman: “Does this truly surprise you?”
Frederica swallows her breath. The woman's scarlet lips relax into a smile, everything upside down.
The moment that her hand touched Frederica's leg, in a situation which would not forgive even the
slightest error in force, the woman pulled off some nigh impossible acrobatics. She leaned her body
weight into Frederica's kick and pulled herself into a one-handed handstand. Frederica shivers at the
feather-light woman perched on her leg.
Frederica: “Spider!”
Woman: “Someone else called me the exact same thing not too long ago.”
Her voice sounds somewhat stung, but no such sentiment reflects in her ferocious strike.
Moonlight glints off her blade as it sweeps for Frederica's neck. Frederica immediately draws up her
cestus to parry it, but both this arm, and the other which was supposed to aid in the deflection,
scream in pain.
Although one-handed, and with arms far skinnier than Frederica's, the woman's grip strength is
immense.
Sparks fly as the blades shriek against each other and Frederica lowers the leg that the woman is
perched on, then aiming for her face and—
Woman: “Poor choice.”
The knife remains caught in the cestus's claws—as the woman uses this as a pivot point to flip even
further overhead.
The trajectory of Frederica's kick was supposed to have caught her as she fell, but instead passes
harmlessly beneath her as the woman's free hand reaches for her leg. Out from beneath her skirt,
there peeks yet another foreboding knife.
Woman: “Show me your vibrant insides.”
Still upside down, the woman's two knives fly in from both sides, force enough to slice Frederica in
two.
※ ※ ※ ※ ※ ※ ※ ※ ※ ※ ※
Soaring down the staircase, Petra gives great swings of her little arms as she runs.
She hears the shrill peals of metal and metal from upstairs, and Frederica's quiet scream.
Petra was not foolish enough to stay fixated on stubborn, childish ideas that would keep her from
listening to Frederica, fighting so that she could flee.
But even Petra, who knows absolutely nothing about fighting, does know this.
102
That shadowy woman is a horrifying monster.
Frederica's face had looked so scary, but the woman's smile hadn't faltered for even a moment. Petra
was not unaware of the strength gap. In fact she was incredibly aware of it.
Leaving Frederica behind like this means that she will be murdered.
Petra: “But if, Beatrice-sama was here...!”
The is one last person present in this mansion.
It seems like the shadowy woman is unaware of Rem's presence. Naturally, Petra does figure that
the woman will add Rem to her list of targets if she does find her, but so long as she and Frederica
refrain from announcing the fact that Rem is here, it's unlikely that the woman will notice her.
Petra: “This one... not it, then this one!?”
Having descended the staircase, Petra opens a random nearby door and checks inside.
It's unbelievable, but apparently Beatrice lives inside a moving room in this mansion. Should you
open many of the mansion's doors, eventually one will lead to Beatrice's room. That's how powerful
of a magician she was.
Petra needs that magician's help right now.
If this person is present here, then she will surely help Frederica. She'll do away with that shadowy
woman, and protect Petra's dream mansion.
Petra: “Not here... not here either... big sis!”
Out of breath and eyes flowing with tears, Petra is near to collapse.
She has opened all of the nearby doors in the servant's quarters. But Beatrice has not appeared. How
long has it been since Frederica started fighting that woman?
Petra needs to hurry, really needs to hurry, and yet.
Petra: “Big, sis...”
She needs to run. But her legs won't move.
Petra claps her hand against her leg in an attempt to invigorate her withering heart. But it isn't
enough. She can't be brave. And her hopes are seconds from waning dead also.
Petra: “—Subaru,”
With weakness dominating her heart, the name she calls in desperation belongs to someone who is
not here.
It's the name of who Petra thinks is the bravest person in the world.
He is amazing and courageous, overpowering his shaking legs as he faces opponents he cannot
possibly defeat.
When Petra and the other villages were in real danger, and she almost died, he was their saviour—
and his name is the one she calls.
Even though she knows that he isn't here.
Petra: “Subaru, Subaru... help me, Subaru,”
103
???: “Alright, will do, Petra.”
Petra: “—wha”
Crying and with her face buried in her hands, the voice leads Petra to look up.
Tears blur her vision. Somebody is standing right in front of her.
They kneel down to match the cowering Petra's eye level, and,
???: “My bad for being late. But here I am to help you. ...Thank god you're safe, Petra.”
His familiar face with its nasty eyes gives her an awkward smile.
His expression as he tries his best to comfort Petra isn't tender in the slightest, which brings Petra
absolute relief.
Petra: “Are you... Subaru? You're here?”
Subaru: “It's me, and I'm here. Everything's okay now.”
He gives a nod to comfort her. Petra reaches out to him.
She pats at his cheeks, and when she leans forward too far and falls, he catches her.
It's no hallucination and no dream, he is here. He is here for her.
She would love to bask in the relief it brings her. —But this is not the time for that.
Petra: “Subaru... Big Sis Frederica's fighting with a lady upstairs.”
Subaru: “Frederica is?”
Petra: “She's dark, with a big knife... and really scary.”
Subaru: “A dark horrifying lady with a huge knife... yeah, I know her.”
Subaru grimaces.
It seems like they both understand how threatening she is. Petra tugs Subaru's arm.
Petra: “Please, save Big Sis Frederica! Beat that lady, Subaru!”
Subaru: “Okay, just leave everything to me! ...Is what I wanna say, but if I face off against someone
who Frederica can't beat, I'm gonna be a corpse in under a second!”
Petra: “—”
For an instant, Petra's heart threatens to flood with despair.
But Subaru's palm comes down to stroke Petra's head gently.
Subaru: “And so I sent in some crazy strong reinforcements instead.”
Subaru looks up as if staring at the floor above, apparently imagining the scene unfolding there. His
104
expression is somewhere between relaxed and anxious, an undefined thing.
Subaru: “Have a nuisance being an incredible nuisance for the reunion, though.”
※ ※ ※ ※ ※ ※ ※ ※ ※ ※ ※
Frederica is seconds from accepting as fact: I am going to be sliced in two through the stomach.
???: “Sorry fer this... but you ain't invited.”
Metal clashes against metal alongside a voice which sounds pleasantly displeased.
It's a contradiction, but true.
They sound excited, but also sound disgusted by their opponent.
Which is really to be expected.
Woman: “You...”
???: “Yer gonna be sittin' there downside up for fuckin' ever, eh!? —Get th'hell off!”
Her blades blocked and attack ineffectual, up slams a ferocious kick into the woman's chest. Her
body curves into a C as she blasts away, and the man lowers his raised leg while he clatters his arms
against each other.
Both his arms are equipped with silver, gleaming shields.
One one-handed shield for each arm, both covering his fists.
Man: “Accordin' t'th'Captain, they say THE BEST DEFENCE IS A GOOD OFFENCE.”
Sharp fangs bared, the man's teeth click as he speaks.
Man: “So there ya go. Got defensive shields set up t'go on offence. ...'S best offence and best
defence happenin' at th'same time, so with two bests ain't it th'strongest?”
It's dumb, child-tier logic.
But this man is applying his child-tier idea, and using two shields as weapons.
The blond man takes a stance with his feet positioned far apart, glaring attentively at the opponent
as he cranes his head back at Frederica.
Man: “Ain't I right, sis—whatth'frickin'hell yer huge!?”
Instantly, the warrior's atmosphere about him dissolves.
The man's—no—the boy's eyes shoot open in shock as he gazes Frederica top to bottom.
Boy: “Wh—yer serious!? That's my sis!? Ain't my sis meant't be smaller, skinner, with a softer
lookin' face!? This ain't my sis, 's more like my bro.. agahh!?”
105
Frederica: “Do not be impolite.”
Frederica jabs her knee into the rude, staring boy's side.
The boy tumbles to the ground before sluggishly getting back up. Looking at his dizzied face,
Frederica notices it. The scar on his forehead.
Frederica: “Is that you, Garf?”
Garfiel: “Nevermind that, 'm I really safe t'be callin' yer Frederica... can't frickin' believe it... gahk!”
Frederica: “Do not neglect to appropriately refer to me as your elder sister.”
Halfway though standing up again, an elbow to the back sends Garfiel back into agony.
Looking at him in pain like this makes Frederica remember when they were young: they had no
toys in SANCTUARY, and had use their bodies to stave away boredom.
Frederica had just flung Garfiel away with complete disregard for their nine-year age gap. Exactly
the same as back then.
Frederica: “No. Garf... you have truly grown large.”
Garfiel: “'S just sounds like sarcasm when yer sayin' it, oi! N' just so you know, my amazin' self's
still gonna be gettin' bigger! Don't think yer gonna be lookin' down't th'topp'er my head forever!”
Frederica: “Huhuhu, allow me to amend that. Your body may have grown larger, but you remain as
small as always.”
Garfiel: “Th'hell was that!?”
Garfiel bares his teeth as he objects to Frederica's statement. This interaction with her little brother,
the first time in ten years, fills Frederica with an unbelievable happiness.
Who would have thought that the day would come where she spoke with Garfiel outside
SANCTUARY.
—Someone who ventured to SANCTUARY surely did well.
Ram, or Emilia, or Subaru? Which of them was it?
Frederica: “Ah, Otto-sama was also with you.”
Garfiel: “Ha, that guy flat never gets his payoff. Think about A MIGURD-MADE BRIDGE COLLAPSES
ON THE USUAL and eh guess h's just that kind'a guy.”
Up arises the vision of a dejecting-looking grey-haired man.
While the siblings both reach this conclusion, from deep in the dark hallway there comes,
???: “Do you mind if I begin to act now?”
Garfiel: “Yer bothered waitin' fer us, pretty consid'rate of yer. 'F yer gonna be so nice then how
about forgettin' yer work n' goin' damn home. My amazin' self ain't lookin' t'punch women around.”
106
Woman: “Goodness, how kind of you.”
Garfiel gestures as if swatting away a bug. The woman smiles.
Frederica taps Garfiel's back, for he is overwhelmingly lax.
Frederica: “Garf. You are going to have a painful time should you judge her by her womanly
appearance.”
Garfiel: “Yeh I got it, she ain't anythin' normal. N'anyway y'better bet th'only lady n'the world who's
gettin' my real lady treatment is Ram.”
Frederica: “If you believe that sounded cool, I will tell you that it was not cool in the slightest. Ram
would snort at you.”
Garfiel: “Th'fuck!?”
Frederica looks astonished. Garfiel glances back at her, indignant.
—That instant, a silver disk comes shooting from the woman's hand.
A disc. Or no, it wasn't a disc, it's a knife rotating at insane speeds on the vertical. The thing
whistles through the air too fast to see and it looms in on Garfiel, ready to split his head open and
splatter fresh blood about the corridor.
Garfiel: “Y'know,”
Woman: “—”
The metal shields clatter together as a searing shower of sparks bursts out.
The thrown knife slices the face of the raised right shield, before a deft shift in the thing's angle
sends the knife flying up to pierce the ceiling. Garfiel goes without watching this, instead racing
forward, gliding over the floor on approach to the woman as he raises his other shield.
Garfiel: “I did tell yer t'get th'hell out'v here, yeh?”
Woman: “I heard, and here's my response.”
Just before his fist can strike, the woman flits backward and yanks in her arm.
Immediately, the knife behind Garfiel rips out of the ceiling, rotating again with its momentum as it
attacks him from behind.
A string is tied around the knife's handle, connected to the woman's other knife.
Frederica: “Garf!”
She is too slow to warn him.
The blade rotates as it closes in on Garfiel's arm, hoisted and seconds from slamming into the
woman, ready to slice the appendage in two. But,
Garfiel: “—Fuckin' cheek!!”
107
Frederica: “—!?”
The instant that Frederica reaches him, or perhaps does not reach him, Garfiel shouts.
His arm explodes in girth. Golden fur coats it, the thing thick as a log, clearly not the limb of any
human but instead that of an animal.
Even the woman has to look rattled.
With a roar, Garfiel slams his fist and the shield into the woman's stomach.
Of course, having paid not a speck of care to dodging, the knife protrudes from Garfiel's arm. But it
has failed to cut through the thick limb and its coat of wiry fur entirely.
Woman: “—Gauh!?”
Garfiel: “Get outta here, woman!!”
Entirely bothered by the pain, the swing of Garfiel's fist blasts the woman away. Unable to kill the
momentum, she slams into the ground, proceeding to bounce and roll further across the floor. Garfiel
watches her tumble as he yanks the knife out of his shoulder. His fangs sever the connecting string
and he tosses the knife out a nearby window.
Garfiel: “Ha! KRUGAN SLAYS THE ENEMY EVEN MINUS HIS ARMS! 'F yer think m'gonna freak out'n
cower at some pain, yer dead wrong, moron!”
Frederica: “The one being a moron is you!”
Garfiel: “Dgha!?”
Garfiel boasts, when his sister's fist strikes the back of his head.
Garfiel falls into a squat, glancing back in protest to the unforeseen chastisement.
Frederica: “Fighting in a manner which injures yourself... Grandmother would cry if she saw this.”
Garfiel: “Aeuh, guh... a-ain't like I don't know what th'granny'd think'v it...”
Frederica: “Is that how you are referring to Grandmother!? I do not recall raising you to be like
this!”
Garfiel: “We ain't seen each other since I was four n' finally when we get our reunion yer doin' this,
yer th' one who's bein' unbelievable here!”
Garfiel breathing jars. Frederica also glances forward, to find a black silhouette languidly getting
up.
The woman quietly uprights herself and flips the knife around in her hand before catching the blood
dripping from her mouth on her finger, and licking it. A lovely smile arises on her face.
Woman: “—Wonderful, you are. Very wonderful. A lively boy.”
Garfiel: “Honestly, my amazin' self wasn't thinkin' yer'd get right back after that one either. My bad,
underestimated ya a lil'.”
108
Garfiel presses his hands together as he apologizes.
The exchange doesn't exactly seem like one between two monsters trying to kill each other, but it
does lead Frederica to forget the passing of time for a moment.
She shakes her head, getting herself back together.
Frederica: “Garf! This woman is shrouded in mystery. Take care not to slacken your guard...”
Garfiel: “'M sayin' I got that. But anyway. Sist... sis, d'you know a girl called Rem?”
Frederica: “...? Yes, she is in this mansion. I, erm, heard that she is Ram's younger sister.”
Frederica isn't irrevocably certain about this point either.
Frederica has known Ram since childhood, and those memory include no younger sisters of hers.
But Subaru explained that Rem was Ram's younger sister, and she resembled her to a shocking
degree. Apparently she was suffering from a Witch Cult affliction which erased her from everyone's
memories.
Garfiel: “She look like Ram?”
Frederica: “Exactly like Ram. But that is no pardon for you to use her as a replacement.”
Garfiel: “I ain't gonna do anythin' scummy like that. Jus'lookin' t'check. —Seriously, then.”
During their conversation, the woman rolls her shoulders and rotates her legs, checking her physical
condition.
Perhaps she's giving them time to have their conversation. Her thoughts aren't exactly clear.
Either way,
Garfiel: “Sis, 'f she's somewhere on this floor, find an openin'n bring her out. My amazin' hands're
gonna be full dealin' with her.”
Frederica: “W-what are you saying? I will be fighting as well. With us together, our chances...”
Woman: “I truly wonder about that.”
Frederica looks at the woman, gaze sharp, when the woman conceals her smile beneath her knife.
Woman: “Please don't make such scary expressions. And I believe that your baby brother will prove
that I'm not wrong in my statements.”
Frederica: “...Garf?”
Frederica's brows furrow in confusion.
Garfiel adjusts the angle of his shields.
Garfiel: “Sorry, sis. This ain't someone easy enough that I can keep worryin' 'bout what's goin' on
behind me.”
Frederica: “Wha!”
109
You'll hold me back, is the judgement passed on speechless Frederica.
While she did recognize that her own abilities did not even touch that of the woman, it's still
insulting to hear that you are so useless that you will be a detriment.
Garfiel: “Don't go misunderstandin' me, sis. I ain't sayin' yer a detriment.”
Frederica: “...Then what are you saying?”
Garfiel: “'F me n' this chick get serious, this place's gonna turn into a warzone.”
Garfiel points at himself, then to the woman. She smiles happily, as if affirming his words. She
fiddles with her braid before stooping down forward.
Woman: “Exactly. ...And so it would be best that you stand down.”
Battle—a sense which only the truly strong can comprehend.
Recognizing that she is far outclassed, a frustration blazes inside Frederica.
She has reunited with her brother after ten years, and she cannot even assist him at all.
Garfiel: “Stop thinkin' bout pointless crap, sis.”
Frederica: “Garf...”
Garfiel: “Look't my arms. These shields're th'ones me and you played with when we were little. The
strength I have now started with me n' you.”
Frederica's eyes widen.
Concern, care, and something other than those emotions comes through in his voice. Frederica feels
that her younger brother has matured, her heart growing hot.
Garfiel: “Th'Captain still handed my ass t'me with th'power'v numbers. But bein' 'n top shape starts
changin' that story too.”
Stepping forward, Garfiel clicks his teeth, batters his shields.
Garfiel: “Come at me, woman. This's my celebration fer leavin' SANCTUARY. N' I'm startin' it by
annihilating th'first obstacle in my way!!”
110
CHAPTER 123A: GUTHUNTER VS THE SHIELD OF SANCTUARY
Subaru: “Got it? In total there are four people in the mansion we have to save. They're all girls.”
Inside the carriage, Subaru raises four fingers as he explains.
The scenery flows by as they speed along the rugged road. But even so no wind or jolting assaults
their carriage. While vaguely finding it a mystifying sensation no matter how many times he
experiences, Subaru nods to the two people looking at his raised fingers.
Subaru: “First is Frederica. Our buddy Garfiel's older sister. Saying the attacker's already there,
Frederica's the only one who could buy us any time.”
Garfiel: “Sis, hrn... Ain't seen her for ten years now.”
Looking uneasy, Garfiel scratches at his short, blond hair.
Garfiel had been so stubborn about staying in SANCTUARY. It's going to be hard for him to face
Frederica, who had abandoned SANCTUARY for the outside world.
Otto: “You truly have not seen her in a decade? From the Margrave and Ram-san's accounts, it
sounds as though they travelled between the mansion and SANCTUARY rather frequently.”
Garfiel: “It wouldd'er been awkward fer sis too. She never came along with that asshole Roswaal...
sh'did send a bunch of letters though, apparently.”
Otto: “Apparently?”
Garfiel: “Gave them all t'granny without reading them.”
Garfiel averts his gaze, looking sulky. His awkward attitude toward his sister is exactly that of a
child. Their reunion is definitely going to be an emotional one.
Subaru sighs. Otto's impression of all this looks to be about the same as his as he pulls the reins.
Otto: “Then the second would be Petra-chan.”
Subaru: “Yeah. Roswaal Mansion's precocious and hopeful new maid Petra's the second. She's a
completely ordinary village girl with no underside at all, so if she gets targeted it's 100% Bad.”
The attacks on Roswaal Mansion so far have ended in dead Petras 100% of the time.
The other three are also highly likely to die, but Petra has no means to fight back at all. So it's
common that she gets dealt with quickly.
If they're going to protect her, they will need to find her immediately.
Subaru: “Next is Rem. She's Ram's younger sister. Though you probably don't remember her.”
Garfiel: “M' still n' disbelief 'bout it, Captain. 'S just the idea of Ram havin' an identical twin sister.
How th'hell could I forget that, when my amazin' self's known her such a long time?”
Subaru: “It's a CURSE where even Ram's forgotten her. Talking about ways to deal with that's gonna
be a change in topic, but... anyway, Rem's not so urgent. The assassin attacking the mansion, Elsa,
doesn't have Rem on her list of targets. I don't think her employer knew about Rem's existence
111
when they hired her.”
Otto: “Although, should she discover Rem-san sleeping in the mansion, I doubt the encounter will
end peacefully.”
Subaru: “...You're right about that.”
We're talking about Elsa here.
Rem might not be on her commissioner’s list, but if she discovers her, she'll probably do something
just for kicks. And while Subaru hasn't seen it himself, Rem has been killed during these loops.
All he can do is pray that Rem is not in a room that Elsa just happens to open.
Otto: “Regardless, this dependence on the opponent's decisions can't be called an overly great
strategy.”
Subaru: “Where I'm depending on you guys, and also depending on the enemy. This is Natsuki
Subaru's brand of warfare, dubbed REVERSE FURINKAZAN.”
Garfiel: “S-so cool...!”
Garfiel clenches his fists, eyes sparkling.
That his random bullshit statement has given Garfiel such expectations makes even Subaru feel
guilty. He decides that later, when they have real time for it, he will teach Garfiel about actual
furinkazan.
He furrows his brows as he looks at Garfiel.
Subaru: “Though...”
Subaru: “I mean it's been horrifying watching this, but is this actually seriously working?”
Garfiel: “Well we're in a rush, ain't we? 'F there were any better way, my amazin' self'd go for that
instead.”
Says Garfiel, looking displeased.
His words are sensible ones, but Subaru's statement is truly inevitable. For Garfiel is presently
outside the carriage, holding on to the thing, while talking with Subaru and Otto through the
window.
His hands clutch the windowframe as he dangles there, hanging alongside the zooming carriage
with his feet brushing across the ground, getting dragged along by the vehicle.
Subaru has seen an enemy get mashed in a carriage's wheels before, and being that this could easily
be a repeat if Garfiel's hands slip, he can't watch on very peacefully.
Subaru: “If something goes wrong and you get smushed, it's no holds barred on my PTSD and we
also stop having anything we can do about the mansion.”
Garfiel: “Th'hell, Captain. Bein' a damn worrywart. Everythin's all fine. Just watch this!
N'thisn'thisn'this! N'this n'this!”
Subaru: “Stop!! I'm gonna die!! I'm gonna die before you do!!”
112
With the windowframe as the pivot, Garfiel starts spinning round and round using just his arm
strength. Between the WINDBREAKER BLESSING and Garfiel's inhuman grip these acrobatics are
possible. And his hold on the frame is so strong that the thing warps and creaks. Subaru can imagine
the pending despair of the carriage's owner which is to say Otto.
Otto: “His EARTHSOUL BLESSING doesn't come into effect unless his feet are touching the ground.
Since we need Garfiel to be in top form, or something close to it once we reach the mansion, we can
only rationalize this as a necessary measure.”
Subaru: “I mean I get the logic. You know, from an outside perspective this looks like us speeding
as fast as we can to shake off some guy trying to get in the carriage. When what's actually
happening is we threw a fourteen year old out of the carriage to drag him along the ground while
zooming at top speed.”
Otto: “You do realise how preposterous both those perspectives sound when you use that
phrasing!?”
Otto, handling the reins, probably wants to avoid giving that first impression. But the two dragons
tirelessly pulling the carriage, Patrasche and Frufoo, pay little heed to the coachman's intentions and
just run ceaselessly.
This is all more or less why Garfiel is using this mock-acrobatic means of locomotion.
Emilia's magic did heal his serious wounds back in SANCTUARY, but that did not replenish his lost
blood or mana.
The travel distance between SANCTUARY and the mansion is about half a day's worth. Even if they
have the dragons sprinting well, how much time can Subaru and the others really spend on
recuperating?
Nothing has changed about Garfiel, with his EARTHSOUL BLESSING amassing power from the
ground, being their ace. Subaru and Otto are only there to arrange a setting where he can fight at his
best.
Garfiel: “But anyway, y'stopped talkin' halfway, Captain.”
Subaru: “Huh?”
Garfiel: “Th'thing we were talkin' bout. We gotta save four people, n'we only got three. I ain't heard
'bout this last person. Who's she off bein'?”
Pulling himself up, Garfiel peeks into the carriage. He gives Otto a questioning gaze as well, but
Otto just shakes his head and shrugs.
Otto: “I'm afraid that I haven't encountered this final person either. I was in the mansion for
approximately a week... but I never even saw her in passing.”
Garfiel: “You ain't even seen her face n' she hates yer so much she don't wanna see you, yer gonna
be okay, guy?”
Otto: “I would like to think that that is not the reason I've failed to see her!”
113
Otto frantically voices his objection while Garfiel watches on with pity.
Subaru strikes his fist against the seat and sighs.
Subaru: “The last one... Beatrice, probably, won't come out unless it's me.”
Otto and Garfiel shut their mouths as they look at Subaru.
The seriousness in his voice probably meant they believe him, even without asking why. Truly
reassuring companions.
Subaru: “I'm taking Beatrice out of there. Dragging her out of there. I need to do it.”
Nobody else. Subaru has to be the one.
Even if Beatrice puts on a show, acting like she doesn't want it.
Garfiel: “'F that's what yer say then that's what it is, Captain.”
Otto: “If possible, I think we should evacuate the nearby villagers in Arlam as well. It will avoid
some chaos. How about I do it?”
The two each show their support for Subaru's decision.
Subaru has his role. And they have theirs.
Truly, entirely, dependable people.
Subaru: “Thank you, idiots.”
Otto: “He's incapable of giving an honest thanks, the idiot!”
※ ※ ※ ※ ※ ※ ※ ※ ※ ※ ※
The battle escalated entirely, spreading destruction across the luxurious mansion.
Steel clashes against steel, shrieking metal comes with showers of sparks, the blows and slashes
destroying the mundane life of the moonlit Roswaal Mansion.
The windowpane shatters and the shards of glass scatter. Damage to the floor sends the carpet
flying, while paintings hanging on the wall splinter to fragments.
Woman: “Wonderful. You're excellent.”
Garfiel: “It don't make me happy to hear that from anyone 'cept Ram!!”
Garfiel launches his shielded right arm, jabbing past the woman as she dodges aside, for the strike
to slam into the wall. He pursues her in her escape, using the momentum from his right arm to pivot
in the air and strike her backhanded with his left.
Woman: “Bad luck.”
114
Garfiel: “It ain't over yet!”
The woman dodges. But before she can swing her blade, Garfiel wrenches his body again to
dislodge his right arm from the wall, sending a strike hurtling for her. The woman aborts her
downward slash to raise her arm, using the kickback to flip backward through the air—the instant
that Garfiel's blow skirts past the woman's feet, the room ruptures.
Backhand blow to the left.
Punch to the right.
Sweep leg back and to the left.
Jab to the right.
Pivot and kick to the left.
Striking blow after blow as he spins, Garfiel offers no leniency in his pursuit of the woman. She has
no room to do anything except avoid Garfiel's assault, and sensing that her feet have reached the
end of the corridor, Garfiel raises his head.
Garfiel: “Yer done!!”
Stepping forward, Garfiel unleashes his fists.
The punches drill through the air, silver reflections of moonlight shooting through the dark corridor
in violent pursuit of the woman.
These are the arms of a beast, so powerful that they will assuredly turn a human body into gore.
With her back to the wall, the woman flicks up her leg to place the sole of her right foot against the
wall also.
She determines her aim to counter the incoming punches, jabbing out her dagger so that Garfiel will
impale himself on its blade. Metal clashes against metal as the knife is caught between the shields.
However,
Garfiel: “Like that trick's gonna work!”
Her plan must've been to slip her dagger between the shields and stick Garfiel with her knife in his
charge. But Garfiel's muscles are not so weak that any woman's skinny arms will accomplish
anything.
With the kurkri's point still between the shields, Garfiel twists aside to snap the dagger apart.
But before he does—
Woman: “Then what if I add another trick?”
With her wall-set foot as the pivot, the woman flips upwards.
Instantly, the woman's foot strikes the handle of her trapped knife, opening a slight gap between the
shields.
And into that opening,
Woman: “Here's the real thing.”
Garfiel: “—!?”
Now entirely inverted, the woman holds yet another knife in her other, left hand. This is her third
omninous-looking kukri. Just how many is she hiding on her?
115
The thin knife easily slips into the gap between the dagger and shields.
The deadly blade does not even whistle through the air as it pressed forward, aiming to slice
Garfiel's neck. Even if he transforms this second, the strike will hit the most lethal of spots.
But Garfiel chooses a fiendish way to counter the blade.
Woman: “Incredible.”
Garfiel: “—yhher prhahise ain't ghonher mhake me happy!”
The woman whispers, enraptured. Garfiel spears his head forward.
His sharp fangs literally bite the woman's left blade to a stop. Blood drips from the shallow cuts at
the corners of mouth, and the knife's metallic stench pierces his nostrils.
Garfiel: “Fhuckin' stinks!!”
Putting force into his jaw, Garfiel snaps the knife to bits.
He spits out the shattered fragments as he swings his clawed foot up to strike the yet-inverted
woman from below. The force of the kick will burst her skull apart—to counter it, she sacrifices her
arm.
A wet cloth sounds to have slapped against the wall as pure scarlet splatters over the hallway.
Garfiel uses his sleeve to wipe the blood from his face, and gives a deep sigh out his nose as he
glances back.
Several meters away, having escaped the dead end, stands the woman. But with many bones broken
from her wrist to her shoulder, her left arm hangs crooked and twisted.
Garfiel: “Pretty fuckin' good t'get away by losin' only an arm. Crap, m'mouth hurts.”
Woman: “...Huhu, thank you. Ahh... it hurts. It truly does. I feel alive.”
Garfiel: “Eh? Ain't just cuttin' others, yer like getting' cut yerself too? Now that ain't somethin' my
amazin' self can understand. Not that I was thinkin' t'make understanding with yer at all.”
The woman drips blood as she smiles splendidly, bringing about visceral disgust in Garfiel. He
batters his shields together—and notices there, behind the woman,
Garfiel: “Hey, sis. Th'fuck're you still doin' over there? Like yer just saw, 's not feelin' like I can
show you me bein' cool th'whole time. Get off t'doin' what yer have t'be doin'.”
Frederica: “...I-indeed. I shall.”
Frederica had not actually been watching in silence, but had been petrified and unable to move.
That was how extra-dimensional the fight between Garfiel and the woman was.
If Frederica had gotten involved in this battle, she would swiftly withdraw after the first few blows.
These two are just that superior.
Frederica keeps her attention on the woman's back as she glances at her destination—Rem's
sleeping room. It's only a few meters away, and she is much closer to the room than the woman is,
but she cannot envision herself reaching its door before her.
116
If she could at least reach the room, she could shoulder Rem and escape out the inside window.
Woman: “You don't need to be so guarded, older sister.”
Frederica: “...Huh?”
Woman: “Right now, I am stricken with your little brother. It doesn't bother me what business you
have in whatever room, or what you're going to do there. None of my interest is devoted to that.”
Frederica: “—!”
The woman does not even glance back as she assures Frederica her safety.
She probably isn't lying. She doesn't seem like the kind of person to trick the enemy in this manner,
and she doesn't need to, either. Above all, anyone listening would hear the sincerity in her words.
Right now, all of her attention is devoted to Garfiel.
She truly could not give less of a care about Frederica.
But the woman emits an aura so dreadful that it could encapsulate the whole mansion. A pungent,
violent bloodlust, which make her initial foreboding air look like a child's joke.
Garfiel: “Sis.”
Frederica: “—I believe in you.”
Frederica swims through the corridor, drowning in the woman's ghastliness as it is, to reach her
destined room—
—After glancing at Garfiel one last time, Frederica slips into the room.
Witnessing this, Garfiel gives a deep sigh.
Garfiel: “Yer so unruffled that yer can overlook sis... ain't what's happenin' here.”
Woman: “Do I look like enough a cheater that I can stay unruffled when faced with such a
wonderful partner? Right now, I am only for you. —Ahh, I can't bear it.”
Both radiant allure and blood-iron horror coexist in this grisly woman. She smiles.
Bathed in her fiery, passionate gaze, Garfiel spreads his stance and stoops his body low.
Garfiel: “Honestly, 's just fuckin' gross. M'rippin' yer apart, manglin' yer t'shreds.”
Woman: “I promise to extract your guts without hurting them too.”
Her left arm still dangling, the woman's healthy right arm readies her knife.
She stoops down so low that her breasts could touch the floor,
Woman: “I am the GUTHUNTER, Elsa Granhiert.”
Garfiel: “...The Strongest of Shields, Garfiel Tinzel.”
117
The instant that the introductions are over, Elsa moves.
Elsa's smile phases into blank darkness as she sprints, so swift that she gives no impression of being
wounded. The instant that Garfiel hears the first footstep, out peals the noise of pounding against
the walls, again and again and again, from every direction.
Elsa kicks off the floor, off the walls, off the ceiling as she closes in on Garfiel. She moves so fast
that he cannot focus his aim, and moves like no creature he has seen before. Something approaching
with these nightmarish movements was no humanoid nor beast.
And the most surprising thing is, she's obviously faster now than she was before being wounded.
Garfiel: “Entertainin'!!”
Garfiel bares his fangs, laughs, and moves.
If the enemy is using tricky movements to approach, then Garfiel will counter by doing the same.
He puts his hands and feet to the floor. And off his rear foot, explodes.
Garfiel the human-sized bullet shoots down the mansion's corridor.
He positions his shields before him, his charge as ferocious as a tiger's with a shockwave that blasts
away the shattered window glass and fragments of wall.
He does not observe what comes of that, instead roaring as he spears his arm into the floor to force
himself to a stop. He immediately flips himself around and back into bestial posture, and again his
rear foot annihilates the floor.
The quake rocks the mansion, the carpets suffer in the destruction, flying about in tatters. Shreds of
red cloth catch on Garfiel as he soars—
Garfiel: “—!!”
Elsa: “Ahahahaha!!”
Elsa plummets down from the ceiling, swinging her blade, which strikes against the zooming
Garfiel's shield. The shockwave stabs through eardrums as destruction rocks the moonlit corridor.
Elsa laughs as she rebounds, making a breakneck flip sideways. The force of the slash has thrown
Garfiel's course, sending him plummeting head-first into the wall. He busts through the stonework
to land gracelessly in a guest room.
Plumes of white dust shadow the areas as Garfiel grabs the leg of the nearby bed. His biceps swell
as he easily lifts the 100-kilo bed and tosses it out the hole he just came through. Boom, bust, and
from beyond the bisected bed comes the black woman's thrown blade.
Garfiel parries it with his left shields and uses his right to slam the approaching Elsa in the face. But
she ducks, and the strike merely grazes her braid. The end of her black hair tickles the tip of
Garfiel's nose, when he then obeys the terror rushing up his spine and immediately zooms forward.
He barely manages to dodge the slash coming to slice up through his groin, his back instead taking
the hit as he blasts though the door. The battlezone relocates to the corridor.
Giving him no time to catch his breath, Elsa comes zooming in pursuit of Garfiel. Garfiel kicks at
her skinny waist. A hit, isn't what it feels like. Elsa contorts her body strangely to evade, and dodges
118
the shockwave from the kick by shifting so that it merely brushes her belly. Garfiel stands stuck
with his leg outstretched as the blade of Elsa's kukri butches the air, closing in.
This isn't like the attack she fired before, when cornered. If Garfiel tries to catch this in his mouth,
the speed and force of the thing will slice his head in two. Garfiel's decision is instantaneous as he
catches the sweeping blade on his right shield, allows its path to continue to his left shield, and then
away.
Shrieking metal. Showers of red and yellow sparks. Dark eyes opened in surprise, and the woman's
exposed belly. Garfiel roars as he slams his raised leg to the ground. He takes his stance and moves
to drive his fangs into Elsa's torso, intending to quite appropriately rip open her guts.
Garfiel: “—!”
That he aborts his lunge and uses the momentum to pull his head in instead can only be called
instinct.
Late to dodge, Garfiel's left ear goes flying off and he takes evasive action through the spray of
blood. He puts his foot to the wall, dodges the oncoming strike by shooting to the ceiling. Dodges,
dodges, dodges entirely.
Garfiel's outstretched arm rips through the ceiling, leading part of the upper floor to collapse. This
creates an opening in Elsa's pursuit, which Garfiel uses to escape. His hands and feet land on the
carpet, and Garfiel uses his palm to put pressure on the bleeding coming from his head and its
missing ear.
He takes a ragged breath. Grits his teeth at the burning pain. He sees Elsa cut through the thick
smoke, walking closer, and smiles.
Garfiel: “Y'fuck... 'm pretty sure I'm meant ter'v turned yer left arm useless.”
Elsa: “You're right. It hurt. But people's wounds do heal.”
Garfiel: “This's just goin' of my piddly knowledge, but when a mangled arm fuckin' heals we ain't
talkin' about humans any more.”
Or really, it's transcending the category of 'living creature'.
Garfiel may have his EARTHSOUL BLESSING, but he still needs several hours if he's going to make a
shattered arm operable again. When on mana-rich earth, and doing everything he can to slack off.
That she can heal during battle, and so quickly, is ridiculous.
Subaru had told him beforehand that she doesn't die even when you kill her, and now Garfiel's
initial speculation feels legitimate.
Garfiel: “Which makes things quick. Yer ain't a human. Dunno 'f yer were born one, but either way
yer at least stopped bein' one.”
Elsa: “You don't look it, but you're surprisingly clever.”
Garfiel: “I told yer it only makes me happy when it's Ram praisin' me. N' anyway I got n'idea 'bout
yer weird healin'.”
Jabbing out his finger, Garfiel states his speculation.
Despite everything and despite how surprising it may sound, Garfiel likes books. With nobody to
119
rival him in strength in the boring SANCTUARY, reading became an important time-killing activity
for him.
But that said, the books Garfiel likes are adventure novels, myths, folklore, things in that vein. His
interests unfortunately do not land on anything productive for procuring knowledge.
Garfiel: “N'th'books my amazin' self read, there were lots'er monsters, heroes, those kinda things
where yer don't know if they really existed. And there was one'v'm just like you.”
Elsa: “...I'd like it if you didn't equate me to a phantasm from a picture book.”
Garfiel: “It wasn't a picture book, was one'm full'a letters. ...Did have some pictures in it but
whatever that don't matter. And I can't say clearly it was a phantasm.”
Looking indifferent, Elsa listens to Garfiel.
This thing where she entertains conversations to the end really does jar with the ferocious
impression she gives while fighting.
Garfiel'll have that face of hers going pale.
Garfiel: “After all, yer th'same as one'v the old Witches.”
Elsa: “—”
The swaying motion of her dagger halts.
Elsa's dark eyes look nonchalantly at Garfiel. He jabs his finger at her,
Garfiel: “—Yer a goddamn VAMPIRE!”
Elsa: “Not that I drink blood or anything.”
With a sigh, Elsa kicks off the ground.
Her left arm has healed completely. She weilds kukri in both hands as she closes in on Garfiel. He
blocks she sweeping slash by raising his shields, simultaneously shooting his right leg out to kick
her—and Elsa launches her own kick along the exact same trajectory, the two of them crashing feetfirst
into each other and blasting away.
Garfiel: “Not fuckin' cool! Yer arm's seriously all back t'normal!?”
Elsa: “But didn't you heal your ear as well, while you were buying time? We're even.”
Garfiel mentally sticks his tongue out at her.
During their time talking, Garfiel used the hand plugging his wound to heal the injury with magic.
He hopes for the missing section of his ear to steadily come back, but if he suffers a wound equal to
what Elsa suffered, then Garfiel's healing magic will only amount to a quick and dirty stop-gap.
Garfiel: “Yer ain't denyin' it. So yer really are a vampire?”
Elsa: “People can call it whatever they want. I don't suck blood, and my meals are ordinary. When
I'm in the sunlight all that happens is that the guards get riled, so it's not really anything special.”
Garfiel: “So yer on about guts so much because yer a vampire?”
120
Elsa: “That's particular to me. I just like gazing at fresh guts and touching warm-looking intestines.”
Garfiel: “That's way fuckin' creepier.”
Elsa sheds and dumps her impeding black cloak.
Garfiel judges that Elsa's motivation has spiked even further and clicks his teeth. He batters his
shields together,
Garfiel: “S' a big world... bit've a drag, but yer better pull it off, Captain.”
With that, Garfiel roars as he swings his shields down at the oncoming Elsa.
※ ※ ※ ※ ※ ※ ※ ※ ※ ※ ※
—He opens the door, and what comes from the room is the scent of paper.
Perhaps the cloying the smell carries the weight of all the days and years spent closed inside this
space. Or perhaps if you consider the appellation A TIME-STOPPED ROOM, days have nothing to do
with it.
Subaru: Just got stuck with some time in Sanctuary to think about all that stuff. And your answer's
another thing I wanna hear.
Beatrice: “—How come?”
Without the librarian's permission, Subaru enters the Archive.
As always, the mood here is both melancholy and tranquil. There are no windows to let in sun, or
for ventilation. Staying here a long time is bound to worsen your mood and your health.
And especially so when the expression of the girl watching Subaru is so utterly exhausted.
Beatrice: “How come you managed to reach this room again, I suppose? I don't remember calling
you, in fact.”
Subaru: “Sorry, but showing up uninvited is just who I am. Impossible to forget that time back in
middle school where I showed up uninvited to a friend's birthday party and made the whole thing
awkward.”
Even dense Subaru decided to be more prudent after that one.
Though, since he announced “Well, that's all for today!” and left noisier than anyone else, he
stopped getting invited to anybody's birthday party.
Subaru: “It's miserable and my heart's about a second from popping so let's cancel that topic.”
Beatrice: “You're the one who brought it up, I suppose. You're like that about everything, doing
things always of your own accord, in fact.”
121
Subaru: “Yup, always of my accord. So no matter how much you hate it, I'm here.”
He sees the girl swallow her breath.
After respectfully bowing his head in a way that she can see it,
Subaru: “I'm taking you out of here, Beatrice. —I'm dragging you out into the sunshine, where we'll
play until your dress is caked utterly brown with mud.”
Beatrice sits as she always does, on the stepladder, cradling herself.
With the black tome cradled in her arms as always, her wavering eyes gaze at Subaru.
122
CHAPTER 123B: HAPPINESS REFLECTED ON THE WATER
—Taking a breath, she again challenges the tomb that she just exited.
Inside the stone tomb, isolated from moonbeams, only the pale glow of the walls provides any
source of light. It wasn't uncommon, in places where ambient mana thrived, that such natural
phenomena helped to preserve visibility.
However, it was unusual for this natural lighting to be inside a manmade structure. It had, most
likely, been reproduced by some inbuilt mechanism of the building.
A mechanism like a metia, functional so long as the required mana was stockpiled—sensing that the
lighting in the tomb follows this or similar logic, Emilia quietly takes a breather.
Inside this tomb, she feels the presence of the minor spirits distantly.
It's not that they're gone. Minor spirits are like ambient mana, existing everywhere. There's a
question of whether you can perceive their presence, or whether they they're strong enough for their
presence to be perceived, but they would be utterly absent nowhere.
This particular perception of them arose from the wall's light-producing mechanisms.
The tomb preserves a rather high rate of mana passage into and out of its space. The mana inside the
tomb is kept at a fixed volume, with mana quantities never exceeding or falling short of that
amount.
The degree of mana needed for preserving the wall-lights is so scant that the minor spirits cannot
manifest themselves sufficiently, and that's why their presence in this tomb feels faint. Even
assuming that minor spirits are present, they would be debilitated in this environment.
Emilia: “This place is sooo nasty for spiritualists.”
Reaching that conclusion, Emilia mutters to herself.
Perhaps overcoming the first TRIAL liberated her somewhat from her sense of being cornered.
Having finally gained enough composure to observe her surroundings, Emilia's impression of the
tomb is that.
It's not any great threat for a magician, who casts using the mana stored inside themselves. But if
they exhausted their stores they would have no means to replenish them, and a magician with few
gates would probably find the tomb a troublesome place too.
Though if we're talking Emilia or Roswaal, it would barely effect their combat capabilities.
Emilia: “Which is strange... since I can hardly sense anyone outside.”
Having regained her capabilities as a magician, Emilia's perception of mana has strengthened.
When she was outside the tomb, she felt the mana of so many entities that she couldn't restrain it.
She had probably picked up the mana of practically all creatures, or perhaps the presence of
practically all od, tugging at her perception. The wear on her mind was intense. She would need to
learn how to control it quickly.
But that behind-the-scenes battle is postponed while inside the tomb.
Instead she needs to wait for the TRIAL. Honestly she doesn't know which option's preferable.
123
Emilia: “Ram was pleading me. Have to keep focused.”
Emilia thinks of Ram, begging to Emilia with her head bowed.
Ram never showed such weakness, and there she was baring her emotions so intensely. How could
Emilia repay her for everything until now if not by answering to her plea?
Subaru, having returned to the mansion without observing Emilia's results, also had faith in her.
His actions expressed his unwavering conviction that Emilia could do it. She needed to answer to
Subaru's trust. Or actually, she needed to do even better than expected and surprise him.
Emilia: “I'm glad they believe in me, but that's not what this is about.”
Though they might've been in a rush, Emilia still has to object to the fact that they all left without
seeing her. She should be permitted to jolt them and sulk.
And especially in Subaru's case. The two of them needed to have a very, very serious conversation
after this.
Emilia: “Anyway, this feeling... the TRIAL's here.”
The moment she entered the tomb, Emilia felt it on her skin.
She had been somewhat unconvinced that exiting and entering the tomb would be enough for the
TRIAL to prepare itself, but the overwhelmingly cool air in the tomb keenly informs her of the truth.
There's no need to postpone it.
Inside the TRIAL room, the second TRIAL is awaiting Emilia.
Emilia: “I saw my past. Then, the next one is...?”
Her cheeks tense, nearly stiff, as she strokes her belly.
She uses the irregularity in her breathing to determine whether her nerves are steeled. They are,
acceptably so.
—The Trial Room waits unchanging as it welcomes Emilia.
It hasn't even been an hour since she left. Of course it hasn't changed.
Perhaps this room alone preserves a greater load of mana, for visibility is slightly better here than in
the hallway. The doorway in the back of the room stands shut and healthy as ever.
What awaits her there, once she has overcome the third TRIAL?
Just as she thinks that thought,
<—Witness the uncomeatable present.>
Emilia: “—hk”
She hears it.
Murmured at her ear, her own voice.
The instant she attempts to consider what 'uncomeatable present' could mean, her consciousness
124
fades to white.
The intense sensation tears Emilia's mind and soul from her body, dragging her into another world.
Unable to rebel, Emilia crumples leaning against the tomb's wall, before collapsing.
Her vision blurs. Her thoughts flee. Her consciousness drowns.
Emilia: “Subaru,”
Unsure of what her own lips said at the close, the TRIAL begins.
※ ※ ※ ※ ※ ※ ※ ※ ※ ※ ※
???: “Hey now, Lia. Where are you going off to, come over here.”
Stopped by that gentle voice, Emilia turns around.
A woman with short silver hair beckons her to the dining table. Her eyes are nasty. Her voice is
gentle. Either indicates Emilia's ideal for women.
Emilia: “Mother, Fortuna...”
Fortuna: “...? Are you still half-asleep? Then you stayed up late again. You're not a child any more,
you can't be giving others trouble like that.”
Fortuna approaches, her tone chiding as she pokes Emilia in the forehead.
Pressing down on the faint red mark on her forehead, Emilia widens her eyes.
Emilia: “Woah.”
A sound of astonishment slips out her lips before she can register it. That's how greatly the sight
strikes at Emilia's heart.
This is the first time Emilia has ever seen Fortuna sacrifice her ease of movement and wear an
apron. The over-adorned frilly white apron mismatches to Fortuna's personality, but suits well to her
beautiful appearance.
Emilia: “Mother, you're cute.”
Fortuna: “—. Where did that come from? You really are half-asleep.”
Her cheeks reddening slightly, Fortuna grasps Emilia's shoulders and turns her around. She gives
Emilia's back a push, and,
Fortuna: “Wash your face in the river. You'll stop saying weird things once the cold water's woken
you up. Though when it's you, Lia, that might not change even when you're properly awake.”
Emilia: “Wh-what are you saying, Mother? That's not what it is. I'm not half-asleep at all... and I
didn't say anything a trifle weird in the first place.”
Fortuna: “Where are you learning this archaic speech, a trifle? I'm sooo worried that everyone
125
might be teasing you and putting these things in your head. I'll have interrogate Arch later.”
Emilia pouts. But Fortuna merely nods back, not conceding an inch. While shocked that her own
opinions are not working, Emilia slumps her shoulders and starts walking her journey for the river.
???: “Goodness, hello there, Emilia. You're not looking the cheeriest.”
???: “Gosh, she really isn't. Which means Fortuna-sama told her off? She may've stayed up late.”
???: “Emilia's old enough now. I'm sure she wants her me time now and then.”
After exiting her house and embarking along the road to the river, the elves of the village address
her.
A group of older elves sit at a table surrounded by thick tree roots as they chat. She had heard they
were the same age as Fortuna, though everyone, including Fortuna, sees Emilia as young.
Emilia: “Good morning. You're all out early.”
Elf: “It's you who's late, Emilia. It's nice that you're helping your Father's work, but it's a waste of
your youth if you don't use some of your time for yourself.”
Elf: “Exactly, exactly. You're so cute, Emilia, you need to have fun while you're cute.”
Elf: “If I were as young and cute as you, Emilia, I'd be bicycling the village.”
Emilia tilts her head at the term 'bicycling the village' while the women all look at each other and
laugh, squealing. The details of their conversation are more or less beyond Emilia, but it's good that
everyone is having fun.
Finding herself feeling happy, Emilia relaxes as well.
Elf: “There, now that's much better than looking down. Smile, smile, let's see a smile.”
Emilia: “—Right.”
After pointing at the smiling Emilia, the women's fingers pull their cheeks into a grin.
Finding their argument as legitimate, Emilia identically makes a smile and nods.
Waving a goodbye to the women, Emilia resumes her course toward the river.
She scales the gnarled tree-roots, passes through gaps in verdant leaves. Hearing the burbling of a
brooklet, Emilia breaks into a jog, her face beaming.
Emilia: “Iiiii'm—heeere!”
???: “Waugh!? Emilia!?”
The instant she pushes a branch out of the way and pokes out her head, she sees someone towelling
themselves dry right in front of her, looking shocked. Realising that the intruder is Emilia, the
youth's eyes flit here and there and there in confusion—
Emilia: “Ah,”
Youth: “Auh,”
Emilia puts her hand to her mouth as the youth's feet slip and he plunges into the river.
SPLASH. A spray of water cascades up as he lands in the brook.
126
Emilia: “Arch! Are you okay?”
Standing atop where he fell, Emilia looks down and calls down to him.
Bubbles arise one after another on the water's face for a moment, before a blond young man floats
to the surface. He wipes his face with his hand, then raises his hand at the onlooking Emilia.
Arch: “Look, Emilia! Don't interrupt people right when they're almost done bathing!”
Emilia: “I'm sorry. I didn't think anyone'd be here... but I'm glad it was you, Arch.”
Arch: “What're you implying!?”
Emilia pats her chest in relief. Arch yells, cursing the absurdity of it all.
Emilia puts her finger to her lips and hums.
Emilia: “I mean we're close Arch, so you'll forgive me.”
Arch: “Auh...”
Emilia: “Me, I've always thought of you like a big brother... so you'll definitely say there was no
helping today and forgive me, I think.”
Arch: “Think damn what. Goddamn it... has no idea what I feel...”
Arch mumbles his regrets while sinking his mouth into the water, spewing bubbles. Which means
the latter of his statement drowns and Emilia does not hear it.
Emilia: “And I came here to take a bath. Can I jump in next to you?”
Arch: “Wha? I-Idiot, don't! Take a bath, in somewhere as open as this? Of course you can't! Be a
little more discrete! Are you trying to be a child forever!?”
Emilia: “Nuhh...”
Arch: “No nuhhs!”
Emilia: “Wehh...”
Arch: “No wehhs either!”
Having readied herself to leap into the river, Emilia pouts at Arch's prohibition on bathing. She's not
sure why he's so panicked, but either way Arch is being mean today.
Maybe he's mad about slipping and falling in the river.
Emilia: “Arch, I'm sorry.”
Arch: “Er, um... h-how come you're being so docile suddenly?”
Emilia: “I thought maybe you really didn't like falling in. I'm sorry. So let me take a bath too. If I
127
don't, Mother Fortuna won't let me eat.”
Arch: “That's something a kid'd think!”
Yells Arch, hands to his head.
He stops dog paddling for an instant, and sinks into the water slightly. Meaning, for an instant, he
takes his attention off Emilia.
Emilia: “Woo,”
Arch: “Ah!”
After her quiet cheer, sunlight skims across Emilia's eyelashes and—she's falling.
Her silver hair flutters out behind her as she shoots toes-first into the water.
Emilia's contact with the water gives not a single unneeded splash as she sinks with shocking calm,
reaching the bottom of the deep river.
In the clear water, Emilia's open eyes sight the fish and water plants swaying in the current. Her foot
contacts the river bottom. She savours the tickly feeling of sand as she ascends.
Her face pops up beside Arch,
Emilia: “—Pahh,”
Arch: “No! Pahhs!”
Emilia smooths her wet hair back, and backstrokes away from the yelling Arch.
Arch furrows his brows, perhaps wanting to say more, but seems to guess that saying it won't stop
Emilia anyway. He gives a deep sigh and goes around to behind Emilia.
Emilia: “This feels nice, Arch.”
Arch “Well you jumped in yourself so maybe it does for you. I got pushed in, and sprayed with
water when you jumped in so I'm feeling terrible.”
Emilia: “Okay. I'm glad you're having fun too.”
Arch: “You really are an optimistic girl, Emilia...”
Feeling complimented, Emilia floats on the water as she puffs out her chest.
Arch averts his gaze and scratches at his nose. His cheeks are red. But the water's cold. Does he
have a fever?
Emilia: “Are you unwell? Is that why you're mad you fell in the water?”
If so, then of course he'd tell her off for what she did, even after she apologized.
Though, she'd like to drag Arch out of the river and heal him with magic immediately.
Arch: “No it's not that, don't worry. That's not what's going on. ...Um, Emilia. Around guys, you
shouldn't... no I mean, around people, you shouldn't be this exposed. Especially around people
you're not close with.”
128
Emilia: “...? But Arch, you're who I'm closest with?”
Arch: “Even around people you're close with! Erm... b-but just only do it around me.”
Emilia: “Not around Mother?”
Arch: “Around Fortuna-sama, me, and that woman!”
Yelling at Emilia as she tilts her head, Arch bites his lip, his face reddening further. Then he sinks
into the water and grumbles, disappearing from Emilia's view as she furrows her brows.
...is the instant when he splashes up by the riverbank, and pulls himself onto the shore.
Arch: “Okay, you get out of there too, Emilia. When you're just trying to wake up, usually you'd just
wash your face, not take a bath. I don't think Fortuna-sama would tell you go bathing right in the
morning.”
Emilia: “Actually, you might be right. ...I didn't bring a change of clothes.”
Arch: “Seriously, what are you doing...”
Says Arch, looking astonished at Emilia's reckless behaviour.
Emilia starts swimming over to him, when he dashes into the forest and returns with a towel.
Arch: “Wipe yourself down with this, and wrap it around yourself until you get back to your house.
Heck, you're a handful of a child no matter how old you get.”
Emilia: “Ahaha, I'm sorry, Arch. Thank you for lending me this.”
Even Emilia has to reflect on her actions after all of this.
His outstretched hand takes her arm and pulls her out of the river, where she takes the towel and
dries her long hair. It glimmers silver in the sunlight, terribly heavy with water.
Emilia: “...Was my hair always this long?”
Arch: “What're you talking about? You've been growing it out for ages. Something about how it's
the same colour as Fortuna-sama's, and looks pretty.”
The towel absorbs the water, when Arch hits her with that statement.
After hearing it said it does feel like he's right, but when exactly did she decide to grow it out?
Although feeling that something isn't quite right, Emilia chooses to avert her gaze from the
strangeness. She gets the damp out of her hair and begins towelling her body. That done, she peers
into the river and reaches out to fulfil her original goal of washing her face—
—Seeing her face reflected on the water, Emilia's throat jars.
Pale skin. Amethyst eyes. Pink lips. Long, glistening silver hair. All exact components of her own
self. Nothing has changed, and nothing is strange.
129
As if.
Strange things, odd things, incorrect things, are all she sees here.
Emilia: “auh, ah...”
Patting, slapping at her cheeks, Emilia exhales choppy breath after choppy breath.
Her lungs feel like they're convulsing. She can't breathe properly. Her guts constrict, and throbbing,
painful pressure coursing through her whole.
Arch: “Emilia, what's wrong?”
Noticing Emilia's irregular state, Arch speaks with his voice low.
Emilia keeps staring at the water's edge, motionless, as Arch touches her shoulder and strokes her
head from behind.
Arch: “Did you see something strange in the river?”
Emilia: “...No.”
Arch: “Did your stomach start hurting? I can't use healing magic, so I'll have to take you to
someone else...”
Emilia: “That's, not it.”
She feels the touch of Arch's palm and hears the sound of his voice. But does not draw her gaze
away from the water.
Arch follows Emilia's gaze, seemingly realising what she is looking at. He timidly points at Emilia
reflected on the water.
Arch: “Did something happen to your face? But I think it looks the same, pretty as always.”
Emilia: “It's an adult's...”
Arch: “Huh?”
Emilia: “My face is an adult's. ...I've never even seen my face before.”
Seeing an unfamiliar face on the water, Emilia whispers with trembling voice.
She moves her fingers to check whether this face may not be hers, but the reflection mirrors her
movements and denies that possibility. This face belonged to her. Never seen it before, and it's hers.
Emilia: “I...”
After noticing that one decisive point of oddity, many more inconsistencies come into focus.
She looks down. Her chest has grown. Her hair too.
Her limbs are longer than she remembers, and there's supposed to be a bigger size difference
between herself and Arch.
People's perceptions of her and conversations with her have changed in nuance.
130
And how many times have people pointed out that she's not a child?
No. She isn't.
Emilia: “—I have to go.”
Arch: “Emilia?”
Emilia stands up, her head swaying slightly as she turns around.
The forest she ran through, and the village. The house where Fortuna awaits.
She needs to go back there.
She doesn't know what she needs to do yet, but that point alone is unshakeable truth.
Emilia: “Arch, I'm sorry. I'm going back to Mother Fortuna's.”
Arch: “Y-yeah... that's fine, but is everything okay with you?”
Emilia: “I'm fine now. I'm sorry for interrupting your bath. And I'll be okay without the towel.”
Emilia takes off the towel and pushes it against the confused Arch.
She makes sure that he takes it before breaking barefoot into a run. Fast as she can, back to her
house—and behind her,
Arch: “Emilia!”
She hears Arch.
Her heart insists that she has no time to wait, but she still ends up stopping. As if someone had told
her to never let a single thing Arch says escape her.
She glances back. Arch raises his hand.
Arch: “I don't know what's up, but if you're ever worried about something, you can always talk to
me! Because I... because I'm like a brother to you!”
After a second of hesitation, Arch gives Emilia those impassioned words.
For some reason, hearing them makes something surge up in Emilia's chest.
She's definitely happy to have heard those words.
But she has a feeling that that the thing swelling up from her heart differs from ordinary joy.
Emilia: “Right! Thank you, big bro!”
Emilia waves in response to the blushing Arch, and resumes her run.
※ ※ ※ ※ ※ ※ ※ ※ ※ ※ ※
Fortuna: “...I'm sure I just told you to wash your face, so how did you manage to come back with
131
your whole body sopping wet? Your Mother's mystified.”
Sighs an astonished Fortuna as she welcomes her dripping-wet daughter back home.
While her hair has mostly been towelled dry, Emilia's white clothing sticks to her skin and water
drips from her skirt.
Emilia: “I'm sorry, Mother. I was kinda... sooo kinda half-asleep.”
Fortuna: “I know I said to wash your face to get rid of your sleepiness, and you sure did put some
energy into doing that. You really are a child no matter how old you get. Did anyone see you
looking like this?”
It's embarrassing that someone would see you when you look like a drowned rat, is probably what
she means.
Then, miraculously, no she didn't run into anybody on the way back.
Emilia: “No, it's okay. Only Arch saw.”
Fortuna: “Hm... Arch. Well, if it's him... but I suspect Arch has started viewing you differently than
he used to...”
Emilia: “Mother?”
Fortuna: “Ah, erm, no, it's nothing. Now, come here.”
Emilia lowers her gaze. Fortuna looks on resignedly before stroking Emilia's head, then taking her
hand, and pulling her into the house. But water continues to drip from her clothes.
Emilia: “Mother, the house is getting all wet.”
Fortuna: “Just need to towel that dry afterwards. Anyway, I have a towel, so dry yourself with that
and get changed in your room. I'll make breakfast when you're back.”
This house, made in a hollowed-out tree, was created by pouring mana into an old arbour to change
the thing's shape. Emilia and Fortuna's house was hand-made by Fortuna, and is a rather large
dwelling for only two people. The second floor has each of their rooms, while the first floor is a
dining and kitchen space.
Thinking back on it, it was a luxurious use of rooms.
—'Thinking back on it', is a rather weird statement.
Fortuna: “Come on, get going.”
Emilia: “Wagh,”
A towel presses itself into her face while she is in thought. Emilia looks at Fortuna in protest, but
seeing her Mother's gaze as she puts her hand to her hip quickly leads Emilia to surrender.
The towel smells like sun on her face. She dries herself as she returns to her room on the second
floor.
132
Her room is a plain thing.
This also goes for Fortuna, but Emilia doesn't especially like pointless decorations. Her room hosts
the bare minimum of furnature, with a few extra fixtures. It has a wooden box with her clothes in it,
which Emilia squats down next to. She grabs a random outfit out of it and speedily changes out of
her wet clothes and into that.
Just like with her room, Emilia feels no urge to embellish her clothing.
She pulls a short-sleeved outfit, long enough to cover her uppers and lowers, over her head. Then
she changes her undergarments and exits the room. —While making a conscious effort not to look
at the object beside the clothesbox.
Emilia: “Mother Fortuna, I'll wash the wet clothes by myself, so...”
???: “Goodness. I think that filial and excellent of you.”
Emilia: “—”
Emilia puts the laundry in a basket and comes down the stairs, when a man's voice welcomes her.
Emilia's breathing jams as she hears the kind, affectionate voice. She looks over at the dining table.
Usually Fortuna and Emilia would be the only ones around that table, and so one of these three
chairs is excessive. It's the chair they use when a certain someone is visiting, which Fortuna brought
out from deeper in the house.
The person seated in that chair is of course the familiar,
Emilia: “Juice.”
Juice: “Indeed, it is lovely to see you again, Emilia-sama. Now, has anything notably different
happened for you?”
Emilia: “Me? No, it's been same as usual. Juice, it's been sooo long. I didn't know you were coming
today, how come you're here?”
Juice: “You did not know? I was sure that I had asked my finger to contact you prior...”
The mild-faced man, Juice, puts his hand to his chin in thought. He is a good-natured person and
appears to be earnestly disconcerted, but Emilia instantly deduces the culprit.
She passes by Juice to peer into the kitchen, where she sees Fortuna with her hand to her mouth,
stifling a laugh.
Emilia: “Mother, you kept it a secret.”
Fortuna: “Huhu, now did I? I might've only forgotten about it.”
Emilia: “I don't think so. Juice's seat is there, and you're making food for three.”
Fortuna: “Ah, sharp eyes. You're usually a little off-kilter, but you're so perceptive about these
things.”
133
Fortuna winks at Emilia and whistles as she picks up a dish. She presents it to Emilia.
Fortuna: “Now come help set the table, Lia. You can't cook anything on your own, so I should at
least be able to ask you to arrange things.”
Emilia: “Hrmp... changing the subject. And I can't cook because you won't teach me.”
Fortuna: “You'll absolutely mix up the sugar and salt, and I'm too scared to put a girl who can't
handle a knife properly in the kitchen.”
Cutting off Emilia's rebuttals, Fortuna sets dish after dish on the table. Although unsatisfied, Emilia
follows dejectedly behind her to the table.
Seated at the table, Juice looks at the fragrant dishes and breaks into a smile.
Juice: “I am privileged to partake in your cooking, Fortuna-sama. The joy does not fade, no matter
how numerous the occasions I relish it.”
Fortuna: “And there you go again, saying that so easily.”
Juice: “I am merely conveying my honest feelings?”
Fortuna: “That's what I'm saying is devious.”
Juice tilts his head, looking somewhat distressed.
Watching their exchange makes Emilia smile. Just watching them is enough to make Emilia
completely forget about how Fortuna argued her into submission.
Emilia: “If Mother's food makes you so happy, Juice, you should just live here too.”
Fortuna: “Wh—Emilia!”
While placing a large plate overflowing with vegetables on the middle of the table, Emilia rides the
conversation and tries that sentence out. Immediately, Fortuna looks panicked and her face flashes
red as she glances over at Juice.
Fortuna: “D-don't say anything crazy. Juice has so many things he has to deal with, he's fitting time
in his busy schedule to come see us and...”
Juice: “I am overjoyed by the offer, Emilia-sama. Were it a possibility, I would like to oblige.
Sincerely I would.”
Fortuna rushes to object while Juice replies calmly, the two in utter contrast. Juice's statement kills
Fortuna's momentum and she plomps down into her chair, before drawing herself up small.
Looking at the two, Emilia also takes her seat.
—This scene unfolding before her looks overwhelmingly natural to Emilia.
Emilia: “Mother, Juice, if neither of you object then you should just do it. No one's going to stop
you from being like that. Ah... unless I'm stopping you?”
134
It's plain to see that Fortuna and Juice think favourably of the other.
Perhaps they're not going any further than this fixed limit because of Emilia's presence.
However, Emilia's worry is—
Fortuna: “You're not.”
Juice: “You are not.”
—promptly dispelled by the two as a needless anxiety.
Emilia's eyes widen. Fortuna and Juice look at each other, realising that they said the same thing,
and laugh.
Emilia: “See, you really do get along sooo well.”
Fortuna: “Stop teasing us, Emilia. Juice, tell her off too.”
Juice: “Indeed, Emilia-sama. Fortuna-sama is a splendid person. Should someone of my likes
overstay their welcome, it will burden her with objectionable rumours.”
Emilia: “Hrrmpf. But, I think you're too late for that.”
Juice undersells himself as he elevates Fortuna. Emilia sees a sadness in Fortuna's gaze as she looks
at him, and raises her finger.
Emilia: “After all, everyone always tells me it when I go outside the house. Not to cause trouble for
Mother Fortuna or Father Romanée-Conti.”
It's pretty funny how dumbstruck the two look at hearing that.
Emilia puts her hands to her mouth to keep herself from laughing, settles her breathing, and,
Emilia: “I'm serious. When I stayed up last night, and got transfixed in bridging the differences
between the old books you gave me, Juice, and the maps... everyone praises me for helping in my
Father's work.”
Fortuna: “Wh-who is, saying...”
Emilia: “Tehena-san from across the street, Mitto-san and granny Tansei.”
Fortuna: “Those three gossips...!”
Imaging their faces floating in the air, Fortuna bites her lip in frustration.
Her brows shoot down in anger, her face just a little scary.
Emilia says, 'now now' to console her, and,
Emilia: “Anyway, everyone thinks that. And me too, um, I, erm, thought about stuff, kinda a lot,
and, hrmm, uhhh... it's...”
Juice: “Emilia-sama, there is no need to force yourself to ponder it.”
Emilia: “N-no! I think it's good! But it just kinda feels like Mother's being taken away so I can't
calm down!”
135
Everyone else is fully ready for it, but the two of them and Emilia are being fickle.
Though their problem is one thing, and Emilia would prefer that her emotions not get in the way of
their decision.
After all, even by Emilia's view, they're a wonderful match for each other.
Emilia: “I think it'd be sooo great. You two should think about it too.”
Fortuna and Juice are silent.
Emilia: “Not anyone in the forest, and not me, and not anyone's going to stop you. I'm not gonna let
anyone tell you it's bad or you can't do it!”
Emilia's hands strike the table as she speaks zealously.
She then realises that she's getting too passionate, and looks taken aback. The two gaze at her as she
strokes her hair and seats herself.
Emilia: “A-and so... I'll leave the rest to you young'ns.”
Fortuna: “Seriously, Emilia, where are you leaning this?”
Fortuna looks astonished as always at red-faced Emilia's comment. But the expression soon
vanishes beneath a laugh,
Fortuna: “Hee, huhuhu.”
Juice: “Ahaha, Emilia-sama... indeed, you have grown. I was lacking in discernment when I judged
that nothing was different.”
Fortuna: “You were, Juice. She's my prided daughter, of course she would.”
Juice: “Yes, I underestimated her.”
Fortuna and Juice look at each other and laugh.
The atmosphere around the two is even more tender than before, and Emilia senses that her own
statements have brought about a change.
The two of them abound with warmth.
The gaze they share, surely, carries a different nuance from before.
—It's a terribly happy scene.
Fortuna: “...Emilia?”
Fortuna glances at Emilia and calls her name.
Emilia swallows her breath and buries her face in her hands. She panickedly wipes away the tears
threatening to spill from her eyes, and gives a forced, “Ah,”
Emilia: “I, think there's some gunk in my eye. Gunk that's sooo big.”
136
Fortuna: “That big? Are you okay?”
Emilia: “I'm okay, it's only fist-sized.”
Juice: “A-are you certain you will be well?”
Emilia: “I'm fine!”
Emilia rubs vigorously at her eyes as she stands up.
She leaves the table, and begins heading for the second floor.
Emilia: “I'm going to put in some really good eyedrops. It'll freshen my eyes up so well they'll fall
out.”
Fortuna: “Your eyes are such a pretty amethyst, Emilia, don't throw them away. They're exactly like
my brother's, and lovely.”
Emilia: “And they're the same colour as yours, Mother.”
Perhaps not expecting that response, Fortuna's eyes open in surprise. Emilia sees Juice laugh at her
expression, and Emilia laughs too.
She smilies as her foot lands on the staircase. She glances back at the two.
Emilia: “You two eat breakfast. I'll be back right away.”
Fortuna: “It won't be good once it gets cold, so really do come back right away.”
Emilia: “Mm, right right away.”
Juice: “Then we will await your return restfully, Emilia-sama.”
With those send-offs from Fortuna and Juice, Emilia takes a deep breath.
She glances back one last time, looks down at the two at the table,
Emilia: “—I love you both.”
With that, Emilia returns to her room.
Emilia closes the door to her room and sighs, expelling all the air inside her.
Her innards feel squeezed, constricted. She slaps her cheeks to psych herself up, shakes her head,
and walks over to a corner of the room.
Next to Emilia's box of clothes is something long and thin, with a thin cloth draped over it.
Emilia had never thought to reach for that thing until now, but,
Emilia: “If I don't face it, it won't start.”
Give her courage.
137
Emilia traces her finger over her lips, remembering the warmth as she pulls the drape.
The cloth falls.
Behind it is a polished full-length mirror to reflect Emilia from her head to her toes—
???: “—Did this scene of ideal happiness grant you with anything?”
—With a white-haired witch standing where Emilia's image should be.
138
CHAPTER 124: LISTEN UP, STUPID
—How many times has he come to this room to see her?
The first time they met, Subaru easily foiled the girl's illusory looping hallway and entered the
Forbidden Archive.
Their first impressions of each other were mutually horrid.
Beatrice preformed a mana drain one someone still midway through convalescence, and promptly
downed Subaru. Afterwards she had to put up with his endless revenge-inspired meddling.
They would insult each other every time they met, but despite that got along ridiculously well, and
Subaru found himself stopping by the supposedly-veiled Forbidden Archive.
Subaru and Beatrice had had many yelling matches, spit flying everywhere, over these almost-twomonths
that Subaru has been in the mansion, just one immature exchange after another.
Those exchanges changed after the Royal Selection properly began and Subaru returned from the
Capital.
Beatrice was rejecting him. With knowledge gained in SANCTUARY, where she was absent, Subaru
learned her history and fate, and accordingly understood some reasons for her stubbornness.
Then he prattled as if he knew anything, trying to understand her solitude—and Beatrice, long
bereft of tears after these four hundred years, wailed her laments.
There was nothing he could've said to the exhausted girl after that. Immediate circumstances led
Beatrice to lose her life, and Subaru saw that final expression on her face as she protected him.
That expression seared itself into his memory. Running off his emotions, Subaru returned here.
—So that this time, no matter what it took, he'd get her out of this place.
Beatrice: “Taking me out of here...?”
Is Beatrice's bewildered response to Subaru's grand opening statement. She hugs the gospel tighter,
drawing her knees to her chest as she sits atop the stepladder.
Beatrice: “Unwanted meddling, I suppose. Nobody asked for you to do that, in fact.”
Subaru: “This isn't about anyone asking or not asking me. I'm taking you out of here. Decisively.”
Beatrice: “Just scram and have that foolish girl comfort you on her lap, I suppose.”
Subaru: “You little... this's war! You say something like that and it's war!”
Beatrice brings up a topic back from when Subaru was overloaded in this mansion, and he strains
his voice to distract from his internal shame.
Beatrice snorts at him and glances away.
Subaru: “Anyway, this isn't the time to be mucking around like this. We have basically no room to
postpone anything. Have you grasped what's going on outside?”
Beatrice: “...I do know that some uninvited guests have come to the mansion, in fact. After the big
139
and little maid did something or other, two preposterous people started going on a rampage, I
suppose.”
Subaru: “Though, one of those preposterous people's a helper who I brought along. I don't think
he'll lose, martially speaking, but unfortunately I get this feeling the difference in their resolve'll
determine the win. And so I can't accommodate too much of your solemnity here.”
Beatrice: “Then you're evacuating the mansion's residents while your assistant buys time ...is your
scheme, in fact. Are you trusting in your ally or aren't you with this sloppy strategy, I suppose?”
Subaru: “The strategy's like this 'cause I know he's way too kind.”
The restorative effects of Garfiel's EARTHSOUL BLESSING mean that his current condition is 80~90%
of his maximum. When adding on his lack of hesitation for battle, he's quite a considerable fighting
force. But Subaru doubts that he has sufficient resolve to kill his opponent, which will keep him
from putting in his all, which is a bit of a minus.
Meanwhile Elsa is in perfect condition. Subaru judges her strange, unexplainable combat strength
as a good match for Garfiel at his best. Her tendency to enjoy herself during her battles is something
of a minus for her combat-wise, but she has that inexplicable immorality. Elsa's statements give no
suggestion that killing her indefinite times will make her stay dead either. Subaru's tentative
estimations dictate that Elsa has the slight advantage.
Subaru: “But if the strategy's working, Frederica should collect Rem while Garfiel's suppressing
Elsa. Petra met up with Otto, so now there's only one essential evacuee left before we can save
everybody.”
Beatrice: “Essential evacuees... you mean to say that Betty is the last, in fact.”
Subaru: “Yeah, I do.”
Subaru had instructed Petra go meet up with Otto, who has guided the villagers in Arlam to safety,
and retreat after helping with a few gambits in the mansion.
Subaru has spent time reaching the Archive, and she should have finished her departure by now.
Subaru: “And so I'm getting you out of here. If you don't wanna run while holding my hand, then
I'll piggyback you or cradle you or do whatever to you, so just behave and come over here and...”
Beatrice: “Don't make me repeat myself, I suppose. I don't need your help, in fact.”
Subaru steps closer and offers Beatrice his hand, but she speaks low to reject him. He comes to a
stop in front of her as she turns her head in indication of the room.
Beatrice: “Hear me, I suppose? An isolated space, of power worthy of Betty, separated from the
cloisters of time. This is Beatrice's Forbidden Archive, in fact. Regardless of whatever threatens the
outside, that threat will never reach Betty's Archive. Your fears are needless, in fact.”
Subaru: “Nope, they're needed. Your Archive's randomness does mean it's strongly advantageous
when it comes to fleeing, true... but, it has a fatal flaw. And the enemy knows what it is.”
140
Beatrice: “A fatal, flaw?”
Beatrice furrows her brows, indeed unable to let the comment pass. But Subaru just responds to her
harsh gaze with a nod, and gestures to the door behind him.
Subaru: “Your power which randomly connects to some door in the mansion is strong. But... it only
works on the mansion's CLOSED DOORS. So if you leave the mansion's doors open, you're certain to
reach the Archive eventually, since you'll be losing doors until only the Archive's is left.”
Beatrice: “—hk”
Subaru: “It's such a stupid thing. I bet you didn't notice it either. I was wondering why I hadn't
realised it until practically I witnessed it myself.”
Subaru remembers when Elsa, having noticed the loophole in GATE CROSSING, found the Archive.
If Garfiel wasn't around to impede her, Elsa would unmistakably come here while using that exact
same method. And likely take Beatrice's life.
Subaru: “Though of course, it's not like I'm underestimating you, or saying that her showing up here
means you're going down easy. It's just that her strangeness is some of the extremest I've ever
experienced. If we can do this without facing her, there's nothing better.”
If they can defeat Elsa then he would like to do that, but it's not an essential requirement for
clearing this loop series. If Roswaal is the one hiring her, then so long as Subaru crosses the time
limit for the issues in SANCTUARY, Roswaal should stop having any reason to keep hiring Elsa.
The whole insignia affair in the Capital proves that this would make Elsa withdraw.
Either way, right now they need to survive through the attack on the mansion and—
Subaru: “Beatrice. This place isn't safe. If you're not here, she won't disturb the library. So just for
now...”
Beatrice: “Why does that woman know how to break Betty's GATE CROSSING, I suppose?”
Subaru: “—”
Subaru spits out the suitable bargaining chips to convince Beatrice to leave.
But Beatrice, perhaps listening to Subaru's statements or perhaps not, whispers a whisper differing
from what Subaru's looking for.
Subaru shuts his mouth. Beatrice remains upon the stepladder.
Beatrice: “It's inconceivable that she would abruptly conceive of how to break Betty's GATE
CROSSING on her first encounter with it, in fact. Whoever taught her those methods knows me, I
suppose.”
Subaru: “Beatrice. This isn't the time for that conversa—”
Beatrice: “—It's Roswaal, in fact.”
Subaru can't divert her.
Her swift thinking makes Subaru swallow his breath.
141
Seeing his reaction, Beatrice understands everything. Roswaal hired Elsa, and his goal is to kill
Beatrice. Which means—
Beatrice: “It is written in Roswaal's gospel that I be killed, I suppose.”
Giving no heed to either Subaru's affirmations or denials, Beatrice sighs.
It's unlikely that the relief Subaru perceives in that sigh is just his imagination. Unable to overlook
the comment, Subaru puts pressure on Beatrice.
Subaru: “Want to tell me what that sigh was? And why the hell you look like you're agreeing!?”
Beatrice: “It's what it looks like, I'm agreeing, in fact. If Roswaal's gospel has ordered him to do
this, then that means my fate is decided, I suppose.”
Subaru: “Fuck is that... Roswaal's book is Roswaal's book, and your book is your book! Your book
really says to go get killed by Roswaal, does it!?”
Jabbing out his finger, Subaru glares at the gospel in Beatrice's arms.
If nothing has changed from the previous loops, then for four hundred years, that book has written
just blank white paper.
Beatrice's expression turns gloomy and she opens to a page of the gospel. She spreads the book
open and presents it so that Subaru can see it—showing a book of only empty pages.
Beatrice: “Nothing is written, in fact. Identical as ever, only blank pages, I suppose.”
Subaru: “Then there's no reason for you to get killed like Roswaal's book says! It's same as ever,
you're who decides what you do!”
Beatrice: “...The same as ever, I'm the one deciding?”
Subaru: “Yes! Nothing being written means you must've faced choices during all this time. Small
things to big things, you're the one who decided every path you took! So there's no reason for you to
dance along to someone else's choices this time, eith—”
Beatrice: “What in my life have I ever decided?”
The doleful question crushes Subaru's momentum.
Beatrice tilts her head as she gazes at Subaru, her eyes melancholy. She flips through the blank
pages
Beatrice: “All the time Betty spent in Roswaal's mansion, protecting the Archive that Mother
entrusted to her, endlessly, endlessly... when during that did I ever have time belonging to myself?
When did Betty, having lived empty centuries without writ, ever leave her footsteps anywhere in the
world? What did Beatrice ever do, and who is she?”
Subaru: “Bea, trice...”
Beatrice: “Betty's life, Betty's four hundred years, are as blank as this gospel, in fact. A void, in fact.
What I chose by myself, what I gained by myself, what can attest of myself... all non-existent.”
142
Beatrice claps the gospel shut and sets it on her lap. She strokes its nameless cover as she quietly
speaks,
Beatrice: “I'm identical to an empty book. Losing me here simply means losing a blank, letterless
text. Never anything to anybody, merely a book shoved in a bookcase—it'd be laudable for it to be
gone, in fact.”
Subaru: “What if there's people who don't want that blank book gone?”
Beatrice feels to be verging on abandoning her four centuries and her future. Subaru manages to get
words out in an attempt to connect to her heart.
Subaru has not yet found his reply to Beatrice's tearful scream from back then.
But even so, should he fail to speak here, she will give up on herself.
Subaru: “You called it nothing, a void. But there assuredly is a book wedged inside that bookcase.
There are people who know that book exists. And maybe there's people who'll want to pick up that
book someday, you think they'd stand the thing going off and destroying itself?”
Beatrice: “The book has neither name nor author, I suppose. Supposing for argument that this
benevolent someone exists, opening that book and seeing the inside would only disappoint them, in
fact. The blank book doesn't want to watch the disappointment unfurl across that person's face
either, I suppose.”
Subaru: “Then! Then what is that book doing in that place!”
Beatrice: “—”
Beatrice gazes emotionlessly at Subaru.
It feels like a retort, saying this whole dialogue lacks any apparent meaning. Subaru raises his head
regardless, continuously reaching out to Beatrice's distant heart.
Subaru: “If someone who picks it up's just going to be disappointed... then for what sake is that
book there? Wasn't the book made because it had meaning?”
Beatrice: “...The book's author crafted that book for the sake of a person, in fact. The book is made
to appear empty to everyone except for that SOMEONE, I suppose. If we assume there's to be
meaning, then the very instant the book reaches the SOMEONE comprises the meaning of that book's
creation.”
Subaru: “And so then—”
Beatrice: “The book mustn't be disposed of until it reaches the SOMEONE, you're saying, I suppose.”
Subaru swallows his breath.
He notices an instant before can voice it what a cruel breed of hope he is arguing for. Beatrice sees
Subaru's expression, and a horribly pained smile arises on her face.
Beatrice: “Exactly. If Betty truly were just a book... then she'd be happy to wait for that day, in
fact.”
143
Beatrice would have waited there for that day when the SOMEONE's fingers flipped through her
pages.
If she were a book.
—But Beatrice isn't a book. She's a little girl, shivering from prolonged isolation.
Beatrice: “If I were a soulless, mindless book... then I could have faultlessly believed in Mother's
instructions forever. I could have been Mother's lovely Beatrice forever, I suppose.”
If she were an entity like a doll, lacking a heart and comprised only of ornamentation, she would
have never deliberated.
If she were an entity like a book, unshaken by the constant passing of time, she would have never
lamented.
Beatrice was not that thing.
Beatrice: “But I have a heart. Should time pass I do think about things, at least enough to lose faith
in what I believed in, in fact. I agonize and deliberate, I suppose. There were countless nights where
I scrambled to salvage my memories, because I'd forgotten what Mother's face, what her smile
looked like!”
Subaru: “—”
Beatrice: “There were times I couldn't bear being alone, and I yearned to touch someone! But
everyone leaves me behind! They'll say whatever they'll say, state it's for the sake of something
more important than me, assert their rationale, and desert me! Mother did! Roswaal did! —Even
Lewes did!!”
Beatrice shouts, her face scrunched up and near to tears.
Hearing the name Lewes makes Subaru remember what he heard in SANCTUARY about Beatrice's
past. And the root of all the present Leweses, Lewes Meyer.
She and Beatrice had only known each other for a fleeting instant, but their story still told of a
definite bond. —Still left a persistent scar on Beatrice's heart.
Beatrice: “—Just, enough, in fact.”
Beatrice loses her momentum. The tone of her voice plummets.
Her expression, twisted with emotion, returns to its usual apathy as she hugs the book on her lap
close.
Beatrice: “Betty's gospel will not outline Betty's future. ...I've known it for a very long time, in fact.
Even Mother forsook Betty's fate far and long ago.”
The lack of writ about the future means that the gospel's owner has fallen into a dead end.
While judging off Subaru's possession of Betelgeux's gospel, that was how Beatrice appraised
books with frozen writ. Appraised that the same thing was happening to herself.
Beatrice: “If Betty's fate has been outlined in Roswaal's gospel... how sardonic, I suppose. But that
does ease me, in fact. It's inconceivable that Roswaal would take half-measures, I suppose.”
144
Subaru: “An old friend of yours might kill you... how is that relaxing?”
Beatrice: “It's obvious, in fact.”
Beatrice nods.
A fleeting, affectionate smile arises on her face.
Beatrice: “If Roswaal's gospel has written about me... then it means that Mother has certainly not
forgotten about me, I suppose.”
—Warped.
Beatrice's smiling visage makes Subaru notice that he is seconds from drowning beneath an
emotional torrent.
It's warped. Beatrice's visage as she rejoices in her contact with her mother's love is so warped it's
unbearable. Subaru could stand that this thing, that this happening, was a mother's love—as fucking
if.
Beatrice: “...What are you thinking to do, in fact?”
Subaru bites his lip and endures the sensations welling up in him as he steps forward.
Caution cloaks Beatrice's expression as she perceives the alarming vibe emanating from Subaru.
Subaru: “—”
Beatrice: “I asked you a question, I suppose. What are you thinking to do, in fact? If you try
anything, I'll show no mercy, I suppose. I've already accepted my fate, in fact.”
Subaru: “Accepted goddamn what. So you're no different from Roswaal. No, he's at least self
aware, you're multitudes more awful. Utterly hopeless, let it get fucking worse.”
Anger surges from inside him.
It's an emotion that Subaru has constantly combated since all these events in SANCTUARY.
Anger at himself while challenging the TRIAL, anger at the witches for toying with him, anger at
Garfiel for underestimating himself out of childish stubbornness, anger at Roswaal for obeying the
writ to try and affirm the fragility of feelings, anger at Emilia for not believing in herself or Subaru's
love—
—and now anger at Beatrice, and everyone who cornered her into this.
Subaru: “You're stupid. Say whatever about your fate, say whatever about your Mother's orders,
anyone looking from aside's gonna think it's sad. You have a heart? You can't be a book? Of course
you goddamn can't, stupid. Did staying holed in this moldy room make you incapable of
recognizing that?”
Beatrice: “Stu...!”
Beatrice's eyes shoot open, and after a look of surprise—indignation.
145
She gets to her feet on the stepladder, her skirt swaying as she points at Subaru.
Beatrice: “You! Who do you think you are referring to with that comment, I suppose! I'm stupid,
I'm stupid? How do you dare say this, in fact... and especially by you! What do you think you could
possibly know about Betty, I suppose!”
Subaru: “I know you're stupid, and you don't realise you're stupid, so I'd say I know you better than
you do! Stupid! Stupid! Stupid! Stuuuupid!!”
Beatrice: “Y-y-you...!!'
Subaru flips the bird as he curses, turning Beatrice's face crimson and blocking off her words. Her
rage is too incredible for her to come up with any retort.
Barging into openings like that happens to be Subaru's forte.
Subaru: “A four-hundred year void? Drop the affectations! You hugged your knees crying for four
hundred years is what you did! You had all that time to think, why the hell are you clinging to this
single answer forever! The book's not telling you anything so you think that means I DIDN'T DO
ANYTHING? Are you stupid!?”
Beatrice: “O-of course I thought about things, in fact! As I plainly would, I suppose! Can you
conceive how many things I tested to see if the gospel's writ would change! But no matter what I
did, no matter how I waited, it didn't! So!”
Subaru: “That's what I'm saying is stupid! The book's got nothing in it so you work to try and make
letters appear, the hell is this, invisible ink on a New Year's card? No one does that any more! If
none of that was working, start thinking of other possibilities!”
Beatrice: “O-other, possibilities...”
Subaru: “Straight-out. The possibility your mom's book was wrong.”
Beatrice falls utterly speechless.
But she immediately snaps at him, determining his reply as moronic.
Beatrice: “You hold your tongue, in fact! Mother would never pull such an idiotic stunt, I suppose!
You... you could not possibly comprehend Mother's vast thoughts, in fact!”
Subaru: “Nope, don't know'em at all, stupid. Like I care anything about what your mom thinks.
What we're talking about is you. And you said it, didn't you. You said that she'd never pull
something that idiotic. Really? Can you assert it? You've never doubted your mother even once?”
Beatrice: “What, are...”
Subaru: “Four hundred years! Gone with a self-writing book sitting absolutely blank! The person
you're waiting for never came either! You spent all of that time alone, had so much room to think it's
ridiculous, and you never thought of it even once? You seriously never thought that this was
strange!?”
Four centuries spent believing in someone.
146
Perhaps it sounds like a sterling way of being. But in truth it is crooked. Especially when spent only
ever thinking about the person, and only ever about their words.
Especially when you're Beatrice, who does not think her wish will come true, and has nigh given
up.
Beatrice: “I-it is inconceivable that Mother would bring about anything incorrect, I suppose! O-of
course she wouldn't, in fact. She is Mother, I suppose! Do you think it possible to doubt the words
of your own mother!?”
Subaru: “Of course I do! I think the stuff my mom says is overwhelmingly lacking in credibility!
That time when she misheard news that 'a satellite fell into the atmosphere' as 'a satellite fell into
Aichi prefecture' and I went zooming out with the big scoop without verifying it is when I stopped
trusting her! That was in third year primary!”
He would never forget the day that he sincerely accepted that, spread the rumour, and turned into a
schoolyard laughingstock.
Subaru never trusted anything his parents said ever again. And he had already deemed his father's
statements as unreliable prior to that.
Subaru: “Four hundred years, and you never doubted her for even a second!? I'm not even twenty
years old, and I'd run out of fingers before I could count the number of fistfights I've had with my
dad. And that's with twenty years. You had twenty times that, and you never felt that way even once,
huh?”
Beatrice: “You... what are you wishing to make me say, I suppose!? I utterly cannot discern it, in
fact! Your aims, the point of your remarks, are utterly arcane to Betty! Arcane!”
Subaru: “Then I'll say it loud and clear! So that your stupid self and your stupid mother can hear it!”
Beatrice is about ready to clutch her head in frustration when Subaru approaches, and takes her
hands.
Beatrice looks up. Subaru draws his face close, into breathing range, and asserts to the teary girl:
Subaru: “Stop getting thrown around by a blank book and a four-hundred-year-old promise. —Be
the one who chooses what you want to do, Beatrice.”
Beatrice: “—”
Subaru: “It's four hundred years. Plenty long enough for at least one rebellious phase to hit.”
Beatrice has admirably been trying to obey her parent's instructions.
Her stubborn volition to keep that promise has spawned her solitude and a timespan of emptiness.
Her mother, Echidna, seems to find even that time spent in agony as something sweet, but from
Subaru's perspective it's profane immorality.
She's forgotten how to cry and the feeling of wanting to cry, the fuck about this is 'sterling way of
being'. Don't make him puke.
With her hands still in Subaru's grip and atop the stepladder, Beatrice looks away from Subaru.
147
Her height as she sits on the top step is practically equal with Subaru's eye level. She eventually tilts
her head down, lets her lips move,
Beatrice: “Th, en... this is, what you're attempting to say, I suppose. Betty, disobey Mother's
orders.”
Subaru says nothing.
Beatrice: “Abandon everything you believed in over these centuries and be free... that is what you
are so easily saying to me, I suppose.”
Her shaking voice gradually regains its composure.
It begins to fill with something that is not shock, and Subaru feels his hair standing on end. Ever
since coming to this world, this sensation alone is one he has undeniably honed.
That being, the sensation of a direly hazardous entity.
Beatrice: “—Demanding that I, Beatrice! Violate a contract! Speaking as if you know anything!”
Subaru: “—Aguh!?”
As if stricken by a galeforce, Subaru goes flying backwards.
His back strikes the archive floor, still encircled by a wind which slams him into the wall. His
breathing stalls. His bones creak all across his body and his vision strobes as he raises his head.
Beatrice remains atop the stepladder, but her expression is one of fury as she looks down at Subaru.
Beatrice: “Contracts are absolute! Absolute, in fact! And especially so for contracts made between a
spirit and a witch. You demand that it be annulled unilaterally, and by the spirit? You understand
nothing, I suppose! Such a thing would never be forgiven! Not anyone! Not anything! And not even
I myself would permit it, in fact!”
Subaru: “—From someone searching for backdoors in that contract and thinking if they can't violate
it better try and get killed, that's rich.”
Beatrice: “—!”
Subaru sighs to force the pain out of him as he sluggishly uprights himself.
Beatrice's rage is not faltering, and her adorable expression remains thick with malice. Subaru raises
his head and laughs venomously.
Subaru: “You're an incoherent mess, Beatrice. You haven't realised how inconsistent you're being?
Of course you've realised it, haven't you. You're a smart person.”
Beatrice: “Be silent, I suppose.”
Subaru: “No, I won't. Annul the contract? Sounds perfect. When you hate keeping the promise so
much that you literally want to die, just stop. No one'll fault you.”
Beatrice: “I will fault me! Why is it you don't understand that, in fact!? Contracts are absolute, and
keeping them is...”
148
Subaru: “Why don't you understand it? If keeping the contract kills you, you need to violate the
contract and live. Is it really so strange that I'm opting for this?”
Subaru easily discards these contracts Beatrice is so fixated on. Beatrice has no words. Subaru
might presently look like an incomprehensible, monstrous creature to her.
Subaru finds it far more mystifying that he's being recipient to that opinion.
Keeping promises is important, of course.
Emilia has criticized him multiple times for breaking promises, and he has gone through multiple
painful experience because he broke them. And so even Subaru knows that keeping promises is very
important.
Even so, he feels no hesitation about making Beatrice violate her contract.
And his reasoning for it is exactly what he just told her.
If anyone demands that Beatrice keep the promise and die, Subaru's flipping the guy the bird and
telling him this: He will make her violate the contract, and make sure Beatrice lives.
It's not even something to think twice about.
Beatrice: “Th-that is unrelenting, incorrigibly insidious of you, in fact...”
Subaru: “I know it's unrelenting, and I am sorry for saying it. But it's important so I'm not
surrendering this.”
Subaru's stance was decided from the very beginning. From the very beginning, the whole issue
depended on Beatrice's feelings.
Beatrice cannot hide her panic and confusion at Subaru's disparagement of contracts. And of course
she can't. Contracts are that important a thing for spirits.
Having witnessed the relationship between a spirit and a spiritualist, Subaru knows they are firm,
weighty, utterly unshakable things.
He knows, and he's saying it:
You are more important than it.
Beatrice: “I-if, you... were THEY...”
Subaru's response to contracts is overwhelmingly overwhelming.
Frailty creeps onto Beatrice's expression, which borders on breakdown.
Her lips speak of the insubstantial someone that Beatrice has waited for over these four centuries.
The fictional entity that Echidna cruelly invented so that she could know WHO BEATRICE WOULD
CHOOSE.
Beatrice wants to be saved.
The way that Subaru's words shake her heart and bring her to tears proves it better than anything.
Beatrice: “Will...”
Beatrice's teary eyes focus on Subaru.
149
Her lips tremble, and, practically clinging,
Beatrice: “...you be Betty's THEY?”
This question could be the full stop on what has gone on for four centuries.
And might be exactly what Echidna ordered her, making it what the witch wants to hear.
Who would Beatrice determine as being this insubstantial THEY?
The witch used her daughter to satisfy her own curiosity, letting her spend four hundred years in
solitude.
The payoff for all that time rested in that question.
Beatrice swallows her breath. Subaru looks her in the eye, and declares:
Subaru: “Are you stupid? —Of course I wouldn't be this weird mysterious THEY of yours.”
※ ※ ※ ※ ※ ※ ※ ※ ※ ※
After the ferocious shockwave gusts through the Archive, Beatrice takes the books thrown about by
the wind and returns them to their bookcases.
While they did fall to the floor, none of the books look to have separated from their bindings,
fortunately.
Beatrice reflects remorsefully on her use of force while inside the Archive, relieved that only very
minor damages occurred.
They are her comrades, who passed four hundred years of solitude alongside her.
Beatrice had not been lying about her wish to be a book. She had fantasized many times about being
like these texts, something which could wait for such a long time without it rocking her heart at all.
She now thought it hope born from a stupid idea.
Beatrice: “Conceivably, it is laughable, I suppose.”
This is the wretchedness into which she has been cornered.
She mocks herself for it. But inside her small chest, self-deprication falls subordinate to wrath.
Beatrice: “That guy... that guy... truly, what is wrong with him, I suppose!”
Just thinking about him aggravates her, brings her close to stomping the ground.
She'd like to vent these pent-up emotions on something, but everything in this place which her
Mother instructed her to protect is precious.
Unable to find anything to take her tantrum out on, all Beatrice can do is wait for her bloated
emotions to wither.
She returns the final book to its shelf and sighs as she smooths out her appearance. Then she seats
herself back on the stepladder, reaches to cradle the black tome—and stops.
A blank book. Just throw the thing away! He had said so easily, so many times.
150
Then at the vital moment, he rejected the option which would have allowed Beatrice to discard the
thing. Absolutely, entirely, so incomprehensible it infuriates her.
Beatrice: “I'm exhausted, in fact...”
But her fury will not last forever.
Beatrice stops puffing out her cheeks, takes that book she had hesitated to hold, and puts it to her
heart.
Ultimately, to the end of the end, leaning on this thing is the only way to protect her mind.
Just as Roswaal's gospel has writ, Beatrice's end will arrive soon.
What emotion should she feel as she waits for it to come?
It's finally ending. Wouldn't that be a good enough sentiment?
It's the one she's supposed to be feeling, but now that it's actually happening, she's lost.
—You are stupid. For some reason those words remain, sitting heavily in her heart.
※ ※ ※ ※ ※ ※ ※ ※ ※ ※ ※
Blown away by the shockwave, Subaru tumbles down the corridor until he slams back-first into a
wall. His side strikes directly against a column, leading him to shriek and writhe.
Subaru: “Ghhah! Hhgahghh... I-impossible! Halfway through the conversation, and that idiot
just...!”
The door in front of him slams shut. Subaru reaches out for the door, his expression hateful, but
naturally the sight he sees after cracking the thing open is not the Forbidden Archive—merely a
guest room.
GATE CROSSING has activated, and Subaru has been expelled from the Archive.
Subaru: “I pissed her off so much she threw me out... fuck, messed up with my word choice!”
What he was trying to say wasn't incorrect, but there was contradiction between how he was telling
it and showing it.
Resulting in Subaru being thrown out of the Archive, and distanced from success.
Subaru: “Anyway, can't stay here. Have to find Beako through another door and...!”
???: “N-Natsuki-san?”
Subaru turns around, thinking to conquer the doors via utterly random selection, when a voice
addresses him. The familiarity of it, and the fact it's calling him lead him Subaru to stumble and for
his eyes to shoot open.
His gaze lands on Otto, peeking out from a neighbouring room, when he's supposed to be
somewhere else. And peeking out from under Otto is Petra, also peering at Subaru.
151
Subaru: “Y-you guys? Why're you still in the mansion? I thought I told you that just one wing's fine
and to run away after opening the doors?”
Otto: “Unfortunately, the situation outside has changed rather dramatically...”
Otto shakes his head, his face pale as Subaru approaches
It's inconceivable that Otto would be joking in this situation. Otto has aborted his escape, and there
must be something happening which warrants that.
Subaru: “What happened? Short version please.”
Otto: “Witchbeasts did. Hordes of witchbeasts are encircling the mansion, and we cannot move.”
Subaru: “Witchbeasts!?”
Subaru's eyes shoot open wide at the unexpected word and he looks to Petra for confirmation. She
nods several times in response.
Petra: “Erm, there's lots of witchbeasts which aren't the dogs... like snakes with two heads, or like
possums, lots of them.”
Subaru: “Do these guys live in the nearby forest?”
Petra: “They do, but.... the barrier should be keeping them out.”
Subaru: “This barrier again...”
During the previous witchbeast debacle, they confirmed that the barrier between Arlam Village and
the woods surrounding the mansion had been repaired. Afterwards they put top priority on looking
out for weaknesses in the barrier, so it's inconceivable that a mistake could've happened after such a
short timeframe.
And most importantly, the beasts are surrounding the mansion for some reason.
Subaru: “It's like with those mutts, some weird volition is operating on them...? What about Arlam's
people? Are they okay?”
Otto: “I couldn't locate any witchbeasts when I instructed them to evacuate, and since they've used
the carriages from the Duchess to flee, they should be safe. Patrasche-chan is guiding them too.”
Subaru: “Okay. That's a relief.”
It's more trustworthy that the clever dragon be tasked with escorting them than some random guy.
While praying for Patrasche to pull it off, Subaru grits his teeth. The situation is unfolding down a
track unknown to him yet again.
This witchbeast attack has never happened before.
Naturally, considering the timing, it has to be related to Elsa's attack.
Subaru: “What about Frederica and Rem?”
152
Petra: “We haven't run into Big Sis Frederica or Rem-san... Erm, I-I don't really think they can
break through them and get away.”
Subaru: “Which means they're also still in the mansion. We'll be thankful the beasts're still staying
outside, but how much can Garfiel do?”
Subaru strokes Petra's head, praising her strong heart for remaining composed during this extreme
situation. If it were Subaru when he was her age, it wouldn't be weird for him to piss himself crying.
But circumstances prohibit them from staying here.
Subaru: “Where are we right now? Which wing of the mansion?”
Otto: “The eastern. Garfiel should still be battling in the western wing, so I'd suggest avoiding that
area to circumvent damages...”
Subaru: “And so the possible escape routes are...”
Of course Subaru needs to collect Beatrice, but it's also indispensable that Otto and Petra escape.
Subaru descends into thought, thinking to scrutinize his mental map of the mansion for any possible
escape routes. However, a voice drowns out Subaru's contemplations:
???: “—Oh my? You were all gathered here, waiting for me?”
A petrifying feeling, like a blade stroked against the back of their necks, leads all of them to freeze
rigid.
Subaru promptly pulls Petra's arm and hugs her close as he timidly glances behind him.
Further down the hallway, lit with bars of moonlight, out peal someone's approaching footsteps.
Their shape soon enters recognizably into the light,
Subaru: “What the hell is Garfiel doing!?”
???: “I'll unveil pretty guts from all three of you—”
Kicking off the floor before the shrieking Subaru, the Guthunter's black shadow darts as she bounds
near.
153
CHAPTER 125: THE ROSWAAL MANSION BATTLE
???: “—DONAA!!”
The only one who manages to immediately react to the oncoming threat is Otto.
He holds his hands out in front of him, influencing the world with a canto—the torrent of mana
breaks through the mansion floor as up surges a wall of earth, which blocks the whole of the wide
hallway and impedes the shadow's advance.
However,
Elsa: “Nuisance.”
Subaru: “Just one hit!?”
One short statement, and two swings of a kukri.
The slash tears through the wall like paper, and with one kick to the bisected blockade, the whole
thing crumbles instantly.
Scattered particles of mana alongside the collapsed wall's remains. An archetypically sadistic smile
alongside the silver gleam of a knife.
Elsa: “First is to slit your throats and silence you, or I suspect you won't be cooperative.”
Subaru: “Stop saying this terrifying stuff!”
Using the momentary opening Otto created, Subaru holds Petra close and tumbles into a
neighbouring room. Otto follows a second behind, shutting the door before immediately
manoeuvring behind the bed.
A slash cleaves through the door. The dangling lower portion of the door plummets, kicked, into the
room.
Subaru: “Take this I guess!”
Elsa swoops into the room, for Subaru to attack her with a wooden clothes-hanger. She dodges by
tilting backward and slices the thing in two with a flourish of her blade, aiming for Subaru's throat
with the backswing. But thanks to Petra jumping in and pushing Subaru out of the way, the contact
ends with only a graze.
Elsa: “Goodness. Bad girl.”
Subaru: “She's our pride and a good girl, moron!”
Blood seeps from Subaru's neck. He presses down on the wound pulls Petra close, retreating.
A ghastly grin arises on Elsa's face as she prepares to pursue them.
However,
Otto: “Then how about this!”
Otto tosses a spellstone, aiming for Elsa's face.
This glowing red thing, packed with fire mana, behaves much like a shotgun bullet. It's Otto's trump
card, even more pure than the one he used against Garfiel.
154
Otto's hidden ace shoots straight for the defenceless Elsa—detonates.
The spellstone bursts apart in crimson halfway between Otto and Elsa.
Noise and light whip through the room, a heated wind fanning Subaru as he watches:
His eyes focused so intensely that time feels to lag, Subaru sees how Elsa doesn't even bother to
turn around as she throws her knife and curbs Otto's spellstone.
The stone detonates at an unintended point in space, burning Otto's eyes. He screams as he pitches
back.
Elsa drives her foot into Otto's exposed stomach, sending him shooting away to crash into a wall.
She does not even glance at the crumpled Otto as she instead turns toward Subaru, who swallows
his breath. Elsa's brows hitch up.
Elsa: “Oh? You're... I think I know you from the Capital.”
Subaru: “I-I'm honoured you remember me. So with that relationship in mind, would you mind
overlooking us?”
Elsa: “I make a point to, no matter how long it takes, witness any guts I previously failed to
behold.”
Subaru: “She's a collector!”
Subaru can feel Petra clutch tighter at his sleeve. His thoughts solder white.
He keenly senses that his gate is dead. He can pray or set his soul ablaze, but neither his mana nor his
gate are giving the slightest murmur of response. It's impossible for him to use Shamac here, and
more importantly it would be a fool's work should he immobilize himself again.
Which leaves him with only one method—Invisible Providence.
Subaru: “—”
The instant he decides to use it, a dark, alien thing slithers through Subaru's body.
It had been still, but began asserting its presence the moment it realised that Subaru was calling it,
eager to display its power and cheering.
A foreboding feeling strikes him, as if he is feeding a repugnant monster.
While consciously ignoring the feeling, Subaru issues orders to the dark power shrieking its birthing
cry, and determines to cut open a pathway from his inside to the outside.
He could cry blood with this agony, and he is aversive to using this power.
Regardless. He clings onto what he can, utilizes what he can, and lives while capitalising on
whatever he can.
All to save everyone he wishes to be saved.
Elsa: “Ahh... what a thrilling expression you have.”
Subaru: “I'll show you something better.”
Elsa: “How excited I am.”
Taking aim at Elsa's core as she brandishes her two blades, Subaru pulls the trigger taut.
155
Now he just needs to release, and her slender form will be shredded mauled and perforated.
Subaru: “—○○○”
A squirming thing flows into his bloodstream, courses through his whole.
It almost feels like the air he breathes is chromatic, like he is cloaked in blazing heat, as the dark
alien nails extend, Elsa's bisection conceivable and anticipated.
Just like this, offer up everything, and—
???: “Subaru!”
A grieving cry, and the dull pain of a pinch at his side.
Subaru scrunches his face in surprise, the repugnant emotions inside him dispersing immediately.
What remains are the faint dregs of dark taint, and unchanged emanations of black murder.
Elsa has begun swooping near, and Subaru as he panickedly tries to repair his aim will not manage
it in time—when,
Elsa: “—Close.”
???: “—Evaded!?”
It takes Elsa a microsecond to ascertain the gust closing in from behind, and dodge.
She aborts her attack on Subaru and twists away, dancing out from under the claws which gouge her
back.
Flipping backwards, she drives a kick into Frederica's flank and rides the momentum to jab her
elbow into Subaru, sending both of them flying as she somersaults backwards—escaping from
between them to calmly land on the room's bed.
Elsa puts her hand to her back, looks at the blood on her palm. She looks to be in ecstasy.
She then looks at Frederica, kneeling on the floor, and tilts her head cheerfully.
Elsa: “Yet another... no, two more people to receive me. Truly a wonderful mansion.”
Frederica: “That ambush did not even work... those are not the reflexes of a human.”
Frederica groans in frustration, unable to hide her shivering.
The blow to his chest leads Subaru to cough as he crawls over to Frederica.
Subaru: “Frederica, my bad, thank you. And, Petra too.”
After addressing Frederica, Subaru thanks Petra, her hand in his. Petra shakes her head with her
eyes teary.
Petra: “N-no, I'm who should say sorry. But, Subaru... your eyes looked so scary, and...”
Subaru: “Honestly, I think I was on the border of getting swallowed. That might've turned out bad if
I wasn't pulled out of it. Guess I can't be careless about using Invisible Providence...”
Petra: “Inv... what?”
156
It doesn't even merit any surprise from Subaru that his ace is a double-edged sword.
The problem here is how its uses are now limited further—all he can do is pray that this current
backfire resulted from using it in quick succession.
He at least can anticipate that counting on Invisible Providence for this fight will mean losing far
too much in exchange.
Petra: “Big Sis Frederica...”
Frederica: “It must have been frightening for you, Petra. You did well to not cry.”
Petra still clutches Subaru's sleeve when Frederica calls her. Frederica gives that appraisal of her
precious faux-sister's efforts while turning to face Subaru, her expression stern.
Frederica: “Subaru-sama, my apologies. I recognize that you desired for me to take Rem-sama and
flee the mansion... I've failed my task.”
Subaru: “No, it's hopeless it in this situation. And the outside's even worse than here... where's
Rem?”
Frederica: “I have her.”
Frederica holds nothing in her hands, both equipped with clawed cestus.
Subaru is anxious about Rem's apparent absence, when Frederica turns her back to face him. Firmly
secured there with ropes, carried on Frederica's back, is Rem.
She's bound securely, but that still makes way to an overwhelmingly surreal scene.
Subaru: “I know we're in an emergency, but it looks like Rem's neck'll snap if she's moved around
too much it's terrifying!”
Frederica: “Fortunately, would be a word I'd hesitate to use, but Rem-sama has been separated from
the regular flow of time. Being so, I find nothing apparently affecting her even despite some
somewhat rough treatment...”
Subaru: “E-even so try to treat her carefully as possible okay?”
It's the result of Frederica thinking to do the best she can.
Subaru doesn't want to complain about it when he doesn't have any alternative plans to offer. He
will have to have Rem endure through an uncomfortable experience for a little while.
But either way,
Subaru: “None of us can fight except Frederica. Me and Petra aren't battlers. Rem's asleep. Otto
fought his best, but for all his struggle he fruitlessly wound up...”
Otto: “Except I'm not dead!? Could you please not spin these terrifying tales while people are
dizzied from hitting their head!?”
Subaru looks down solemnly, which resuscitates Otto who lies tumbled on the floor in a corner of
the room.
157
He shakes his head and crawls over to the group, and trembles at the bisected door and
clotheshanger.
Otto: “Who would've thought that the spellstone would be shot down like that... it worked fine on
Garfiel.”
Subaru: “They've got different experience when it comes to fighting, and their brains are probably
made different. Don't compare them. It's sad.”
Frederica: “Garf... then he truly has been raised in the manner which he appears to have been. I was
not watching over him...”
Subaru puts a stop to Otto's cruel comparisons.
It seems like even Frederica has some thoughts about Garfiel after their ten-year reunion. She might
feel guilty that her eyes strayed from him and he grew up into a sort of a punk.
Leaving all that business aside and their fostering of brother-sister relations as something to do later,
Subaru: “Gotta do something to solve the problems at hand.”
Elsa: “Can I assume that you're about done with your pleasant chat?”
Subaru: “Sorry for making you wait. And how about you? Are you mentally ready for a five-versusone
beatdown?”
Elsa: “I'm afraid you're including three, or perhaps four stray children in your calculations?”
Elsa smiles faintly as she accurately counts the number of non-combatants.
The kukri in each of Elsa's hands sway as she easily hops off the bed. Watching this, Subaru
realises:
—No blood is dripping from Elsa's back any more.
Subaru: “But it looked like it'd been pretty deep?”
Elsa: “You mean my wound? Don't worry, it's fine. Look at what's happened already.”
With that, Elsa does a turn on the spot.
And just like Subaru suspected, the wound Frederica inflicted on Elsa's back is perfectly gone. The
clawmarks still remain gaping open on her clothes, so it wasn't that he'd imagined it.
Frederica is the first as everyone except Subaru swallows their breath, faces tense.
Conversely, Subaru just gives a deep sigh and curses his bad premonition for being correct.
Subaru: “I mean I knew killing you won't make you stay dead... but are you kidding, your wounds
heal too? You're basically just a monster.”
Elsa: “I don't remember ever discarding my humanity, and I have to have some contentions about
how you're saying this to a woman. Besides that, where could you have learned about my
characteristics?”
Subaru: “Anyone'd think something was up the second you weren't split in two by Reinhardt.”
158
Elsa: “I don't go through experiences like that one often. I almost did get split in half. —I wonder
what a hero's guts are like. It's extremely fascinating.”
Although having borne witness to such incredible combat strength, it doesn't seem Elsa has learned
her lesson.
It'd be fine for her to go around hounding Reinhardt, who feels like he wouldn't die even if you
killed him, so why is she so focused on constantly causing problems for Subaru's team?
He has too many bitter complaints and grievances with Roswaal than he can ever hope to voice.
Frederica: “Subaru-sama... her being present here would mean, Garf is...?”
Asks Frederica timidly, her expression stiff.
Having witnessed the abnormality of Elsa's constitution, she is anxious about her brother's absence.
But Subaru has no answer which can dispel Frederica's unease.
If there's anything he can tell her, it's,
Subaru: “Unfortunately, I can't explain why she's here either. But I seriously doubt Garfiel's been
beaten down in such a short timeframe.”
Frederica: “From what I witnessed, their strength seemed on even par... Garf had looked to hold a
slight advantage.”
Subaru: “That's how I see it too, but in the end we don't...”
...know, Subaru means to say as he glances toward Elsa, when his breathing freezes.
Following Subaru's gaze, Frederica looks over there as well and also holds her breath.
Elsa's brows furrow, perplexed, as she also looks at that same spot above her head.
It looks like the room's ceiling is sinking in—falling—and,
???: “Th'fuckin' cheek!!”
???: “Ee, eep!?”
Subaru: “That moron!!”
The instant they hear the ceiling breaking, Subaru and the others rush to the door.
Right after the five of them flood out the door, the ceiling collapses to crush the entirety of that
room, furniture groaning and wood snapping apart thunderously.
The explosive noise and the gale gust out the room, the aftermath of the destruction flowing down
the corridor.
Up billow plumes of white smoke. Subaru spits the gritty dust from his mouth as he tumbles down
the hallway to escape the scene. It seems that everyone has manage to avoid getting caught in the
collapse.
And from beyond the smoke,
???: “Don't yer pull none'v th's stupid crap! Now out'n'front we go!”
159
A familiar, uncouth voice shouts with fervour.
The battering of metal on metal and the noise of a blow follow the voice, until a silhouette cuts
through the smoke and tumbles into the hallway.
Subaru: “Uh, wha!?”
Seeing that tumbling silhouette, Subaru finds himself yelping in surprise.
Well of course. This figure is not the one he anticipated, and is instead a clawed furry quadrupedal
beast—with spotty fur, which looks much like a hyena.
But it is not the size of a hyena. It's huge, twice as big as Subaru.
Subaru does shudder for a moment at the arrival of the giant beast, but immediately notices that the
hyena's eyes are devoid of life, and the animal is dead. He looks to find that its neck bones are
broken, and may be bent into angles opposite of what they're meant to be.
Something possessing incredible power had obviously snapped the thing's neck.
And if we're to say that there's anyone in this mansion who could probably do that to the beast, it'd
be—
Garfiel: “Hey, Captain. Th'hell, y'were still inside?”
—Garfiel, who kicks the smoke away and coolly appears in the hall.
He notices Subaru and the others staring in astonishment at the dead hyena, and guffaws.
Garfiel: “Yer don't need t'freak out, 's all good. My amazin' self killed it.”
Subaru: “Right, thank you... or not! You stopped paying attention to her! And so I thought I was
gonna die! I was terrified! I thought I was dead!”
Garfiel: “Yeah yeah my bad, but my amazin' self wasn't thinkin' t'let her go fer an instant. Sh'ran off
while I was tangled up with th'pest.”
Subaru: “Pest which means?”
Garfiel's face twists bitterly as he clicks his fangs.
This pest he's talking about probably means the hyena. Going off the previous conversation, it
definitely has to be some kind of witchbeast but—and that's when:
???: “Geez! I can't believe this! Elsa! Elsa! Dooo somethingggg!”
Elsa: “I'd love to, but I'm sure you're the one who said 'leave this to me, go do something about the
others'. Though I'm happy to have more bellies to gut.”
Two female voices, one loud, one calm.
Instantly, the room that Garfiel crushed bursts once again, and again silhouettes cut through the
smoke to appear in the corridor.
Weighty footsteps, and light footsteps—with a size disparity so large you'd hesitate to call them
only two pairs.
Otto: “...What is that thing?”
160
Unable to keep silent any longer, Otto points at it and asks Subaru for an answer.
Subaru feels the cold, damp sweat oozing down his body.
Subaru: “From what I'm seeing, a biggish hippo.”
Otto: “Bigg'ish'?”
Subaru: “Yeah. 'Cause hippos are big anyway.”
If you took a hippo and tripled its size, it might manage to be this creature.
Black flesh, with a thick rocky hide. Its round eyes host a red gleam, wicked and hostile. Its mouth
is so large that it could probably eat Old Man Rom in one bite, with flat teeth like mortar stones.
It resembles a hippo at a glance, and is probably what you'd get if you tripled a hippo's wickedness
and ferocity.
???: “Spotty Rex's deaddd! He's deeeaaadd! Poor boy! It's awfuulll! Awfuulll!”
High-pitched sobs wail out from atop the giant hippo in mourning of the hyena's death.
The person riding the hippo, legs flailing everywhere, is a small girl. Her brown hair hangs in a
braid, and her features are rustically simple.
Her face is familiar to Subaru.
Subaru: “...From the witchbeast forest.”
Back when Subaru got caught up in the loop series at the mansion.
She's from when Subaru went into the deepest reaches of the forest to save the children from Arlam
Village. And she's the main reason that the children were lured into entering the forest.
Subaru had heard from Roswaal that she vanished after the whole affair was over, but,
Petra: “She's from back then!”
It seems that Petra has reached the same conclusion.
If Subaru had been the only one to notice it, then he might have discarded it as some kind of
misunderstanding on his part. But if Petra's memories are telling her the same thing, he has to
accept it.
This girl was involved with the witchbeast debacle.
With the current situation considered, that means that even that debacle was—
Subaru: “Roswaal's, plans!”
She's working with Elsa. So Roswaal was behind the witchbeast affair too?
Which means that the events in the Capital, the events in the mansion, all of everything was in
Roswaal's hands. All of Subaru's efforts had been in accord with a future dictated by a dark book of
prophecies.
Subaru: “Like I can accept something so stupid!”
161
Fate being fixed is a real no thanks.
At very least, it will start changing from now on. All this means is that he's put the witchbeast
debacle aside as another thing to interrogate Roswaal about, and that he has yet another reason to
smack that clown in the face.
Subaru blazes with rage and rebellion. The girl atop the hippo finally notices his gaze.
She blinks her round eyes and waves at Subaru.
Girl: “Oh, you're the guy from before. And Petra-chan's here too. It's been aaageeees.”
Subaru: “Y-you're sure not discouraged from talking. You do realise what this situation is?”
Subaru can't hide how the girl's unconcerned attitude catches him off.
She tilts her head at Subaru's blatant caution.
Girl: “I realise, I'm wooorkiiing. Mama'll scold me if I don't do my work. But then Elsa's there off
doing whatever she wants.”
Elsa: “Taking the rear post is tediously boring, it was a mistake to appoint me there. My methods
are far more vivid and fresh for enjoying life, compared to being made animal feed. Being killed by
me is the better choice for the victim too, correct?”
Elsa starts walking over to the hippo's side as she directs the conversation onto Subaru.
Subaru sighs, then raises his finger.
Subaru: “Okay, then I'll give you the coolest proposition ever. You take that knife you're holding
and flip it around. And then you plunge the thing into your stomach. After that you roll around on
the floor. Guts everywhere, I'm happy, you're happy. It's the seppuku challenge. Isn't it cool?”
Girl: “Pff! Ahahahaha! That's awesome! Come on, Elsa, wanna try it? Elsa, you like guts. It'll be
fun! I'm excited!”
Elsa: “Sorry, but I've already done that so many times after getting this constitution that I'm bored
of it.”
After learning that his super cool proposition has already been practised in reality, a super cool
shudder rushes down Subaru's spine.
Regardless, this doesn't change that they have two predicaments sitting in front of them.
Subaru: “I don't know how it works, but is it safe for me to think she's controlling the witchbeasts?”
Garfiel: “Doubt yer wrong. S'th'same f'th'ones outside, n'same f'that mutt, allv'm're doin' whatever
sh'says no fuckin' fuss at all. —What's the plan, Captain?”
Honestly, the situation has changed immensely from the initial plan. It's not just Elsa, they have
another foe—and it's someone who commands massive witchbeasts.
So long as there are beasts outside, it's going to be nigh impossible to escape the mansion
peacefully. And most importantly, Subaru's team has not yet assembled all of the people they need
to save.
162
Even if they take Frederica, Petra, and Rem to the village, it's not enough.
Subaru: “Garfiel... can I ask you to do something crazy?”
Garfiel: “Try me, Captain.”
Subaru: “I want you to stall Elsa and the girl simultaneously.”
Garfiel: “—”
Subaru knows that he's asking for something unreasonable.
Just Elsa alone is a foe who presents unparalleled difficulty. While Garfiel is keeping her put, he
also needs to keep the attention of the massive witchbeast.
Subaru has, since coming to this world, learned the threat witchbeasts present to a painful extent.
And so,
Garfiel: “No problem. Just leave it t'me. Gotten fired up now.”
Subaru: “—!? S-seriously? No kidding? You can do it?”
Garfiel: “'S what'm here for. Been talkin' some massive talk. Too late fer me t'start whinin' over
th'enemies bein' strong'r havin' numbers. 'S a THE MEEDAN WHO SHOULDERS THE MOUNTAIN
LOSES ANYWHERE TO RUN.”
With that, Garfiel clatters his shields together.
Even Subaru can tell that it's bravado, and not supported by any real self-confidence.
Regardless, Garfiel is the only one he can rely on for this.
Subaru: “Garfiel. I know I already said this countless times in the carriage, but...”
Garfiel: “I hear ya. My amazin' self got no ideas'v dyin' in this place either.” Garfiel
interrupts Subaru and eases him by pushing him forward with his shoulder.
He is indicating that there is no need to say anything else.
Repeating it would be inconsiderate toward Garfiel's resolve. So Subaru swallows his words and
returns a push to Garfiel's shoulder.
By that alone, he presses a dicey form of trust on Garfiel.
Garfiel: “Now get goin'. I ain't able t'get serious 'f yer gettin' in th'way.”
Garfiel bares his fangs as he speaks to the others.
Hearing it, Otto, Petra, and Frederica look at each other.
Otto: “Garfiel, don't die. I don't want to be zipping around cleaning Natsuki-san's messes by
myself.”
Frederica: “We truly have not spoken enough. But very well. We'll speak another time, with
Grandmother alongside us.”
163
Petra: “Y-you can do it, scary-looking man.”
Garfiel smiles wryly while nodding to the three.
Subaru feels like they just loaded a pile of death flags on him, but actually with how huge the pile is
it flips into a comforting life flag, is how Subaru rationalizes things in a bid to cling to hope.
Garfiel: “N' so, yer opponent from now on's my amazin' self. This time I ain't gettin' distracted and I
ain't lettin' yer flirt around. My claws n' fangs n' shield's're gonna beat yer into tears!”
Roars Garfiel as he sharply turns around.
Bathed directly in his aggression, Elsa smiles while the girl's mount give a low growl.
Elsa: “Mei Lee. Don't interfere this time.”
Mei: “But you're the one interfering, Elsa! I'm just doing what Mama saaaiiid tooo!”
While having their disagreement, Elsa and the girl attack Garfiel.
Garfiel braces himself as he catches the heavy blow on one shield and the sharp blow on the other,
sparks flying as Subaru runs away as fast as he can.
Subaru: “Otto! Frederica! Situation's changed! Since we can't leave the mansion out anywhere
proper, we'll escape from a different route so we don't get eaten by witchbeasts!”
Otto: “You say 'a different route', but I'm sure we'll be faced with the same outcome even should we
take a backdoor. If we can't have Garfiel supporting us for combat, what should we do?”
Subaru: “What if you do frantic witchbeast negotiations with your BLESSING OF XENOGLOSSY, and
depending how the bargaining goes they surrender the path and we escape? Here's your chance to
be the lead role.”
Otto: “Witchbeasts generally just say ME EAT YOU WHOLE, so it isn't really a conversation!”
It was a faint hope to begin with, and Otto looks miserable as he responds to it, running alongside
Subaru.
Yes, there exist people who you can speak with, but not communicate with. It seems that principle
works for both humans and animals. Elsa makes good proof of it.
Which means that there's only one escape path Subaru can think of left—
Frederica: “Subaru-sama. I have an idea for an escape route.”
Subaru: “I know, Frederica. It's probably the same place as what I'm gonna suggest. But...”
There's a problem with that route.
Just as Subaru goes to point out what it is, he dashes out the hallway and swallows his breath.
Subaru: “No matter where we run they just can't make it easy for us, fuck!”
—Before them, two hyenas notice their presence and come rushing to attack.
164
Though the cast of the Roswaal Mansion Battle has changed, the fight remains heated.
165
CHAPTER 126: ATTACK OF GUILTILAW, EBONY KING OF THE WOODLANDS!
—Sparks of steel on steel shriek and shriek in succession.
Garfiel: “Ghaaaaaaaahgr!”
Elsa: “Ahahaha! Wonderful, wonderful, wonderful!”
Her body dances through the air. Her blades elect for no fixed course as they slash for Garfiel's
vitals.
Who knows how she is capable of these moves. Every single casual-looking strike closes in with
deadly force and accuracy to imminently gouge into Garfiel.
Her crooked blade shreds through the air, transcending sound as it flies at sonic speed.
Garfiel redirects the blow upwards with his shields, defending himself by letting the strike slide
away rather than block it directly.
The force of the woman's slash remains lethal as she shifts merely the trajectory of her swing, her
body flowing adeptly aside. Cutting into that opening, Garfiel takes aim at the woman's open
stomach and swings up his leg.
Garfiel's kick is mighty as a cannonball, easily capable of demolishing walls of stone.
If it hits someone at full force, their fleshy human body will offer absolutely no defence as its
overwhelming strength exhibits destruction on their innards.
And Garfiel has, in fact, succeed in landing such blows to pulverise the woman's flesh and bone
more than a couple times now.
However,
Elsa: “I've seen this before.”
Garfiel: “Fuckin' fuck off!!”
The woman twists her open side and back away from the kick's trajectory. Garfiel's foot strokes
across the woman's back, merely grazing her, before tangling in her black cloak.
It's an instantaneous, but conceivably fatal lag for both the woman and Garfiel.
Elsa: “Hah—”
With a quick exhales, the woman reaches her arm around to her back, entangling the cape further
over Garfiel' legs. Her other hand darts up from behind, herself halfway through a backflip, racing
for Garfiel.
The swing will slice Garfiel's right thigh in two—before he can think, Garfiel hops with his free left
foot and jabs it directly beneath his entangled right.
Garfiel's left foot slams into the flat of the ascending blade.
Metal and wrist snap as the woman cries out sensually, dropping her knife. She does retreat, but
being that his leg remains entangled and he falls back to the floor, Garfiel cannot pursue her. He
uses the momentum from his kick and puts his hands to the ground to backflip away, opening
distance between them before disentangling his foot.
Garfiel: “Got yer wrist n' yer knife, haha.”
166
Elsa: “That's fine. I have spare knives, and my hand will be moving again before long. And my
cloak... it's practically just an impediment while fighting you.”
Garfiel: “Yer can keep yer bravado ter yerself.”
Elsa: “We'll check on your guts whether this is bravado.”
Garfiel uses the stolen cloak to wipe off his sweat and dumps it on the side of the hallway.
Elsa pays no mind to her cloak as she lightly touches her crooked left hand with her right, and calls
out to the massive silhouette behind her.
Elsa: “Mei Lee. Don't just watch, give me another knife.”
Mei: “Geez, just doing whatever you want, Elsa. I'm not your luggage girl or knife caddie. And you
keep fighting so Boulderpork can't cut in.”
The girl riding the massive witchbeast puffs out her cheeks in reply as she flings something to Elsa.
It's a holder for the knives Elsa uses. She draw two fresh kukri out of it, holding both of them in one
had as she feels out their grip. She looks up at the girl.
Elsa: “It's a blight on your own cuteness that you brought that giant witchbeast along. Though I'm
glad to dance with him without any nuisances involving themselves.”
Mei: “But it's gonna be ridiculous if you get caught up in that and let the mark get away. If mama
knew what you did, she'd totally scold you. I'm gonna tell her you were naughty, Elsa.”
Elsa: “If I were scared of scoldings, then I wouldn't start without you or steal your food. It's enough
for you and the others to be the good children. I personally don't mind being troublesome.”
While she speaks, Elsa tosses the two knives in the air and begins juggling with them one-handed.
The size and speed of the blades as they spin means that Elsa could lose an arm if she made a
mistake, but Elsa's risky manoeuvres end with one knife in her right hand, and one knife in her left.
Elsa: “My apologies for making you wait. It seemed like waiting would be enough to fix my hand.”
Garfiel: “Don't worry yerself 'bout it. My amazin' self's also lookin' t'buy time, and I ain't crass
enough t'butt into a talk b'tween sisters. Family talks're damn important.”
Elsa: “Goodness. Why do you believe that she and I are sisters?”
Garfiel: “'Cause yer callin' th'same goddamn lady yer mom? It don't matter that yer hair n'eye
colours're different. 'M talkin'bout bein' family nevermindin' yer blood.”
Hearing Garfiel's reasoning, Elsa's eyes shoot open for a second in surprise. She puts her hand to
her mouth, and slips a very cheery laugh.
Garfiel: “Eh?”
Elsa: “Huhu... ah, no, forgive me. I wasn't expecting that response, so I went just a little bit
167
funny. ...You truly do seem like a good boy.”
Garfiel: “Stop treatin' me like a kid. My amazin' self's n' amazin' man.”
Elsa: “Indeed? Although, it doesn't feel to me that you're fully a man or an adult.”
Elsa replies to the dissatisfied Garfiel with her cheeks still relaxed.
Garfiel's brows furrow in puzzlement, making Elsa's smile even more cheerful.
Mei: “Elsa Elsa. Don't you get the feeling this scary-looking guy's actually really precious?”
Elsa: “Yes, Mei Lee. I am beginning to get that feeling. I may have sighted for the first time in a
long while somebody who I'd rather keep alive after pulling out their guts.”
Garfiel: “Stop runnin' yer damn mouths. Yer both gonna be takin' a nap after eatin' my amazin'
fists.”
Garfiel sharply turns his wrists as he speaks.
He doesn't really understand Elsa and Mei Lee's conversation, but he can definitely tell that they're
slighting his determination.
Should Garfiel understand that, then he has no kind words to offer.
Unless they apologize in tears as they beg for forgiveness, Garfiel will pulverise them immobile,
and give them the punishment they deserve. —Such is Garfiel's duty.
Garfiel: “Bring it on already. Yer even buyin' even more damn time f'th'Captain'n'th'others t'get
away. And my amazin' self ain't hopin' t'be gettin' a gold star fer runnin' away. M'beatin' yer t'yer
last inch, teachin' yer a lesson. That my amazin' self's the strongest shield inside or outside
SANCTUARY.”
With that, Garfiel batters his shields together.
A screech rings down the hallway as Garfiel lobs his determination at the two enemies in the
moonlit corridor.
Mei: “—Pffhahaa! Elsa, did you hear that? He's the strongest shield! Strongest shield... pff. Pffhaha!
He is precious!”
However! The situation turns that Mei Lee laughs, of all things, and Elsa's smile also intensifies!
They do not seem to be threatened.
Garfiel: “Fuck're you laughin' at, huh?”
Mei: “Ahh, it's so funny. So funny I just laugh. You're funny too with how you think you're oh so
strong, but it's the group that ran who're also just so so funny.”
Garfiel: “Th'Captain's group's funny?”
Mei: “They so are. Aren't they? My pets are surrounding the mansion, so there's only one place to
go to escape. That's actually meant to be Elsa's post, but she went off acting on her own, so I put a
replacement there.”
168
Elsa: “—”
Mei Lee shots Elsa a criticising gaze. Elsa unabashedly pays it no heed.
Her murderous eyes stare at Garfiel, observing his every action, making it extraordinarily difficult
for him to move. And he also has to pay attention to Mei Lee's comment.
Mei Lee thumps the back of the witchbeast she's riding while Garfiel's gaze grows sharper.
Mei: “Except for Boulderpork, I brought one more huge pet with me today. He's blocking the path.
So when you buy time, it actually does the opposite of what you want.”
Garfiel goes silent.
Mei: “You think when you're done with me and Elsa, you're gonna catch up to the others and save
them but, you're really actually not. So when I see you doing your best to buy time without even
realising that, everything's just soo funny.”
Unable to keep herself from smiling, Mei Lee laughs at Garfiel's silliness.
Faced with her juvenile malice, Garfiel gives a deep sigh.
Indeed, there are many unstable requirements piling up on them. Mei Lee is correct, they are
definitely facing a situation which exceeded their plans.
However,
Garfiel: “Ha. Stupid bullshit.”
Mei: “...Huh?”
Garfiel: “Yer th'ones who ain't gettin' it. You got more monsters around? We're th'ones gettin'
pinned? As fuckin' if me or th'Captain'd let that fly.”
Enjoying the way that Mei Lee's smile disappears, Garfiel steps forwards.
He watches as Elsa reacts, stooping herself slightly forward, as he says:
Garfiel: “Th'Captain n' them beat th'shit outta me. —They're gonna snort laughin' so hard they blast
yer dumb obstacle right outta here!”
※ ※ ※ ※ ※ ※ ※ ※ ※ ※ ※
Subaru: “We'redoomedwe'redoomedwe'redoomedwe'redoomedwe'redoomedwe'resodoomed, what
is even happening anymore!?”
Utterly out of breath, Subaru whines as he dumps himself to the floor.
On the third floor of Roswaal Mansion's main wing, on the platform leading to the staircase to the
top floor, are assembled Subaru's group—Subaru, Otto, Frederica, Petra, and Rem, all holding their
breath as they stay put.
The fatigue is blatant on all of them as they sit there, with deepish wounds present on the whole
169
party.
But especially,
Subaru: “Are you alright, Frederica?”
Frederica: “...I am, this is merely trivial, it is not anything serious. Subaru-sama, I apologize to you
for demonstrating such fecklessness.”
Subaru: “We'd be getting nowhere without you. The pathetic ones here are us guys, me and Otto.
I'm sorry. We're weak.”
Otto: “T-this time alone... I lack any margin to refute your ribbing, Natsuki-san.”
Otto gives a frustrated sigh. Subaru spits the blood out from his mouth.
While ignoring the hideous pain across his whole body, Subaru readjusts Rem's position on his
back. —He has switched roles with Frederica, and is now tasked with carrying Rem.
Otto guides Petra by the hand while Subaru is shoulders Rem. Their only fighter, Frederica, stands
at the frontlines while opening a path—such has been the optimal plan for these five.
Right after parting with Garfiel, Subaru's group were attacked by two hyena witchbeasts.
Between Otto's spellstones and Frederica's fighting, they barely managed to repel the hyenas, but
they soon discovered many more witchbeasts placed throughout the mansion to torment them.
Batlike Blackwing Mice lurking in the hallway between the main and separate wing.
Hyenalike Spotted Rex wandering throughout the mansion, attacking whenever they could.
Possums that cast a net over the team after they entered a room, and swooped down the second they
let their guard down.
They had a particularly painful battle when dealing with a two-headed snake thick as Subaru's arm.
They managed to drive the Blackwings away with smoke, Frederica's claws bested the Rex, they
fled from the possums while having their rear ends chewed, Otto's frantic negotiations managed to
stall the snake, and Subaru took the opening to grapple the thing and have Frederica decapitate it
twofold—and now, they're here.
Subaru: “We're just, utterly... we lost because we had to split up with Garfiel...”
Otto: “Don't be so faint of heart. Now is about when Garfiel would be confidently shouting that
we'll succeed, so let's hold expectations at least equivalent to the ones that he's placed on us.”
Subaru: “With how dutiful you are, you really don't feel suited to being a merchant...”
Otto is looking the least dire of all of them, stamina-wise. Subaru gives him a wry smile, psychs
himself up, and gets to his feet.
The Rem on his back is, honestly, so light it's saddening. Subaru had heard that unconscious or
sleeping people were heavy to shoulder, but Rem alone isn't exhibiting that.
He can barely feel her weight or her warmth. Her very presence is dim. Her faint heartbeat and
respiration alone prove that she is alive as Subaru firmly corrects her position.
As if terrified that, even though this will surely not happen, he'll drop her and not notice.
Petra: “Big Sis Frederica...”
170
Frederica: “Do not worry, Petra. There's no need to look so anxious... we will reach our destination
very shortly.”
Frederica responds to Petra's nervous gaze with a hearty smile.
But Frederica's situation is not as optimistic as she is making it out to be. A hyena mauled her arm
during a fight, she is unable to lift her bleeding left arm, and her movements lack their usual lustre.
They cannot hope for her to fight at full strength, and need somewhere to immediately heal and rest.
Subaru: “Though yeah, we really are close to our destination.”
Mutters Subaru as he looks up the staircase—at the uppermost floor.
The team is trying to reach Roswaal's office. Of course they're aiming for the escape route there, the
bad road that Elsa had welcomed Elsa's invasion in all the loops previous.
When Subaru first lost his plan to flee outside mansion, he had bordered on discarding this route as
well—but after a conversation with Frederica, changed his mind.
It happened right after they left Garfiel and repelled the two hyenas.
Frederica: “There is a concealed passage in the Master's office which leads to the outside. Though
it, we may capably escape the mansion and flee to a cabin in the forest. Should we use it...”
Subaru: “Sorry, Frederica. It's not gonna be that easy. There's reserves posted in the hidden passage.
Since that's the path that woman got in here through.”
Frederica: “—”
Aware that he the situation is nigh hopeless, Subaru nonetheless reports this information.
Subaru has run into Elsa before while trying to check the hidden passage. Leaving aside whether
she entered through the route this loop, she at the very least does know the passage exists.
Subaru: “Going off what Elsa and that girl said... it sounds like they have other allies. Leaving aside
whether this 'mama' is actually their mother, considering how they look nothing alike... if they're
gonna post a rear guard, then they're gonna post someone at that passage.”
Of course they're going to block the path.
Witchbeasts are surrounding the mansion, and there's an enemy in the escape route too. They're
utterly trapped, and Subaru forces his brain to fire.
Things are desperate.
It's wretched that, in a situation where their escape route is ineffective, they can't use Beatrice's
help.
They wouldn't have to be agonizing about this if Subaru had succeeded in convincing Beatrice.
With her GATE CROSSING, escaping this place would be so simple that they wouldn't even need to
think about it.
171
Subaru: “...I'm so selfish.”
Subaru knows about Beatrice's anguish and the reason behind it, and he's still trying to cling to her
aid.
He can't get her help here because he failed to bring her outside, and that in itself proves that he
wasn't seeing her properly.
It's natural that she hate and eject him from the room.
Otto: “Natsuki-san.”
Petra: “Subaru.”
Perhaps thinking something about Subaru's expression as he broods, a tap come to his shoulder and
a tug comes to his arm.
He looks to find that the tap is from Otto on his right, and the tug is from Petra on his left. The two
each use their methods to bring Subaru back to reality, then realise that they did the same thing, and
scrunch up their faces.
Looking at the two of them, Subaru sighs, feeling saved.
Frederica: “Subaru-sama. I believe that we ought to choose that path nonetheless.”
Subaru raises his head. Frederica raises her finger.
Frederica: “As you have stated, it presently appears that we are trapped in a deadlock. Ferocious
witchbeasts are encircling the mansion, and the enemy is aware of our sole route of escape.
Ordinary thought would have it that we will be killed unavoidably...”
Subaru: “Yes, right. I think the same, so I've been wondering about whether we could at least find a
weak spot in the perimeter of witchbeasts, but...”
Frederica: “Incidentally, Subaru-sama. Where have you previously met that assailant woman?”
Interrupted by Frederica's low-voiced question, Subaru quietly holds his breath.
Unable to read her intentions in asking it, Subaru nods.
Subaru: “Yeah.”
Subaru: “She targeted Emilia in the Capital before. The Sword Saint just happened to show up there
and owing to that everyone got out fine. Though it'd be way too convenient to expect that hottie to
burst into the scene here, definitely.”
Frederica: “I, see. Your last encounter involved the present Sword Saint. No, regardless, that does
not matter. I do not wish to know the methods used previously to repel the woman, I would rather
like to know her personality.”
Subaru: “Her personality?”
Subaru tilts his head at Frederica's rather nebulous question.
Subaru: “I mean, her personality is she's the same weird fetishist that she looks like. She's the
GUTHUNTER, loves cutting open people's stomachs and checking out the insides. She's up there in
172
the worldwide rankings for danger.”
Frederica: “And judging by how she appeared to enjoy her confrontation with Garf, she would be
particularly fixated on doing the deed by her own hands... correct?”
Subaru: “Not like I know her, but yeah she's probably that kind of character. ...I don't see where
you're going with this?”
Frederica: “It is simple, Subaru-sama. —Unexpected events in this attack are occurring for the
enemy as well.”
A powerful assertion.
Subaru's eyes widen in surprise.
Frederica: “Witchbeasts presently encircle the mansion. The young girl who was also present is
likely a manipulator of witchbeasts... we shall perhaps call her a witchbeastmaster. The enemy's true
designs had been to assault the mansion whilst the witchbeast perimeter was in place, and attack
those of us inside, would be what it appears.”
Subaru: “What makes you think that?”
Frederica: “—The timing between the attacks from the beastmaster and the Guthunter are not
synchronized.”
For a moment, Subaru furrows his brows in thought. But he immediately realises what Frederica is
trying to say, and hits his fist to his palm.
Subaru: “That's it, so that's it! Fuck, why didn't I notice it? Yes, Frederica's got it right! With that
weirdo's personality, of course this'd happen!”
Otto: “Wh-what is it? I don't quite see how everything connects...”
Subaru kicks the floor in frustration and excitement. Otto looks somewhat nervous, but Subaru just
gives him a nod.
Subaru: “It's real simple, Otto. The witchbeast attack's actually meant to corner everyone in the
mansion. And when we're cornered, we can't run away like normal. So we head for the hidden
passage. —Is the natural course of events. Right?”
Otto: “That would be exactly the course we have followed, correct? But weren't we saying that the
enemy knows of the secret passage, and so we cannot use it?”
Subaru: “Exactly. The correct course of the attack is, we're cornered and run into the hidden escape
path, and that's where we all get killed by a waiting Elsa. That's their plan. ...But it's gone astray.
Elsa isn't in the passage right now.”
Otto: “—”
Why isn't she?
Considering Elsa's disposition, the answer's obvious.
173
Subaru: “Elsa didn't want to miss out on prey so she started moving on her fucking own. That's why
she's out of sync with the beastmaster. And it means she's not at the spot that she's meant to be
blocking. —So there's no one at the hidden passage!”
Frederica: “The original plans had been for the woman to lie in ambush in the passage.
Consequently, being that events are diverging from their plans, it is extraordinary unlikely that a
rear guard is presently occupying the passage. The enemy shall surely realise that the situation is
divergent from their plans should they be given time. Likelihood is steadily increasing that they
may send another individual into the passage.”
Petra: “So we gotta race there while no one's around!”
Following on from Subaru and Frederica's theories, Petra practically leaps as she gives the answer.
Subaru laughs as she puts her hand on Petra's head, and pats her auburn hair vigorously.
Subaru: “Full marks.”
Subaru: “With the information we have, this's what's most likely. Either way, it's a more hopeful
idea than breaking through the witchbeast perimeter outside. And worst case, we can at least check
what's happening with the office. ...Let's do it. This is the only way we're all getting out safe!”
—Ready for that plan, the team arrived to this sight outside the office.
Everyone is both physically and mentally exhausted. Regardless, the hope of reaching their goal
filled them with enough energy to move their incredibly wounded selves.
And now, that flicker of hope is—
Subaru: “...You have to be kidding.”
Mutters Subaru reflexively after reaching the top of the staircase and peeking into the hallway.
Otto pokes his head out above him, as does Petra below him, and all seeing the same thing, they
agree with Subaru in dumbstruck shock.
Frederica: “What has happened? Is the Master's office...?”
Frederica sits on the stairs behind them as she asks this of the three scouts. But going by their
reactions, she likely has surmised that the situation is looking bad.
Subaru stifles his footsteps as he turns around and says, rather anxiously,
Subaru: “There's a real nasty-looking one camping outside the fucking room.”
—To Subaru, it looks like the monster CHIMERA.
A lion-esque feline head, with the skinny body of a horse or a goat. Its long tail whips about like a
snake, and although it is smaller than the beastmaster's hippo mount, it's more than stupidly huge
enough to block the mansion's expansive hallway. A strange entity which looks to have burst out of
174
myth—with easily surmised prowess in combat.
Otto: “That... is the witchbeast GUILTILAW. I-It lives deep in woodlands thick with miasma,
something of the king of beasts... and now, in a human village... it isn't meant to be the kind of
witchbeast that you could possibly bring with you to a mansion...”
Subaru: “What're chances that we're misestimating, and it's actually a wimp? Like, it looks like that
but actually its personality's gentle and you just feed it katsuobushi and it's happy, or something...”
Otto: “I wouldn't know what katsuobushi is, but are you saying to approach it with food? It will
probably end in the beast chomping you in half.”
Otto's statement leads Subaru to think of how huge Guiltilaw's head is.
Indeed. With a mouth that big, Subaru is a two-bite meal.
Subaru: “No but transformed Garfiel's even bigger. Okay, let's go get him and compare sizes. If our
guy's bigger then that guy'll slink away dejected.”
Otto: “If we go back to summon him, then that woman will carve us to bits. You can stop being
funny, Natsuki-san. ...Have you thought of any ideas?”
Otto entertains Subaru's joking, but his gaze is expectant.
It's like he's expected Subaru to have come up with some idea over the span of that little exchange.
Thinking Otto the placer of quite ridiculous expectations, Subaru glances back to Frederica and
Petra,
Petra: “Subaru.”
Frederica: “Subaru-sama.”
And they're gazing at him with expectation too.
Subaru: “—Seriously, just what expectations are you putting on me?”
Giving a deep sigh, Subaru shivers at the weight of the huge expectations. He adjusts Rem's
position on his back, and closes his eyes.
What, presently, are their possible combat forces?
Frederica is injured and Otto has basically no magic. Neither Petra or Subaru are fighters, and they
are on the third floor of the mansion's main wing. There is no way they can call Garfiel up here, and
even thinking of getting Beatrice's help is a bust.
But that said, fighting while using everything available is the only technique Subaru's ever had.
Everyone's abilities, their capabilities, materials present, the opponent's situation, the requirements,
Subaru thinks of them all, considers them all, mulls over them all—and sighs.
Subaru: “When neither martial or magic forces're looking like they'll work... time to stake it all on
my unmatched knowledge from the 21st-century.”
※ ※ ※ ※ ※ ※ ※ ※ ※ ※ ※
175
The first thing to catch Guiltilaw's attention is a sound.
Guiltilaw: “—”
Having heard the peal of something hard tapping and tapping and tapping against the floor,
Guiltilaw raises his snout.
Silent King of the Woodlands. Some localities indeed refer to Guiltilaw as such, and unlike other
witchbeasts, he does not favour needless roars and pointless noise.
Contrary to his great frame and queer appearance, he soars deftly though the wastes, making not the
slightest sound in approaching his prey before landing a single fatal strike and slaying the creature.
Such sneaky and assassination-eqsue hunts are his greatest forte.
Thus, although his MASTER may have ordered it, Guiltilaw cannot see the hunt of lying in ambush in
one spot as anything but foolish utilization of his prowess.
Although naturally, he has not the slightest intention to be an ingrate and defy his MASTER's orders.
Because the breaking of his HORN allowed Guiltilaw to escape from his curse.
Guiltilaw: “—”
Guiltilaw casts his snout around, searching for the source of the sound while ruminating on his
MASTER's orders.
Remain in place outside this door, and hunt any enemies what may approach—such is the duty that
Guiltilaw has been ordered, and his MASTER's desire.
Tap tap tap. Those nigh defenceless sounds clearly are footsteps.
Many two-legged creatures, such as his master, make this sound when they walk. Among their
number are the truly strong, who do not even make such noise as footsteps, but the lord of these
footfalls is not that.
They are undefended, uncalculated, unintentional, unheeding—possessing not a speck of grace.
Guiltilaw finds them irritating to mangle even for a meal with how utterly weak they are.
Guiltilaw: “—”
Silently, Guiltilaw glides away from the door.
The footsteps are coming from the western staircase, the direction from which he has heard
intermittent sounds of battle for some time now.
Guiltilaw knows that his MASTER has brought in accompaniment with other witchbeasts. While
instructing many beasts inferior to him in strength and size to surround the mansion, his MASTER
tasked Guiltilaw with defending the door, mounted herself upon a large and dimwitted beast, and
went hunting.
It did dissatisfy Guiltilaw that she chose that merely-size beast for her hunt and left him behind to
guard the rear. But should the foes he face here at least be powerful ones, then he can both agree
with his reason for being brought here, and preserve his honour.
Thus, Guiltilaw did not do anything so foolish as leave his post to attack the enemies, no matter
176
what beasts they faced, until they managed to reach this very spot.
A weakling who could not even reach Guiltilaw's location did not merit battle.
A weakling butchered by beasts weaker than himself did not merit the hunt.
However. They prey has overcome the other witchbeasts, and arrived at this spot. The second that
Guiltilaw sensed their presence, he felt secretly thrilled.
—And this is what he has been waiting for?
Something fragile, ignorant of what it is to even hide footsteps, with such weak lust for battle.
One swing of his claws, one flourish of his fangs, would scatter this fleeting, inferior being to bits.
Guiltilaw: “—”
What surges inside him is rage. Only rage.
His fangs will ravage the prey, and without a single lump of their flesh going down his gullet, he
will leave them strewn about the floor.
That is the only thing that will assuage this burning feeling of insult.
Pursuing the footsteps, Guiltilaw moves without casting any shadow over the moonlight. Should
there be anyone to witness him as his great frame glides silently in motion, they would surely think
themselves observing a nightmare.
The ebony assassin approaches the footsteps, finding that the prey seems to have stopped at the next
bend—Guiltlaw draws his claws to bisect the prey from behind.
Guiltilaw: “—!”
With not the slightest sound, Guiltilaw stretches out his neck and bounds for the prey's back—
however.
Guiltilaw: “—?”
The prey that he caught, and sensed had been within mauling range, is nowhere to be seen.
Unsure of where to swing his upraised paw, Guiltilaw stalls for a millisecond, feeling something
awry. He sniffs as he turns his head.
Where has the foolish, frail, flimsy prey gone?
Guiltilaw: “—!”
Once again, the noise of footfalls strikes Guiltilaw's ears.
He lowers his head and looks toward the noise, to find that it seems to be echoing from the stairway.
The noise of the prey's footsteps, descending, running down the staircase.
It appears they they have noticed his presence and somewhat accelerated to avoid him. But should
Guiltilaw learn of such a thing, then he shall never allow the prey to flee.
Guiltilaw turns his head. Looks at the door that his MASTER ordered him to protect.
He may be distancing himself from his post, but this prey is surely the exact prey that his MASTER
ordered him for. Should he slaughter the prey, that is tantamount to observing his MASTER's orders.
With that decision, Guiltilaw pursues the gracelessly fleeing prey.
177
He is effectively teaching the prey that the moment they turned their back on him—nevermind that
they were within range of his strikes—they lost any means of resistance.
For Guiltilaw, who dashed over mountains and reigned over the woodlands as King, the hunt of
fleeing prey was an everyday act of amusement.
The only prey worthy of being absorbed into this flesh were the truly strong.
Prey that turned their backs and lost their fangs to resist him merely existed so that he would not
forget the feeling of blood and gore on his claws and fangs—and they ought to learn this too.
Guiltilaw descends the staircase, following the footsteps.
He kicks off the wall at the stairway landing, dancing through the air to the floor below. He reaches
the second floor, then the first floor in pursuit of his prey, and now stands in the lowest floor of the
building.
He perceives the distant signs of fighting.
The scent of his MASTER, and the stench of the annoying dimwitted beast accompanying her. The
remaining scents are blood and steel, the aroma of the strong.
Guiltilaw: “—”
Were it possible for him, he would prefer to venture in that direction, and participate in the fight.
He wishes to brandish his claws and fangs in presence of his MASTER, ripping the strong fighter to
pieces and drowning them in a sea of blood, supping upon the taste of victory.
However. He must not desire such a thing right now. He has orders to uphold.
—Should he swiftly hunt this prey down, perhaps his participation shall be permitted.
Guiltilaw: “—ϡ”
Guiltilaw feels the burning in his fangs ever more keenly, his body shuddering.
Again he hears the footsteps, and pursues them to hear a door shut further down the dark hallway
before looking at the door, freshly closed.
Darting over, standing silently before the door, Guiltilaw uses his long tail to dexterously open the
portal.
This is not his first time invading the dwelling of the two-legged creatures and brandishing his
fangs.
He understands the framework of these 'doors', squeezing his massive frame through the doorway as
he sneaks into the room. He had been expecting the prey to be waiting here at this very moment, but
he cannot find the slightest glimpse of them, and yet again Guiltilaw suffers utter surprise.
But his disappointment this time does not hide far away.
Guiltilaw: “—”
Turning his head, Guiltilaw's gaze lands on a corner of the room—on the wardrobe.
Sticking out from the crack between the wardrobe's two doors is fabric from the prey's
overgarments. They swooped inside in a panic, and their clothes were caught there. The shallowness
of this prey, believing that they are hiding from Guiltilaw while failing to realise that, is humourous.
Guiltilaw silences his footsteps. Creeps near the wardrobe.
178
He raises his tail, sharpens its tip, and hesitates for not even a second.
Guiltilaw: “—!”
His tail pistons, pierces easily through the wardrobe like a spear.
It leaves a round hole as if made by a drill—and many more of them, coin-sized holes stabbing one
after another into the wardrobe, skewering the pathetic prey what cowers inside.
When more than twenty holes litter the wardrobe, Guiltilaw ceases attacking with his tail.
He reaches out his front paw and yanks the wardrobe door so that he may observe the pathetic, dead
prey. The perforated door opens easily, and the prey inside—
Guiltilaw: “—Grawh!?”
The instant Guiltilaw goes to confirm the corpse's presence, a burning shock to his nose makes him
recoil.
A terribly intense stench shoots through his nostrils, the sensation so painful he could wail. He
promptly looks back at the wardrobe, to find a transparent bottle, broken and overflowing with
colourless liquid.
The stench is coming from this substance. And the prey is not inside the wardrobe.
The protruding cloth had merely been clothes protruding from the wardrobe.
Guiltilaw: “—!”
Once again hearing footsteps peal from the hall outside the room, Guiltilaw turns around.
His nose is not working, but his eyes and ears are fine. He spots a shadow dash down the corridor,
and while lamenting the insult of his disabled nose, pursues the shadow.
Guiltilaw has never faced such humiliation in his life.
This is not a bold and honest confrontation against Guiltilaw, who has overwhelmed all enemies he
has ever faced, nor is it him easily sinking his fangs into fleeing prey. This is an entity scrambling
so horrendously for life of a wretched likes Guiltilaw has never seen before.
Assuredly, kill them. Slay them. Maul them, splay them over the dirt, trample them.
Guiltilaw: “—”
Forgetting to even silence his footsteps, Guiltilaw's massive frame soars into the room where the
footfalls fled.
He easily blasts through the twin doors. What welcomes him is a room remarkably larger than the
others he has seen.
A large table stands in the middle of the room, and in the back of the room is a hearth.
Candlesticks sit lit upon the table's white tablecloth. In a room with the moon as the only source of
light, the flames flicker bewitchingly.
Guiltilaw: “—”
Fire is an irritating thing for Guiltilaw.
Even during day, when the great globe of white fire remains in the skies overhead, Guiltilaw detests
fire being near him. After all, the forest that Guiltilaw lived him was engulfed in flames, and he lost
179
his peaceful home. His horn was broken and he began obeying his MASTER during that affair as
well, so fire prompts memories of both liberation and humiliation for Guiltilaw.
Guiltilaw: “—”
He hears no footsteps. But he does hear something else.
Opposite the door he just came through is yet another door, on the other end of the large room.
From that likely-cramped space beyond the door, he senses something.
Guiltilaw sniffs, but his sense of smell has not returned yet.
He cannot smell the aroma of the prey wetting itself in terror. When he mauls the prey, he likely will
be unable to smell or taste its blood either, which is a disappointment.
But he can put those sensations off for another time, so long as he succeeds in slaughtering the prey.
Right now, only erasing this sense of humiliation blazing in his chest, and making the prey who
disgraced him shriek its death wail, will offer Guiltilaw any solace.
Guiltilaw: “—”
Guiltilaw steps forth, heading straight for the room.
Then he stabs his sharp tail into the room's door. It fills with holes just like the wardrobe did, and
Guiltilaw pulls the door open before taking a breath and leaping inside.
Guiltilaw: “—σσσ!!”
He soars into the room, roaring.
His bellow intimidates the prey, scares the weakling so that it may compensate him with his claws
and fangs into its flesh.
He whips his tail about, spreading destruction throughout the room, when dust erupts from shredded
bags and boxes sitting on the cupboards. His forepaw slams down on the floor, shattering it and
shredding through the cloth draped across the ground for dust to erupt yet again, from below—but
no. These plumes of dust thick enough to block out Guiltilaw's vision are only growing thicker.
Guiltilaw: “—!?”
Guiltilaw's vision drowns in white, which invades his windpipe the second he takes a breath,
making him cough. Some kind of, massive quantity of flour is dancing through the air.
Enough flour to rob him of his vision, and even rob him of the breath needed to roar.
???: “Got him!”
Someone, some creature, speaks.
Guiltilaw hears their voice not from inside this room, but the previous one,
???: “Eat this, the soul of science—flour explosion!!”
With a sound, something is hurled into the white-choked room.
The bright, flickering thing is one of the candlesticks from the table in the previous room.
The candlestick strikes the wall, its flickering flame falling the floor and blooming larger for an
instant.
180
Guiltilaw: “—”
???: “H-huh...?”
But that's all.
The candlestick remains fallen to the floor, doing nothing in particular. The speaker sounds to have
misunderstood something, and Guiltilaw knows that they are standing petrified outside the room.
Guiltilaw: “—ϡ!”
Guiltilaw's instincts tell him that he is never getting this opportunity again.
Some breed of insufficiency has happened for the enemy. And if that insufficiency had not
happened, Guiltilaw would have been in danger.
Comprehending this, Guiltilaw twists his body, electing to escape from this room.
If he can exit to a spacious room, a place where he can swing his paws and his tail freely, no plans
the prey come up with will present any issue. He'll use the overwhelming disparity in strength to
force them to submit, and wrest victory.
There's no need to do anything more than that—.
???: “Yes, didn't I tell you? That instead of doing that nonsense thing!”
???: “It's quicker to just do this!”
The instant that Guiltilaw thinks to soar out of the room, he hears two more prey speak.
A low voice, and a high voice. The moment that he realises these are prey of different sexes,
Guiltilaw senses that the shelf behind him is collapsing toward him.
The string drawn across the entryway is connected to the leg of the shelf.
Forcefully tugged, the shelf collapses onto Guiltilaw's back. But its size only allows it to hit
Guiltilaw's massive behind.
The force the blow carries inflicts damage on Guiltilaw equivalent to zero.
Calmly taking the blow, Guiltilaw severs the string with his claws.
And when he prepares to definitely leap out of the room—
Guiltilaw: “—?”
The cupboard opens, and the liquid overflowing from it streams all over Guiltilaw's body.
It feels slimy, unlike water. Its colour is slightly yellow, and having it slathered over his prided
black coat is hideously unpleasant for Guiltilaw.
But that discomfort disappears instantly.
Guiltilaw: “—!?”
???: “Here is Otto Swein's personal investment of trading oil—take as much as you want!”
The prey's voice calls from outside the room.
But Guiltilaw has no leeway to mind the weak prey's voice in that moment.
181
—The oil he is covered in catches on fire, and detested flame burns his body whole.
Guiltilaw: “—ϡ!!”
The King of Beasts, descended from the plains and forever obsessed about his throne in the
woodland skies, without ever knowing what bested him, combusts in flames as hot as his
humiliation.
4
4 Tappei A/N: Guiltilaw-san, flubber of debuts.
182
CHAPTER 127: THE FINAL DAY OF ROSWAAL MANSION
Subaru: “Otto, you mentioned this, right. Something about using wind and water magic to make
footsteps peal from far away.”
Otto: “...Actually I believe that we did talk about that before, but it impresses me that you
remembered. Magic that simple isn't impossible for me even with my currently impoverished mana,
but... how would I use it? The only time I ever use it is when I want someone to turn around for a
moment.”
Subaru: “We'll be using it exactly how you said. You make footsteps peal, pull their attention, and
guide them into a trap. —Then I blast them away with the soul of science.”
Otto: “You sound absurdly confident about this, though what exactly is this 'soul of science'...?”
Subaru: “Simple, strong, certain death: a dust explosion. The methods and materials are simple as
hey presto. All you need's some fire and flour. If it's powerful as I know it is, it's gonna be more
than enough to blast away just one single monster.”
※ ※ ※ ※ ※ ※ ※ ※ ※ ※ ※
Otto: “...Is what you said, then I believed you and assisted you in it, and this is what happens!”
Subaru: “Shut up! Scientific advancement always comes with sacrifices! Why didn't it work!? There
wasn't enough flour, or not enough fire, or... are the laws of physics just different in this world? So
that's why the dust explosion didn't...”
Petra: “Auughh! None of that even matters, focus on getting it out! Ahh, oh no! Oh no!”
Petra butts in, screaming, into Subaru and Otto's yelling match.
The three of them are in the kitchen on the first floor, lit by the glow of blazing flame. Because,
Subaru: “You used too much oil! How're we gonna put this out!? It's spreading!”
Otto: “Do you think it's possible to shirk on oil when hunting such a ludicrously huge monster!?
And if we couldn't bring the flammables out and simply left them there, the results would be the
same anyway! You are definitely paying the fees for this afterwards!”
Petra: “Just stop it, you guys! This isn't the time for this! We can't put it out! Run!”
Subaru: “You sound like a middle schooler failing to recover from a mishap with fireworks...”
Says Subaru, exasperated, when he notices that the tablecloth in his hands has caught alight. The
flames don't go out no matter how he bats at them, so he resignedly dumps the cloth into the fire.
The fire from the storage pantry has spread within an instant, and the flames have started circling
around to the dining room and kitchen as well. It feels like the spellstones they use for cooking will
get caught in the blaze and explode at any second.
183
Subaru: “We sacrificed way too much for this...”
Says Subaru, frowning, as he looks down at the charred corpse fallen at the threshold between the
pantry and the dining room. It's the beast that was blocking the door to the office on the third floor,
which Otto lured downstairs with his sneaky magic, then got covered in the storeroom oil and
burned to death.
It had brains befitting its brawn and graciously triggered every single trap without suspecting a
thing. Fortunately it was seemingly susceptible to fire, falling into a panicked frenzy when it caught
alight, and proceeded to burn up without doing anything else.
Subaru did face a conundrum when his dust explosion failed, but Otto and Petra's backup plan of
using oil led them to victory.
For once you could say that Otto and Petra's failure to understand Subaru's lectures on the terror of
dust explosions, and dimwitted insistence to lay down insurance, saved them.
But if we're to mention problems that arose from it, then it'd be that the flames that killed the
witchbeast have, even after felling the beast, neglected to go out.
The fire burns the walls of the mansion, burns the food inside the pantry, tongues of flame reaching
to the legs of the dining room table.
It reeks of smoke, of a fatal and burning world. Subaru's vision begins to haze. In this land without
fire brigades, they are lacking in enough water magicians to put out the fire.
Subaru: “I know that we needed to do this, considering how Garfiel and Elsa're fighting and
witchbeasts are prowling around... but it's so big we'd have to reconstruct the building...”
Otto: “This isn't the time to be discussing it, Natsuki-san. We'll follow Frederica and escape.
Swiftly, before the third floor staircase stops existing.”
Petra: “Hurry! Hurry!”
It all feels unreal to Subaru as he watches flames engulf the familiar scenery, when Petra and Otto
tug at his sleeve.
Otto and Petra are the only people here except Subaru. Frederica and Rem split up with them when
they began their plans to trap the witchbeast, and have also been tasked with judging when the beast
moved away from the door, and then securing the hidden passage in the office.
It did worry Subaru to entrust the task to Rem and wounded Frederica, but thinking about pure
combat ability, it's a sensible plan. Even when Frederica's unable to use an arm, she is far more than
capable of defeating Subaru and Otto.
Either way, they succeed in repelling the witchbeast.
While praying that their reading is correct and no other enemies are in the passage, Subaru's team
burst out of the dining hall and sprint up the stairway, aiming for the top floor.
Subaru: “What do we do if Garfiel dies in the fire!?”
Otto: “Garfiel surely isn't so stupid, he'll be well! And it's possible for him to escape by charging
through the witchbeasts outside!”
Subaru is anxious about the fire's spread, and how it chips away the battlefield for Garfiel. Otto's
184
shouts are correct, but seriously what if—
Petra: “Big Sis Frederica!”
While Subaru broods, the three reach the third floor.
Out of breath, Petra sights Frederica standing outside the office and waves to her. Frederica seems
to perceive that the group's fight was successful, and instantly looks relived.
Frederica: “Thank goodness, you're safe. It comforts me that nobody is missing.”
Otto: “Please excuse me, may I ask why you are saying this while staring at me? Do you mean that
I seem probable to go missing? Please stop, I'm near to weeping!”
Subaru: “Yeah yeah, just calm down calm down. We'll put improving your reception aside as an
issue for later, and for now think about how to deal with our current problems. Frederica, how's the
passage?”
Frederica: “It operated without any issue. And I have confirmed that the path itself is also safe, at
least as far as the inner room... incidentally, am I simply imagining this smell of something
burning?”
Frederica narrows her eyes as she asks about the stench. Subaru grimaces, looks at Otto and Petra,
and the two shake their heads.
Subaru: “Ahm, well we kinda made a couple mistakes, and the fire we used for defeating the
monster got really huge. And so...”
Frederica: “The mansion has begun to burn. ...I had not anticipated that the building would return to
a state of complete normalcy, but now it shall burn down entirely. ...It's no comparison to our lives.”
Subaru: “Oh, you get it. Yup. Yup it's an inevitable sacrifice.”
Frederica: “I have little sentimental connection to this mansion. Instead, Ram's sentiment for the
building is likely strong, so you would best prepare yourself for a scolding afterwards.”
Subaru: “Wheuhghh...”
Imagining the relentless and endless chastisement, Subaru suddenly feels trepidation for their
reunion.
But it's good that he can think about the future like this. Frederica smiles wryly at Subaru's attitude,
and a relaxed atmosphere spreads across the scene.
Subaru: “Now, we just imposed another time limit on ourselves, so let's get out of here quick.
Frederica'll take the lead, then Petra then Otto. If you hit a safe zone the second you're out of the
passage... hard to tell what side of the barrier you'll be on, but either way follow Frederica's
instructions. Best plan is to meet up with the villagers who fled with Patrasche if you can.”
Calling an end to the jokes, Subaru quickly explains what their current direction is.
Frederica and Otto's expressions tense as they nod in response. But Petra furrows her brows.
She raises her little hand and calls,
185
Petra: “Subaru?”
Petra: “I-isn't this kinda funny? It almost sounds like you're not coming with us...”
Subaru: “—It does. I'm sorry, but I'm not leaving with you. We're splitting up.”
Petra: “Why!?”
Cries Petra in surprise.
She reaches out and grabs his sleeve, her fingers shaking, trying to keep him from going.
Petra: “Let's just run! The mansion's burning, and there's so many scary monsters! You can't beat
them in a fight, can you, Subaru? So won't you run?”
Subaru: “Well you're right so I have no excuses there, but I'm not gonna fight. Though I guess in a
sense, it is a battle.”
While happy for Petra's concern, Subaru gently unhooks her fingers. He sees the grief permeate her
big, round eyes, paining his heart.
Otto taps her shoulders from behind, taking care not to startle her.
Otto: “Petra-chan. Natsuki-san has something that he needs to do. Until he's done it, he cannot leave
the mansion.”
Petra: “But! Subaru's weak! He's in danger! We should just leave you behind instead, Otto-san!”
Otto: “You're not saying that because you believe in my strength at all, are you!?”
Shaking her head, Petra looks up at Subaru with tears in her eyes. Subaru kneels down to get on
Petra's eye level and pats her head.
Subaru: “I'm sorry, Petra. You, and Rem, and Frederica will all escape the mansion safely. But that
still isn't the entire rationale for why I came back to the mansion. There's still one more person I
have to get out of here.”
Petra: “B-Beatrice, sama?”
Subaru: “Yes. Have you met her?”
Petra shakes her head.
Petra started working here about ten days ago. She has not caught sight of that shut-in girl even
once during her time living here. Beatrice is indeed a hardcore shut-in.
Even though Subaru basically never left his room except to go to the bathroom either.
Petra: “I-is she really around? You aren't just thinking too hard, and fooling yourself that she...?”
Though she probably is not intending to, Petra begins doubting reality.
Could it be that this person only exists inside your own head? Is what she's asking.
186
Subaru: “She's an absolute pain, lonely but a complete meddler, takes everything upon herself and
answers questions all on her own and suffers for it, can't settle issues on her own so she wants
someone else to end it for her.”
Petra says nothing.
Subaru: “I'd really rather not think that my imagination could come up with someone like this. If
I'm gonna fantasize about anyone, it's gonna be a helper character who's with their fondness gauge
at maximum.”
Beatrice would never once do a single thing that Subaru wanted, didn't know what either she or
others desired, was trying to give up on thinking, and was the pinnacle of nuisancehood.
And so Subaru needs to teach her.
Subaru: “You know, Petra. Beatrice is basically the same age as you. And with how you're mature in
lots of ways, you might resemble her first friend.”
Petra: “Her first friend?”
Subaru reminisces on the past Theta mentioned.
Thinks about Lewes Meyer, Beatrice's old friend, who left a permanent scar on the girl's heart.
Beatrice and Lewes may not have recognized it themselves, but from an outside perspective, they
were obviously friends.
Subaru: “Petra. Once I come back with Beatrice, definitely be her friend. You'll like her. 'Cause it's
so fun teasing her.”
Petra: “Even more than Otto-san?”
Subaru: “Yeah. You don't even need Otto any more.”
Otto looks like he wants to say something, but Subaru consciously ignores him.
He draws his hand away from Petra's head and stands up.
Subaru: “I'm doing it. I'm searching for Beatrice. I'll do my best not to die in the fire, but if I do
burn to death then I want it to go down in the records that I died because of Otto's oil.”
Otto: “I'd really rather that not happen. If you don't come back safely I'll slap you, I swear.”
Says Otto, looking miffed, as he sets his hands on Petra's shoulders and draws her near him.
As if drawing a line between Subaru, and the four of them.
Subaru: “Frederica. I'm counting on you.”
Frederica: “Unsparing to my health, I swear that I shall cut open a path to our escape.”
Subaru: “Be sparing. If we can't keep you, it was pointless for me to come here.”
Frederica's eyes widen.
It's not often that Subaru sees her looking so surprised. Feels kind of nice.
187
Finally, Subaru looks at Rem, on Frederica's back. The sleeping princess shows no signs of seeing
Subaru off.
It's fine. Rem isn't meant to be seeing Subaru off. Subaru is meant to be greeting her.
Petra: “Take care, Subaru!”
Turning his back to the four, Subaru breaks into a run.
Even at their parting, Petra's voice washes over Subaru's back. But he doesn't glance behind him.
Petra would not desire him to, either.
The flames are spreading steadily across the mansion.
—With his hand to an unaffected door, Subaru must wonder whether this fire will reach the
Forbidden Archive.
※ ※ ※ ※ ※ ※ ※ ※ ※ ※ ※
The shield catches the blade as it slashes down, and to a screech of sparks and metal, the knife
flows away.
Weaving into each other's openings, a forceful kick plunges into Elsa's stomach—she takes the
blow, rotating to dissipate the strike's force, and uses her momentum to slash at Garfiel, her blade
closing in to slice his head in two. But,
Garfiel: “Lax!”
Elsa: “Goodness. How harsh.”
Garfiel's wide, open jaws close down on the blade, making this the fourth mouth-intercept of the
day.
The force of Garfiel's jaw instantly shatters the knife, and Elsa draws her hand back before leaping
backwards in retreat. The theft of her favoured weapon makes her smile deeper.
Elsa: “If you were wrong by even a hair, your head would have shot off. It's certainly impressive
that you did it.”
Garfiel: “Got th'trick t'it down. 'M startin' t'get bored 'v how you fight, 'bout now.”
Elsa: “How cold. Looking like you understand a woman's entirety, when you've only known her a
short while.”
Garfiel: “...Fuck off with that embroilin' phrasin', oi. —Hrn.”
Garfiel sticks his finger in his ear, grimacing, and sniffs as he notices something.
He looks down the hallway. His mouth curves into a grin.
It doesn't look like Elsa's noticed it yet, but Garfiel's sense of smell has picked up the stench. This is
the stink of stone and wood on fire—otherwise said, the aroma of flame.
188
Mei: “—Ahh, geez, I can't believe it! He's sooo useeeleessss!”
Right after Garfiel smiles, the girl atop the witchbeast puffs out her cheeks.
Elsa glances at her. Mei Lee remains peeved as she continues,
Mei: “Apparently the Shadowlion who's meant to be stalling the others just died. He never listened
to my instructions anyway, and he got mad real quickly so he was always a problem, but... how did
he manage to die when aaallll he had to do was nap outside a door?”
Elsa: “The true question is, why did you bring such a useless beast with you?”
Mei: “The Shadowlion was the only one except Boulderpork who wasn't in rut or hibernation. And
he still died, I can't believe it.”
Groans Mei Lee as she tosses another knife to Elsa. Elsa recieves it, confirms the feel of its grip,
and remains utterly apathetic this information from Mei Lee.
It doesn't look like Mei Lee cares at all about the dead witchbeast either. The poor creature.
Regardless. What he's overheard makes a wicked smile arise on Garfiel's face.
Mei: “Eww. Scary-looking precious guy, you're making a real nasty face.”
Garfiel: “My mug's nastiness ain't a match fer th'Captain's. N'anyway, ain't it 'xactly what I told ya?
Yer sneaky plots ain't nothin' t'th'Captain n' his happy band'v friends.”
Elsa: “While yes, they have exceeded our expectations... where does that leave them now? The
slaughter of one useless witchbeast doesn't change that we still have numbers. We continue to keep
you, their pivotal combat force, pinned here... and nothing especially changes about their
predicament.”
Garfiel: “Yeah, yer right.”
Elsa holds her two knives loosely while Garfiel crosses his arms.
He sniffs again, thinks back on his fight with Elsa until now—and decides.
Garfiel: “'S'bout time fer things t'get movin'.”
Elsa: “What do you—”
Mei: “Elsa!”
Garfiel's statement makes Elsa raise her brows. But before she can finish her question, Mei Lee
cries out.
Garfiel looks to find that the Boulderswine's eyes have changed colour, and the giant animal is so
agitated that it's stomping around on the spot. Mei Lee calls out to the creature, getting it slowly
back under control. But it seems like the witchbeast has, just like Garfiel, noticed the fire.
Mei Lee pats the Boulderswine to calm it down, then looks gravely at Elsa.
Mei: “Elsa, the building's burning. Somebody set it on fire.”
189
Elsa: “—”
Garfiel: “Hell're you sayin' with that 'somebody'. —'S was obviously th'Captain. Makes sense, n'
good that it's so upfront. Witchbeasts're beasts. If yer gonna drive 'em away t' make a path, quickest
way's t'scare 'em with fire.”
Mei: “But... then he came to the mansion to save the people inside, only to burn it down in his
escape?”
The decisiveness of Subaru's actions stuns Mei Lee speechless. Elsa also looks to be having trouble
consolidating this information, perhaps because it doesn't fit with her image of Subaru.
But Garfiel's heart remains horribly calm in contrast to their surprise.
Naturally, Subaru had not told Garfiel beforehand that he would go this far. Garfiel did believe
Subaru someone who took daring actions, but not even he expected that he'd burn down the
mansion. Which makes Garfiel feel comfortable as someone who decided to enter under Subaru's
tutelage.
And most importantly, the fact that this situation has been arranged lights a spark in Garfiel.
Garfiel: “Mansion's burning. Outside's a horde of witchbeasts.”
Elsa: “—?”
Garfiel: “Got people we gotta save, n'adversaries we gotta stall. Th'only guy who can fight's me, n'
th'Captain told me he's leavin' this up t'me.”
Mei: “What're you suddenly going on about, Mister...”
Garfiel: “'S goddamn obvious.”
Elsa tilts her head. Mei Lee looks like she's observing something creepy.
Garfiel clicks his fangs, feeling refreshed.
His body is light. Nothing scares him any more.
Garfiel: “With all these conditions in place, what fuckin' man out there ain't gonna get fired up!? M'
goddamn goin' for it. 'S a FACING THE DRAGON, SWORD SAINT REID LAUGHS AND DRAWS BLADE.”
Elsa: “You recognize that that saying means someone abnormal and insane?”
Garfiel: “Y'bet I know. And? Yer sayin' there somethin' wrong 'bout my amazin' self n' you bein'
here?”
Garfiel affirms his own stupidity with a refreshing breed of momentum, leading Elsa to stare in
utter astonishment. But only for a moment.
She immediately grins, licking her lips as her eyes soften beautifully.
Elsa: “You are correct. You are sincerely correct. You've stated it perfectly.”
190
Agreeing with him, Elsa points the knives she wields at Garfiel.
She crosses her blades, her long, black hair dancing as she tilts her head.
Elsa: “But would you mind if we had a change in attitude? I doubt that you are suddenly going to
grow any stronger, and also suspect that you recognize this after clashing with my constitution
numerous times. A bout may leave me as the more wounded party, but the confrontation still
remains unproductive.”
Garfiel: “Yer right.”
About ten minutes have passed since Garfiel and Elsa started fighting.
Steel has already met steel over one hundred times, each competing viciously with the other.
Garfiel holds the slight advantage in terms of combat ability. He narrowly surpasses Elsa in brute
strength, in speed, and in his techniques, never once conceding predominance.
But Elsa can heal her wounds in mere seconds and happily accepts injury without feeling pained in
the slightest, never once hesitating in either her offence or defence.
And while getting into wounds, it's worth mentioning that Garfiel is also wounded. He also needs
time to heal himself, while Elsa does not.
He is inferior to Elsa in terms of stamina. Should the fight turn into an endless cycle of bouts, then
her blades will soon catch Garfiel.
However,
Garfiel: “Five... no, maybe six? 'S how many times my amazin' self beat you in.”
Elsa: “Yes, you may be correct. And?”
Landing a direct hit with a kick, smashing her into the wall with his shield, grabbing her by the leg
and slamming her head-first to the floor—Garfiel has landed many fatal strikes on Elsa.
The injury healed every time, and he truly was not achieving anything, but—
Garfiel: “I was anticipatin' four 'er five times at best.”
Elsa: “—”
Garfiel: “Vampires ain't immortal. You pile enough killin' blows on 'em... 'n eventually they're
gonna run outta life. That's what I'm gonna be doin' t'you 'fore this mansion's all burned down.”
Garfiel takes his stance, legs apart, as he laughs ferociously with his fangs on full display.
Elsa hears him in silence, the smile vanishing from her face. She fiddles with the end of her braid
before giving a quiet sigh.
Elsa: “Mei Lee. —Give me it, and you pursue them.”
Mei: “Elsa... are you serious?”
Elsa: “When given rationale to do it, failure to do it is discourtesy to the opponent. My only regret
is that I may not be able to extract your guts cleanly.”
Replies Elsa with her eyes closed. Mei Lee does not question further.
191
She drops the knife holder she has been championing to the ground, and draws a different holder—
one containing merely two knives, and throws it to Elsa.
Garfiel: “Hmm?”
Garfiel hums cheerfully as he watches Elsa draw the knives from the holder.
These two blades radiate a pressure so intense that none of the others she's used can compare.
The knife in Elsa's left hand is completely black from the handle to the blade. It looks identical to
the kukri she's been using at a glance, but this one's blade is curved with countless, bestial fangs
down its edge, specialized more for goring than ripping.
The knife in her other hand is the exact opposite, pure white with a thick body. It also looks like a
kukri, but its thickness makes it seem like a strike from it could snap bones, and pairing it with the
black blade makes its ruthless image compound greatly.
Garfiel: “Yer tellin' me that's yer ace?”
Elsa: “These are the ones I use when I'm focusing on killing the opponent, rather than seeing their
guts. Exclude Mother, and you are the third person I've used them on.”
Garfiel: “That's one hell'v'n opinion I ain't glad for, n' one hell'v'a family I ain't jealous 'bout, oi.”
Garfiel scrunches up his face at the unpleasant confession.
Mei Lee gives orders to her witchbeast as she nimbly moves herself. The dimwitted beast stomps the
ground, charging through walls as it heads toward the main wing in pursuit of Subaru's group—
however,
Garfiel: “Well, thanks fer showin' me yer ace. I don't show you mine, n' 's what ya call unfair, yeh?”
With that, Garfiel stomps the ground.
Immediately, a pulse rushes out Garfiel's sole and through the ground, speeding down the hallway,
passing beneath Elsa before reaching the witchbeast—and exploding.
Pork: “—!?”
Mei: “Boulderpork!?”
The earth caves in beneath the beast, which loses its balance and crashes into the wall as it falls. The
impact rocks the mansion, and Mei Lee is unable to stay atop the witchbeast, instead coming to land
in the hallway. She strokes the fallen Boulderswine's rump as she looks at the floor, sees the
unnatural depression, and glances behind her.
Mei: “Don't tell me, you did this?”
By utilizing his EARTHSOUL BLESSING, Garfiel can conjure depressions and protuberances in any
surface within visible range that he can determine as being GROUND. It comes with disparities in
effectiveness depending on how far away the target is or how large a scale he is aiming for, but it's
more than enough for him to bluff with.
Garfiel has learned from Subaru to, when you've got something you really don't want others to find
192
out, laugh with complete shamelessness.
Garfiel: “'S about what it is. Yer safe t'think that me not lettin' yer escape's n' expression'v my will.
Long 's my feet're touchin' th'ground, yer ain't escapin' from anywhere my amazin' eyes can see ya.”
Elsa: “Mei Lee. You can put minimal forces upstairs. Call the others, and awaken that beast.”
Mei: “...Mama'll be mad.”
Elsa: “What will truly earn us a scolding is if we fail to remove the threat. And, I doubt we'll have
the leeway to worry about what will come afterwards.”
Garfiel: “So y'do get it.”
Mei Lee's expression loses its calm as she nods, puts her fingers to her mouth, and whistles.
Garfiel silently watches on as the thin sound echoes far, all throughout the mansion. If the two were
speaking truths, then witchbeasts should be approaching this spot before long.
This situation is only blazing hotter and hotter.
Elsa: “I'll pluck off your limbs and shoulder you home once you're lighter. I doubt this will all be
worth it if I'm unable to enjoy myself protractedly.”
Garfiel: “Where's th'option t'just quit it with th'guts thing?”
Elsa: “I'd rather quit breathing.”
Garfiel clicks his neck at that statement, before stooping forward in preparation to receive the
enemy's strike.
Elsa sways loosely and nimbly positions her white knife behind her, flexes her arm,
Elsa: “—I assure you that I, more than anyone else, can love you to your flesh and marrow.”
A horrific, debauched smile. The shriek of blade rubbing against blade.
And,
Garfiel: “—Ghgh!?”
The white knife sticking from Garfiel's left shoulder breaks his bones apart.
—The battle between the Guthunter and the Shield of Sanctuary, enters its final phase.
※ ※ ※ ※ ※ ※ ※ ※ ※ ※ ※
His beaten shoulders, his hips, his head all hurt.
He is battered all over after falling many times, always stifling his pained moans from the impact
dead.
193
He runs, runs, runs, out of breath, knees shaking, eyes fogged, runs.
It hurts to breathe. He keeps his head low, so as not to inhale smoke. The flames have already
engulfed the majority of the building, through which he sprints as he searches for a yet-untouched
door.
Subaru: “—hk”
Discovering an unopened door, Subaru flies madly at the doorknob and wrenches the thing open.
Before him is revealed an utterly mundane guestroom, which will shortly drown in a sea of flame.
Leaving the sentimentality aside, Subaru leaves the door open as he runs for another room. He goes
for adjacent room, and the one adjacent that, and the one adjacent that, opening every door he sights
—
Subaru: “—There!”
Freeing him from the scent of soot and char, the stench of aged paper streams out of the room.
Subaru sniffs the familiar, musty smell as he stomps across the threshold.
He raises his head. Addresses the person occupying this chamber.
Subaru: “Hey! Enough of this, stop being angry and listen to—”
Beatrice: “Get out, I suppose!”
An invisible shockwave comes racing at him, threatening to blast him away. But Subaru manages to
hook his fingers on the carpet to defend himself from the force.
Amidst a pressure so intense it could drag him backwards with it, Subaru's cheeks twist into a smile.
Subaru: “Hah! Don't underestimate me too much. You think I'd put up with getting thrown out of
here so quickly, over and over, by the exact same meth—”
Beatrice: “I won't say it again, in fact!”
Subaru: “Bhggagh!?”
A thick book rides the wind to smack against Subaru's forehead, dizzying him and sending him
tumbling, flying backwards, ejecting him from the room.
He shoots down the corridor. Crashes into a wall. He shakes his head as the door closes itself in
front of him, and he hurriedly leaps at the thing—already too late. This room is no longer connected
to the Forbidden Archive.
Subaru: “Asshole! Who're you taking after, goddamn loli!”
After violently kicking the door open, Subaru breaks into a run in pursuit of another door.
That the room hadn't sent him to the second floor of the eastern wing—an area close to Garfiel's
fight with Elsa—was probably Beatrice's kindness.
Subaru: “Then at least listen to me, stupid!!”
194
Beatrice must be thinking the exact same thing from within the Archive.
Keenly feeling that truth, and rejected times upon times, Subaru sprints through the mansion in
search of the door to the Forbidden Archive.
With the fight in the western wing in its final phase, and the fire from the main wing blazing
through the whole building—only a question of time remains until Roswaal Mansion burns to the
ground.
5
5 Tappei A/N: Guiltilaw-san, what have you done!?
195
CHAPTER 128: LOVE YOU TO YOUR BLOOD AND GUTS
He drives his fangs into the green tail slipping before him. Mindlessly tears it apart.
Purple fluids splatter everywhere and vivid blood showers his face, but he doesn't care. His left eye
has already been bathed in venomous fluid and blocked shut for ages.
He roars to obfuscate the burning pain before slamming his arm into the two-headed snake, killing
it. He kicks its corpse, keeps everything in front of him in check as he retreats, and when the chill
races up his spine—he instantly recoils back.
And the grisly blade screams past, grazing his chin.
The witchbeast in the blade's path becomes prey to the fanglike knife. Flesh is shredded, blood
spatters in sheets, a scramble of organs forms a curtain before him—which he charges through,
aiming for the perpetrator woman before ramming his arms into her torso.
Elsa: “—!”
His right shield at her chest, his left shield at her flank, her flesh squelching and bones cracking at
each point.
At his ears, before his eyes, from all directions come the cacophonous cries of beasts, their shrieks,
his roars, crashing conflict, the pounding of metal on metal, too many noises mashed together for
him to properly register the world.
He doesn't care. This stuff in front of him, in his right-eyed vision, is what's real.
Her voluptuous breasts crater in, the force of the gut-wrenching blow making her vomit blood. Even
with her scarlet lips turning a deeper shade of sanguine, and faced with pain enough to threaten her
life, her expression remains one of rapture.
It might not even be her combat strength, or her stamina, but that mentality of hers that's the real
nuisance.
Elsa: “—Hah!”
Garfiel: “Ghrrrrr!!”
Her short exhale. His responding roar.
She swings her left arm from behind to in front, shrill noise pealing out from behind him. The slash
reflects off the wall, rebounds off the ceiling, hits the floor as it comes pressing for the back of his
head.
Garfiel: “—”
He directs his attention behind him, extinguishing the idea of evading it from his mind.
The woman before him draws her right arm firmly back, preparing to piston her serrated black knife
into him. If this is to catch him between the two knives, then this blow will likely slice open his head,
or maybe his throat.
He tilts aside, forcing himself out of the blade's path as it rushes to stab the back of his head.
A thunk resounds out from around his left shoulderbone. Feeling the tip of the rebounding blade
bite into a gap between his bones, he clicks his tongue—when the knife slices into his joints,
196
rendering his right arm momentarily motionless.
Elsa: “Huaaah!”
Garfiel: “Shah!”
So violent as to mute all sound, she looses the readied blade.
This unremitting attack makes for less of a 'slash' and more of a 'pointy bludgeon'.
The strike will blast his head off should it hit, mutilating it utterly. Garfiel immediately raises his
left arm to intercept the strike, but with his poor posture, he cannot avoid all the damage to his right
shoulder.
Animal teeth shriek against metal for only a microsecond before Garfiel's arm is easily shunted
away.
With only a meagre drop in its speed, the back blade resumes its charge for Garfiel's head. More
than enough strength to cleave apart his skull presses in, a second from hitting.
Hitting—
Elsa: “—!?”
—what Garfiel kicks up, forcing it into the path between his head and the knife, the witchbeast's
corpse.
An uncomfortable feeling like a hard-skinned vegetable against his cheek, and blistering venom that
burns the skin it touches. Risking being bathed in both these things, he salvages the benefit of
avoiding fatal damages.
The knife slices into the witchbeast's corpse, the battering force of the blow proceeding through the
cadaver to strike Garfiel across the face.
The impact pummels him, sending him whirling left to right, spinning in circles—and with two
wilful steps into the ground, he soars backwards.
His EARTHSOUL BLESSING activates, obeying his will to make the ground he stepped on explode.
The detonation sends him soaring backwards, the woman now to his back as he proceeds to zoom
straight for her. —With the woman's white blade still sticking out of his shoulder.
The instant the blade touches her, the woman flinches.
Though she knows that the side contacting her is the pommel, it still makes her falter from making
any instantaneous decisions.
With his right shoulder still against the woman, Garfiel spreads his stance to drop his centre of
gravity.
The instant this makes the woman think to step backwards and open range, Garfiel's arm shoots up
and grabs her face in a vicegrip.
Garfiel: “—Partial Transformation!”
Immediately following his scream, a change occurs in the arm clutching her face.
The arm swells explosively—growing a coat of golden fur in an instant, transforming into the logthick
arm of a beast.
And naturally, it ends in a beast's paw, what with saber-like claws,
197
Elsa: “Kyhaaaaah!”
The thick claws gouge into the woman's face, splaying blood everywhere and making her recoil.
His five fingers as they drive into her head prompt the same pain and injury as knives. Evens she
has to put her hands to her face, backpedalling, shrieking while looking to the ceiling.
Garfiel: “Rhm!!”
He plunges a kick into a torso, shunting her back.
The force battering her chest carries more than enough strength to further destroy her shattered
bones and ruptured innards, churning them into a greater mess.
The fallen woman drops her weapon, spitting up pure scarlet as she gives a faltering laugh.
It's horrible to listen to, and he's more than ready to swoop in and make it stop, but,
Garfiel: “Fuckin'! Just one after another!”
Just as Garfiel moves to pursue her, witchbeasts flood into the gap in his assault.
Rats with black wings, possums bloated in proportion to their anger, Spotted Rex assembled here
from throughout the mansion, and a restored giant—the Boulderswine all rush in.
His claws rip apart the swarm of rats, one stomp of his foot eliminates the swollen possums, his
kicks snap the necks of the Rex snapping at him, all as Garfiel faces the charging Boulderswine
head-on.
Mei: “Get squished!”
Garfiel: “Y'think I'm gonna be toleratin' that, y'dumbass!”
Tons of weight come charging with explosive force.
Rather than a blow from an animal, this cannonball is equivalent to a building dropping on him.
Not even Garfiel could take a direct blow from this and get out safely. He'd be unable to offer even
a second of resistance, get blasted away and trampled flat.
However,
Garfiel: “'S what makes it fun—!”
Bracing his legs, Garfiel unleashes his Earthsoul Blessing to its utmost limit.
He feels the blessings of the earth pulsing up from underfoot, rippling through his flesh.
A warfaring glint lights Garfiel's golden eye, fangs bared as he smiles wickedly, detonating the
blood lying dormant inside him.
Garfiel: “—σσσσσȠ!!”
This strangled bellow is not addressed to the outside, but a call to his own interior.
Flowing through his body, difficult to accept as it is, definitely not something he acquired by
choice: his bloodline. He calls to his usually-hidden pedigree, feeling goosebumps as his soul
trembles.
198
Just like his left arm that tore the woman's face apart, Garfiel's right arm swells explosively.
Starting at his arms, his shoulders, his torso, his neck, his head all crunch as his skeleton changes
shape, his face morphing from that of a human to that of a ferocious feline—a massive tiger.
Following the enlargement of his torso, his hips, his legs, his clothing fails to endure the pressure
and bursts apart. Scraps of cloth hang off his frame, the two shields on his arms barely managing to
stay equipped as small bucklers—here is a beast that, by physique alone, can compare with the
oncoming Boulderswine.
Garfiel: “——฀!”
The floor creaks, caving in beneath him.
Even this solidly-constructed mansion cannot endure the confrontation of these two massive beasts.
So giant that the hallway cannot contain him, Garfiel shatters the walls, ornaments crashing to the
ground as his back scrapes across the ceiling.
Mei: “—Wugpig!!”
The girl atop the witchbeast shrieks in response to Garfiel's transformation.
She must be screaming the name of the witchbeast. Answering to its master's call, the Boulderswine
gives a roar so strong as to disintegrate boulders and opens wide its maw with all its flat teeth,
racing for Garfiel.
The witchbeast rears up on its back legs, raising its forelegs to stomp Garfiel flat.
The massive tiger, its golden eyes flaring, lets its own legs propel it into the opening before the
behemoth's crushing blow hits and stabs its claws into the Swine's thick, stony hide.
Blades screech against bedrock as the tiger's claws are peeled out of their sockets. Knifes fail to
puncture the thick hide, and the Swine's plummeting forelegs proceed to slam straight into the tiger.
The stomp presses down on the tiger, a crushing pressure on its shoulders. The force pins Garfiel's
upper body to the ground, the merciless impact prompting the tiger to shriek.
Mei: “Don't stop, Wugpig!!”
Bones shatter and flesh squelches, but the noises do not deter the witchbeast's master.
Hearing her wailing voice, the Swine roars and raises its forelegs up, ready to stomp once again and
crush the tiger's head.
However,
Garfiel: “——฀!”
If his claws won't work, the tiger has only one weapon left.
Twisting its neck, the tiger with its crushed shoulders uses its spine to upright itself. The Swine's
forelegs are raised and its belly is exposed—the tiger bares fangs.
Not even a witchbeast with skin as solid as rock can have its entire body at the exact same
toughness. Compared to its legs or back, its vital regions are going to be less heavily guarded.
And so, the tiger drives its sharp fangs into the Swine's bared stomach.
Mei: “Boulderpork!?”
199
Garfiel: “—ℓℓℓℓ₰!!”
The tiger's jaws, so immense that they could swallow a man whole, close around almost half of the
Swine's extensive belly.
For a moment, the Swine's hide does attempt to resist the piercing fangs. But like the points of
knives stabbing into a fruit, the sharp fangs instantaneously and effortlessly tear through the thin
skin.
The Swine's shriek comes as the tiger kicks at the floor, using the momentum to roll sideways.
With his fangs still sunken into his prey, attempting to shred the creature apart—it's the hunting
behaviour of riverside-dwelling water dragons.
Were Natsuki Subaru here to witness it, he would deem it as being something close to the death roll
of an alligator, a creature that does not exist in this world.
His hindlegs strike the floor, buying rotational and forward force as he mangles the Swine's torso.
Inside the thick hide rest a vast store of blood and guts, which spill relentlessly out from the
bitewounds and onto the mansion hallway floor.
Pork: “—ζ”
Eyes wide, the Boulderswine gives a weak death wail as it collapses.
The tiger spits out chunks of the Swine's flesh before slamming its rear leg into the massive
creature, toppling it onto its side. The girl, having dismounted the witchbeast at the moment of the
crash, is utterly lost for words as she watches her witchbeast's gruesome death.
Mei: “No, way... I don't believe it...”
Stepping back, the girl glances behind her to see what troops she has left.
Many witchbeasts have heeded her call are steadily assembling here. But they are only a mob of
small- and medium-sized creatures, none of them large like the Boulderswine.
Mei: “Ugh! What is this!? Elsa! Elsa! Dooo somethinnngg!”
Elsa: “...That is a rather, unsparing demand.”
Realising that she is at a disadvantage, the girl slings senseless insults while calling her partner's
name. Reply does come, from a shadowy woman who crawls out of the darkness.
Her mangled face has regenerated. She fiddles tirelessly with her bloodied braid.
Elsa: “Gouging a woman's face open without hesitation, you are indeed fantastic, you are.”
Garfiel: “—σσ฀! σσ฀! σσ฀!”
The woman laughs with a bloodsoaked grimace. The tiger, shoulders broken, growls in agitation.
Its massive form quakes, before it butts its massive head against the fallen Swine, and pukes.
The tiger moans in pain before its great body begins losing mass, bit by bit, and its enlarged form
starts returning to human shape. After a few seconds there now stands a half-naked boy, batting
away shredded strands of golden fur.
200
Garfiel: “Auh... fuck, m'back. Head hurts...”
Elsa: “I see... so you are half-beast. I did think your eyes looked rather nasty for a human.”
Garfiel: “'F we're gonna be followin' yer logic, that means our Captain ain't human either.”
Garfiel shakes his head, getting a grip on the sensation of his own human body.
Over the course of returning to human form, his broken shoulders have mended enough that they can
both move. But in saying that, they still do flare with pain every time he moves them, and make his
thoughts burn a soldering white.
He can't stay in top performance for much longer.
But the same should be going for his opponent.
Garfiel: “Went n' busted open yer witchbeast's guts fer ya. Yer allowed t'go happily swimmin' n' that
ocean 'v blood there, I ain't gonna mind.”
Elsa: “I'll have to decline. Animal guts serve as no substitute unless I'm extraordinarily starving.
The beauty of guts is that they are disembowelled from people.”
Garfiel: “Yer aesthetics make no sense t'me.”
Garfiel sticks his pinky into his ear and picks rigorously while giving an astonished sigh.
Elsa is overwhelmingly disadvantaged, but her attitude isn't budging.
—Garfiel estimates that it will take five more tries at most until Elsa's immortality ends.
And Garfiel has already showered four lethal blows on her. Five if you include the mauling of her
face. This should be about time that she starts hitting the limit for her regeneration.
Meaning that Elsa's stock of lives is already exhausted. Garfiel is injured as well, but that isn't going
to make him slack in this fight.
Being that no support is possibly coming from Mei Lee's beasts, they effectively have their blades
at the other's throat—so why is she being so composed?
Elsa: “It's not that there's any special reason for it. You don't have to be so scared.”
Seeing Garfiel's brows furrow in puzzlement, Elsa speaks as if comforting a child.
Garfiel scrunches up his face in response, growling like an animal.
To obfuscate the fact that she has clearly seen the slight confusion in his heart.
Garfiel: “Fuck off. Stop talkin' like yer know anythin'.”
Elsa: “But it's plain to see. Disembowelling someone means facing someone before they are
disembowelled. Your face is a familiar one to me.”
Garfiel: “—”
Elsa: “It's the face of being unable to comprehend a deviant.”
Garfiel falls speechless, his throat feeling to clench. Elsa puts her hand to her mouth and laughs.
201
She smiles slightly as she tilts her head.
Elsa: “Don't worry, it's fine. I'm not wishing to be understood by anybody. My happiness is
something I acquire by spurning the life of another. To live is to spurn death.”
Garfiel: “...'M gettin' that 'f I take this seriously, 'm gonna go nuts.”
Garfiel raises his arms, battering his shields together as he rejects any attempt at understanding her.
He doesn't have the leeway to be thinking about her circumstances. And her last statement has just
eliminated any reason he had to pay attention out of whimsy.
Garfiel: “But I will ask yer this. ...'F yer pledge that you ain't ever gonna do nothin' bad again n' run
away, 's not impossible that I'll let you go.”
Elsa: “You truly are a precious boy.”
She shows her final mercy, then dispels it with a smile—the signal, to charge.
Blasting off, Garfiel soars ahead. Elsa counters him by swinging her white blade up to hit the
ceiling, hit the floor, revolving and rebounding as it closes in on Garfiel.
Elsa's wide white blade is a stringing-together of multiple knives. The blade-edge alternates from
one side to the other, the knife rippling like a snake's bones as it ricochets through the hallway.
Up? Down? The knife easily outspeeds the eye, soaring about as a white light. Garfiel braces his
shields over his head and abandons the option of evading. The knife plunges down into his upper
left arm, imparting him with the pain of broken bones as he resumes his advance.
Elsa: “I was born in Gusteco of the north, where it is very, very cold.”
Split-second combat is unfolding in this battleground, but for some reason her lilting voice sneaks
into Garfiel's ears.
It isn't even audible. His attention is pyroclastic, focused amidst instantaneous trade of deadly
attacks. There is no opening for this voice to butt in.
Is what it should be, but the woman's voice slips smoothly into Garfiel's consciousness.
Elsa: “The divide in wealth was fierce, and it wasn't uncommon at all for lower-class children to be
abandoned. I was one of those children, with no parents I ever knew, drinking dirty water to
survive.”
Garfiel: “—Rghhhh!!”
Elsa: “I spent my days stealing objects, threatening people, doing things in that vein, with the
people around me constantly changing. Why am I alive? What is happiness? ...Not questions I had
any time to consider back then.”
His fist plunges forward, inches from belting Elsa's face.
But she leans aside to dodge the overblown attack, slicing her black blade up to cut shallowly
through Garfiel's torso.
The bestial fangs pilfer his flesh. Elsa licks her lips as the bright blood bathes her.
202
Elsa: “It was frigid that day.”
Garfiel: “Shut up! I ain't goddamn listenin'!!”
Elsa: “The wind blustering from the lofty mountains was so strong, so cold, that it froze the town
that day. My breath could freeze in that chill, when the shopkeeper I stole from caught me.”
With a hot sigh, Elsa speaks on, enraptured.
Her blades of death compound in momentum, slicing cut after cut into Garfiel as he fails to keep up.
Elsa: “No one would complain if he killed me, but seeing as I was a girl... I can still remember his
face as he smiled, and moved to strip my clothes.”
Garfiel: “Gh, auh...”
Elsa: “The bitter wind howled as he stripped my overwear, snatched my underwear... and when I
contemplated that before he could do anything to me, the cold might just kill me first, I happened to
pick up a shard of glass.”
Her leg sweeps up to try and belt him in the side of the head, but Garfiel counters it with a headbutt.
The impact reverberates through his brain and makes him recoil, but surely shattered Elsa's foot too.
Elsa draws her leg back, retreats. But her expression remains one of ecstacy.
Elsa: “I wasn't thinking about anything. I just had the shard of glass, then when he leaned forward I
pressed it into his stomach, moved it, and sliced him open.”
Garfiel: “—”
Elsa: “I felt nothing for his screams, or the fact that I had taken a life. But amidst that icy gale, I did
think,”
Garfiel's breathing freezes. Elsa smiles.
Elsa: “How warm, blood and guts are.”
Elsa's blade swings up, threatening to split apart Garfiel's skull. He glides aside, kicks off the wall
to manoeuvre behind Elsa, slams a kick into her back—but she instantly twists around and strikes
his shin with her pommel, diverting the kick.
His leg crashes into the wall, which crumbles alongside plumes of dust. Garfiel clicks his tongue as
he leaps back and away.
Elsa: “If there is happiness in the world, then it is in the warmth and beauty of forgetting the cold.
From birth I had nothing, and now I had this: the first definite happiness I ever found. —You can't
understand, can you?”
Garfiel: “Ain't wantin' to, either.”
Elsa: “That's fine. I don't want sympathy.”
Garfiel: “Then why'd y'tell me th'damn story, 's fuckin' gross.”
203
Elsa: “Why, I wonder?”
Garfiel's eyes house hostility as Elsa tilts her head, mystified.
And she narrows her eyes saucily, licks her lips salaciously,
Elsa: “Because I find you truly darling.”
Garfiel: “...Sorry, but I already got a girl I like. Ain't got time t'be datin' a crazy bitch.”
Elsa: “So cold. But it's fine. I'm only concerned about your innards.”
It feels like a conversation is happening, but fundamentally no conversation is.
Over all his exchanges with her thus far, Garfiel has finally come to understand this.
He has no interest or sympathy or anything for Elsa's life story.
That was her foundation, she had those experiences, and she became this monster. That's all.
Garfiel's shields already know who they ought to protect.
Garfiel: “—You're dead, Elsa Granhiert.”
Elsa: “Once I kill you, I will adore you, Garfiel Tinzel.”
Each calling the name of the other, the half-beast and the murderer wage violence.
The beaming light of the white knife slices through the corridor's darkness, and the black knife
pistons forward cleave Garfiel in two.
A knife ricochets everywhere in the corner of his vision. He cannot defend against the attack, nor
does he have the option of evading it. But if he fails to take the blow and dampens his charge, he'll
merely be repeating the same foolish mistake.
Garfiel: “—”
The knife slices through sound, dancing throughout the hallway.
If he cannot perceive the blade's point, he can only aim for the point it was thrown from.
Garfiel thrusts out his left arm, the fasteners on his shield loosened—and lets the thing fly.
He had loosened the bindings when he battered the shields together. Now he is tossing it, and Elsa's
eyes shoot wide open as it smashes directly into her left hand—something crunches, and her broken
fingers drop her white knife.
Having lost the hand manipulating it, the knife stabs into the ceiling, where it falls still.
A deep, dark smile, and a surging roar. A deathly blade murders the air as it swings down—Garfiel
charging straight into it—and strikes him.
He sets his right arm upon his head to receive the direct hit from the black blade.
The shockwave pierces through his shield, rocks his skull. His eyes spin and he comes close to
stumbling forward, but just manages to stomp firm and catch himself.
He did it—when the woman's knee shoots up and smashes Garfiel's nose.
204
Elsa: “You mustn't be careless and think you're safe.”
She says with a laugh, sweeping her leg up at Garfiel as he recoils.
Her leg hangs poised high, and from her shoe comes the glint of a blade in the heel—with his point
aimed to stab Garfiel through the neck—
Garfiel: “Yer the one who better not be overlookin' my amazin' weapon.”
His open jaws swallow her heel and the blade whole, gnashing at her slender foot.
With her bones and the knife chewed up to the heel, Elsa's eyes shoot open wide.
Elsa: “Goodness.”
Yelping in surprise, Elsa staggers away but loses her balance and tumbles to sit on the spot.
Her right leg is mangled from the ankle down, inoperable, and the force of her own attacks has
broken her arms as well. With her left leg as her support, Elsa gazes at Garfiel—
Elsa: “—Ahh,”
Taking in a breath, Elsa blushes like a girl in love.
Her exhale carries enough heat to be chromatic. Her wet eyes abound in hot passion.
—Before Elsa, Garfiel shoulders the immense Boulderswine, and throws it.
Although aware that she will be crushed beneath its incredible mass, it is not until the silhouette
swallows her that Elsa's gaze strays from Garfiel.
With her breathing ragged, gazing at the grimacing blond boy with love—
Elsa: “I feel thrills.”
The overwhelming weight crushes the murderer, the vampire, the Guthunter, until nothing remains
untouched.
Her flesh squelches. Fresh blood mingles with fluids from the witchbeast.
Scenting the stench of death, Garfiel howls.
Roaring, bellowing, booming like thunder through the burning mansion.
—The Shield of Sanctuary Garfiel Tinzel, and the Guthunter Elsa Granhiert, have concluded their
battle.
205
CHAPTER 129: —CHOOSE ME
—When she thinks back on that instant, the terror assaults her even now.
How her clinging fingers were cast aside, and her name was affectionately spoken.
The love in their goodbye. The determination and tears in their smiling eyes. Both carried far more
than enough weight to silence her.
What should she have said? She still doesn't know.
What had she been thinking? She can no longer remember.
What ought she have done? She still fails to see any answer.
—And so Beatrice remains, even now, cowering motionless in the Forbidden Archive.
Beatrice: “...Lewes.”
The sound out her lips is a fragment from a memory so ancient, even just the word sounds wistful.
When she speaks that name, emotions bursting, the frozen time inside Beatrice—the four-hundred
year void—instantly comes surging to the surface.
Beatrice secluded herself inside the Archive, waiting for THEY's eventual arrival, only after Lewes
Meyer had been lost as her existence became impetus for the establishment of SANCTUARY, and the
Warlock Hector had been repelled.
Beatrice had lost someone so close to her that they could safely be called her only companion.
Anyone could see how haggard Beatrice was, having lost that friend owing to her own inability.
And everyone knew that only time would mend her injured heart.
So her Mother's conclusion was simple.
Echidna: “I suspect that warlock will return to destroy me someday. I plan to set up means to
oppose him before that happens... but even that might be fallible.”
Beatrice: “Yes, Mother.”
Echidna: “If we engage in confrontation again, it will develop into truly heated, absolute combat.
Considering the enemy's strength, my chances of surviving are about fifty-fifty... or maybe a little
lower? Since Roswaal's unfortunately lost his gate, and can't assist in battle.”
Echidna lowers her gaze, but Beatrice's unaffected demeanour remained stable.
It's not that she's suppressing anything. Ever since that day, her emotions have almost entirely
stopped showing on her face. Who could suppose the effect that the overwhelming loss, the
emotional aftershock, had had on her?
It could be that her emotions froze exactly because her heart knows that effect.
Echidna looks at Beatrice and her unchanged expression, running her finger through her white hair.
Echidna: “I'm already one of the witches least suited to combat. Once I know I can't enlist aid from
206
Roswaal, genius in sorcery, it's after expending all possible means that I finally begin seeing hopes
of victory.”
Beatrice: “...What should Betty do, I suppose?”
Everyone knows that Roswaal was half-killed in the battle to establish SANCTUARY's functions. His
gate was utterly decimated, making him ineligible as a magician.
The sight of her comrade lying in bed, still moribund in this very moment, arises in Beatrice's mind.
Sounding somewhat desperate, she assaults Echidna with questions.
Beatrice: “Should I do the same as Roswaal, and buy time until your algorithms are complete? Or
should I sacrifice myself, conglomerate of powerful od that I am, and become the nucleus for the
algorithm, I suppose? I won't regret it for an instant when it's for your sake, in fact. ...Please, use me
however you'd like, I suppose.”
Beatrice grasps her skirt and curtseys, displaying the greatest of trust to her mother.
Honestly, the emotion is far too brittle and fleeting to be called TRUST. But Beatrice is unable to
comprehend her own present mental state, and even supposing that she did understand herself, she
would have likely reached the same solution.
Reckless lust for vengeance, and indignation at her powerlessness—the question of whether or not
she recognizes these two feelings of hers constitutes the only single difference.
Echidna: “—I see. Once you've told me that, even I can ask for favours without any reproach. You
truly are a good girl, Beatrice.”
Beatrice: “...Yes. Betty's your daughter, in fact.”
Hearing such words from Echidna would usually overjoy Beatrice.
Perhaps Echidna was aware of that, for she was careful give Beatrice verbal praise only
infrequently. But now those magic words sink into Beatrice's empty chest with a hideously hollow
thunk.
Perhaps nothing will rekindle the fire in her heart.
Is what Beatrice thinks, and so she fails to immediately react to Echidna's next words.
Echidna: “Beatrice. I'm entrusting you to oversee my archive of knowledge. Until the time that must
come does come, you'll protect the knowledge as the Archive's keeper. —So that nobody can steal
it.”
Beatrice: “...wha,”
Echidna: “Fortunately, you have unparalleled affinity for Yin magic. You'll use GATE CROSSING to
link a familiar location to an isolated space. ...Yes, we'll call it the FORBIDDEN ARCHIVE. There, I
want you to guard over the extent of my knowledge, compiled into books.”
Beatrice's eyes shoot open in shocked turmoil as Echidna keeps speaking, leaving her behind.
Beatrice had expected Echidna to order her to accompany her in this battle of life and death. Cast
into an utterly unanticipated role, Beatrice can only glance about in bewilderment.
Even though witnessing her daughter's discomposure, Echidna continues without missing a beat.
207
Echidna: “It'd be best to link the Forbidden Archive to Roswaal's mansion. I'll dismantle my
laboratory, and prepare for the final battle. I'm sorry, but I can't expend any people to carry the
books. I'd like you to ask Roswaal about preparing the bookcases and securing labour.”
Beatrice: “W-wait...”
Echidna: “It won't last forever. Both you and I are already liberated from the fetters of predestined
lifespan. The cycling of the seasons isn't especially meaningful for us. But in saying that, once you
consider that I may be lost, it's irresponsible for it to lack deadline. Which means...”
Beatrice: “Please wait, I suppose!”
After a deep breath, she shouts.
Beatrice cannot comprehend what her mother is saying.
Or no. Her instincts are screaming at her, telling her not to comprehend it. Echidna's thoughts are
vast, always easily excelling what the ordinary man could possibly understand. Meaning that
Echidna's statements represent the optimum, and Beatrice had never thought to interrupt her before.
But now is not like that. Nothing like that.
If Beatrice lets Echidna speak her whole screed, she will surely regret it.
If Echidna states the whole of her opinion, what she'll present is the absolute optimum solution with
no purchase for debate. The world will follow a course affirming Echidna's stance, and Beatrice will
be unable to defy it.
To defend against that, Beatrice must interrupt before Echidna can finish.
Beatrice: “Mother... what are you saying, in fact? I-I, don't understand what you mean with this
Forbidden Archive, I suppose. Betty is! Staying with you!”
Echidna: “Having you with me won't influence the confrontation with the warlock much at all,
unfortunately. Naturally, it would surely increase my chances, but... only by a pittance. It would fall
under statistical error.”
Beatrice: “B-but if it's better than me being absent, then Betty will help you, in fact! It'd be—”
Echidna: “You can't. The risk that we'll both be destroyed outweighs a tiny, potentially non-existent
boost to my prospects of winning. Considering that there is a less than fifty-percent chance that I
will survive this battle, I have to endeavour to ensure my knowledge survives to the hereafter.”
And ensuring her knowledge survives to the hereafter means upkeep of this Forbidden Archive that
she's trying to entrust to Beatrice.
In this moment, Beatrice curses her GATE CROSSING and her ability to create unique spaces. If she
didn't have these powers, her mother would never desire that she take this ro—
Beatrice: “Don't... tell me... my powers were for this?”
Echidna: “—”
Beatrice: “You knew from the beginning that this would happen... supposing so, then it isn't just
about this Forbidden Archive, wh-what happened in SANCTUARY was also...”
208
Echidna: “Having ways to anticipate things doesn't necessarily mean using them. I did have means
to both perceive this route, and settle matters without travelling it. But I swear on my way of life
that I have not utilized that power. That alone I want you to believe.”
Echidna shakes her head in response to Beatrice's strangled question.
Echidna approaches Beatrice, who is chewing at her lip, before taking a book from the bookshelf
and presenting it to her daughter.
Beatrice: “This, is...?”
Echidna: “An imperfect replica of my BOOK OF WISDOM. The Book of Wisdom's algorithms are
both advanced and moreso complicated, so I didn't manage to fully unravel them all... but it should
be enough to work as a simple guide for the owner's future.”
Beatrice accepts the book, tracing her shaking fingers over the cover.
She raises her head to look at Echidna, who stares at Beatrice with the same faraway gaze she
always has. As though she's looking somewhere into the distance.
Echidna: “There are two books. One goes to you, and the other has been given to Roswaal. I expect
Roswaal will manage what comes next provided he reads the book. I know it's a one-sided request,
but I want you to see it through.”
Beatrice: “—”
Beatrice looks down at the book, her eyes wavering as she finally realises that she is far too late.
I have to make her speak, I have to make her say it. Were her ideas, but they were not nearly
sufficient.
Echidna, her mother, had already settled on all of her answers.
Beatrice could cry, pleading and clinging, but it would not change Echidna's stance.
Because that's the kind of person the WITCH OF GREED Echidna is, and the kind of witch she is.
Echidna: “We'll return to the topic of cutoffs. I might not return, but the archive must be opened to
someone someday. Once that happens, it'll be clear to you. Someone suitable to inherit my
knowledge will surely come for you.”
Beatrice: “Come, for me...”
Echidna: “We'll call this person THEY. The cut-off is when THEY open the doors to the Forbidden
Archive, and announce that your duties are over. —This is my final request.”
Final request.
The phrase makes Beatrice swallow her breath, and look up at Echidna's face as she gazes back at
Beatrice.
Her mother's constant, unchanging expression.
But Beatrice feels that, in just this single instant, it comes mixed with unfamiliar emotion.
Echidna: “Betty. —Please, be well.”
209
※ ※ ※ ※ ※ ※ ※ ※ ※ ※ ※
After parting with Echidna, Beatrice obeyed her mother's request and went to stay in Roswaal's
mansion, using her Yin magic to create the FORBIDDEN ARCHIVE and stockpile books of her
mother's knowledge there.
It's the sea of knowledge that Echidna had spent her life amassing and cataloguing. When holed up
in this room of books, it feels like her mother is embracing her.
Leaving aside the question of whether or not Beatrice used to perceive it that way, she did obey
Echidna's instructions.
If she neglected to immerse herself in her duties, the bereavement tormenting her heart would
exceed what she could bear. She passed her days in the Archive, oblivious to time, with the loss
always plaguing her.
???: “Replicating souls... overwriting into vessels...”
Beatrice could not accurately determine just when it started feeling hollow.
But once enough time passed that she no longer remembered when she last held a real conversation,
an adult Roswaal began venturing into the Forbidden Archive.
Roswaal: “I'll be iiiiiiiiiiiiiintruding once again today.”
The skinny, unshaven young man limped into the room.
He used a cane and walked with a lumbering gait—the battle with the warlock had destroyed his
body, and his gate had lost the majority of its functions. Even attending to daily life was an arduous
task for Roswaal now.
Even so, after he recovered some amount of strength, he strained his inconvenient body and
displayed his debilitated condition as he faced the bookshelves.
He was just skin and bones. His looks, known for their beauty, shone with no brilliance. His sunken
yellow eyes alone blazed wet with insane ferocity.
Beatrice: “—Do whatever you want, in fact.”
Though really, Beatrice didn't want to let anyone at all enter the Forbidden Archive.
Until the THEY that Echidna mentioned came, this place was meant to be Beatrice's SANCTUARY,
never to touched by anyone's eyes.
But Roswaal was an exception. He alone was devoting himself to Echidna's wishes, as Beatrice
was, a companion who she had spent more than a little time with.
Roswaal's wishes alone would permit Beatrice's heart to open the Archive.
It may have been Beatrice's faint sense of camaraderie that determined the fate of Roswaal L.
Mathers, and his family.
Roswaal ventured to the Archive, sank into the sea of Echidna's knowledge, and staked his entire
lifetime upon a search for something.
Beatrice did not know if his efforts ever wound up bearing fruit.
210
But the Roswaal L. Mathers who had studied with Beatrice under Echidna, ten years after Echidna
and Beatrice parted—when bordering on thirty years of age—lost his life, and his descendant
inherited the mansion.
Roswaal: “Myyyyyyyyyy goodness, it is a pleasure to meet you, Beatrice-sama. My predecessor
had told me about you.”
Beatrice: “...Roswaal's dead, I suppose?”
Roswaal: “The previous Roswaal has passed away. But do be at ease. I, the current Roswaal L.
Mathers, have inherited the debts toward your duties and your mother.”
The second Roswaal gave Beatrice a smile.
—With one of his eyes yellow, and one of his eyes blue.
※ ※ ※ ※ ※ ※ ※ ※ ※ ※ ※
Nothing especially noteworthy happened after that.
The Mathers family continued to introduce themselves as Roswaal down the generations.
Though aware that they did this to remember their respect for Beatrice's deceased mother, Echidna,
Beatrice did not allow the Roswaals unlimited entry to the Forbidden Archive.
Naturally. The only Roswaal to whom Beatrice could give special treatment was the first one. All
the other Roswaals were imposters.
She did accommodate them somewhat, given that they were providing the mansion needed to
preserve the Forbidden Archive, but nothing further.
From then on, Beatrice would only ever open the Archive to THEY.
This awaited THEY, and the guidepost her mother had given her, forced Beatrice into solitude for a
very, very long time.
???: “Your power is magnificent. Please, grant it to me as my spirit.”
—Shut up. Get lost.
???: “You've been isolated here for so long. It's a horrendous fate. It doesn't matter who ordered you
to do this, it's unforgivable.”
—What would you know? About the precious duty my mother desired of me.
???: “You don't think knowledge ought to be free? Can you imagine how many lives would be
saved if the knowledge stored here was spread? You must already recognize it yourself.”
—It has nothing to do with 'how many'. I'm only looking to save a handful of people. And there's
nobody I can save any more, except one.
211
Four hundred years.
Beatrice wasn't seeking them out, hadn't permitted them in, but even so many people visited the
Forbidden Archive.
They each flung whatever words they'd fling at Beatrice, keeper of the Archive, before inevitably
demanding that the Archive be opened.
Their proposals, propositions, and demands did sometimes sway Beatrice's heart.
She wondered countless times after the doors burst open, and she noticed the daylight spilling in
from outside, whether this may finally be the arrival of THEY.
But, heedless to Beatrice's expectations, not a single one of them knew about THEY, and Beatrice's
book mentioned nothing indicating that they were THEY either.
So Beatrice cast away the words, the hands, everything they offered her, rejected them, and kept her
mother's words close as she passed the time until today.
Over the years, resignation and disappointment steadily overtook Beatrice's heart.
She wished that she had spoken with the first Roswaal more.
Ever since she lost the only person who could share her memories of Echidna, Beatrice had to face
this concept called 'eras' all by herself.
She had nobody to rely on. Her only option was to be stubborn, and seclude herself inside an
impregnable, isolated barricade.
Over four hundred years, her cage consequently took shape.
Was it a prison locked from the outside, or from the inside?
—Not even Beatrice could tell any more.
Puck: “Hey there, Betty. It's really been forever. It's me, Puck.”
This inconceivable reunion was perhaps the only event that even minutely thawed Beatrice's frozen
heart.
Beatrice: “B-Bubby? How come, you're here...?”
Puck: “This mansion's Roswaal went and swindled my daughter. So here I am with her. I wasn't
expecting you to be here. I'm glad we got to see each other.”
The name of this cat spirit, bashfully washing his face with his paw, is Puck.
Like Beatrice, he is a man-made spirit created by Echidna. He is the only entity who shares
Beatrice's birth and circumstances, applicable as being her race.
The time that Beatrice and Puck spent together four hundred years ago was short, but felt long.
Puck was created before Beatrice, and separated from Beatrice's group before the battle with the
warlock had begun, wandering the world in accordance with his purpose.
Beatrice never thought that they would meet again, and practically considered him dead. She keenly
felt how the centuries-long reunion made her heart surge.
But, her joy only lasted an instant—.
212
Puck: “After I left you, I spent about three centuries wandering the world before I finally found Lia.
I'm not sure what you're waiting for, but I know your wishes will come true.”
Beatrice: “Yes, yes I suppose. But I envy you, in fact. The role Mother gave Betty has...”
Puck: “Mother? Who was she, again?”
Beatrice: “—”
Beatrice remembers how Puck looked, not joking in the least, his head tilted in mystification.
When Puck left, he and Echidna formed several contracts. Beatrice didn't know the detailed terms
of them, but Puck's forgetting of Echidna is obviously part of it.
Beatrice: “...No, nevermind it, in fact. I'm glad I got to see you again, I suppose.”
Puck: “Mhm, it's great, Betty.”
Puck, having fulfilled his purpose and meaning in life, looked dazzling to Beatrice. But she knew
that the topic she wanted to broach would only serve to impede his path.
So she kept quiet, smiling sadly as she wished her brother well with his future.
The unexpected reunion gave Beatrice slight joy, but moreso agony as her dead four hundred years
pressed down on her heart.
Comparing herself to Puck, who fulfilled his role, Beatrice was dumbstruck at the overwhelming
disparity in their performance.
And she thought:
Beatrice: “...I'm no longer able to ever laugh like you, Bubby.”
Beatrice decided to get as little involved with Puck's beloved half-elf daughter as possible.
If she didn't, Beatrice would wind up taking out her pent-up resentment on the girl. She would do
such wrong to her beloved brother's blameless, precious daughter that the situation would never be
fixed.
Calling her heart to a stop and suppressing her emotions was her forte.
She had spent four centuries constantly doing it through the sunrise, after the sunset, submerged in
the moonlight.
Her speciality. A familiar deed. Lucid resignation. That kind of thing.
That kind of life—which suddenly met an intruder.
Subaru: “M-make it painless ok.”
Beatrice: “It's incredible that you're so persistent in your frivolity, in fact.”
It had truly been forever since someone had entered the Forbidden Archive without permission.
While looking down at the boy, fallen on the floor from the mana drain, Beatrice sighs and strokes
213
her hair.
Using her space-connecting powers to send the boy into a labyrinth had been an act of simple
revenge.
Revenge for having to help in healing the boy when he came in wounded yesterday. Revenge for
having to grant the request of the half-elf girl he saved.
Her plan had been to alleviate some of her sourness about the affair by pestering the boy.
Then he defeated GATE CROSSING on his first attempt.
He must not have noticed how shaken Beatrice had secretly been.
Beatrice: “Not someone I want to have anything more to do with, I suppose.”
Said Beatrice after expelling him from the Archive.
Not even Beatrice could determine how he reached the Archive in one attempt. Perhaps his affinity
was for yin magic, and he just happened to be on Beatrice's wavelength that day.
But even if he did have yin affinity, he lacked any affinity as a magician.
He'll only be staying for a few days. With that thought, Beatrice managed to ignore the
uncomfortable strain in her chest.
Puck: “Betty. Were you mean to him? Come on, don't do that. He helped Lia, so you better give him
a real apology.”
Puck showed up in the Archive the next morning to scold Beatrice for her actions, and now she had
to confront the boy she had just decided she'd stop having anything to do with.
Subaru: “She shows up, and what the hell does this loli start saying?”
Beatrice: “What I suppose is that word. I've never heard it before, and it still disgusts me, in fact.”
Subaru: “It means 'too young to go down their route'. Sides I'm not really into younger girls.”
Beatrice: “...Your extensive discourtesy to Betty loops around to be pitiable.”
Tit for tat.
She hadn't intended to apologize anyway, but this conversation completely eliminated any urge.
Beatrice passed breakfast in silence, saw Puck's rather resigned expression, and breathed a sigh of
relief. Seems like he'd forgiven her.
In exchange, it wound up that the boy would be sojourning in the mansion for the long-term.
Beatrice's desire to seriously start cursing the situation intensified, and she decided to excuse herself
and return to the Archive. The mansion came with complex circumstances and history anyway, and
right now was a state of emergency, too.
This gutless boy would give up before long.
All Beatrice had to do was endure until that happened.
Subaru: “Hey, Beatrice. Done with work so here I am to hang out.”
214
Completely oblivious to Beatrice's thoughts, the boy came parading into the Archive while looking
like a nitwit, annoying Beatrice even though she hadn't asked for any of this, and just kept doing it
whenever he found time to spare.
Beatrice could only sit there, stunned at his impudence.
There had been others qualified to enter the Archive without Beatrice's permission. But they had all
been seeking the Archive's knowledge, or seeking the powerful spirit Beatrice.
The second they opened they mouths, it'd be requests to liberate the knowledge. Or requests to
contract with Beatrice. Always.
Subaru: “Beatrice. —Mind if I pull your drills and make them sproing everywhere?”
Beatrice: “Are you trying to die, I suppose?”
Just when it looks like he's going to say something serious, it's the same crap as usual.
He had been somewhat desiccate in his first few days after waking up gaining employment in the
mansion, but after that, his overly-familiar attitude was off the charts.
...Is what Beatrice thought, when suddenly:
Subaru: “I'm stuck with no way out. Completely upfront, I'm looking for your help.”
—He noticed the first signs of the Witchbeast Affair in the forest surrounding the mansion.
With his body bathed in a witchbeast's curse, discussing de-cursing and potential origins of the
curse with Beatrice, she felt that there was something different about him compared to before.
And she simultaneously noticed:
The yin power she perceived from him, and its somewhat crooked manner of peaking.
The witchbeast affair ended without being any of Beatrice's concern, he apparently resolved his
differences with the maid sisters, and was welcomed in as a true member of the mansion.
He then went around being his jolly self, pestering her with an attitude even more over-familiar than
before, and there was that one delicious episode among others about his mystery condiment called
mayonnaise, all while Beatrice began meditating on an impossible fantasy.
—A boy who showed no great interest in the knowledge, or in Beatrice's power.
Could he be the one who Beatrice had been waiting for?
The suspicion was baseless, continuous, and exhausted her. But when she tried to deem it as a
legitimate theory, she stymied herself by opening her blank book of prophecy.
Being that the prophetic text said nothing, this boy could not be Beatrice's awaited THEY.
And he was lacking in too many ways to be Beatrice's awaited one anyway.
First, his eyes were nasty. His attitude too. He hadn't any cultured refinement, and short legs. He
regarded something else as more important than Beatrice, and was not gentle with her.
In fact she couldn't find anything good about him. It addled the mind as to what the half-elf girl and
blue-haired maid found so appealing.
215
There wasn't anything good about him, so why couldn't he just be uniformly disliked and alone?
If he was, then when he showed up in the Archive, she wouldn't hesitate to change the way she
interacted with him a little.
Is what she sometimes thought, and yet.
Roswaal: “Beatrice. I'm thinking to invite Emilia-sama and Subaru-kun to SANCTUARY.”
Said Roswaal to Beatrice after returning from the Capital.
A variety of questions whizzed through Beatrice's mind, her eyes wide. But Roswaal silenced
Beatrice's queries with a single action.
He stroked the cover of the prophetic book in his hands.
Roswaal: “...Do you understand? Beatrice.”
Beatrice: “I-I, do understand, in fact. ...Do whatever you wish, I suppose.”
Beatrice could say nothing else.
After Roswaal turned his back to her, and she learned that he was leaving for SANCTUARY in
advance, Beatrice decided that she would hole up in the Forbidden Archive and go without seeing
anyone.
The writ of Roswaal's gospel was demanding contact with SANCTUARY.
Beatrice did start having hopes for her own gospel after hearing that. But her prophecy book
contained endless pages of pure solid white as always, abandoning her heart in a wasteland.
Beatrice knew what came of Lewes Meyer's sacrifice.
She also knew that the place had gone unfreed for four centuries. And that people diverged from
demihuman races were held inside there, awaiting liberation.
And that it was a barrier the half-elf girl needed to overcome if she was aspiring for the throne.
—But what would happen to Lewes Meyer's sacrifice if the place was freed?
To Beatrice's feelings of powerless about being unable to save Lewes Meyer?
To her overwhelming sense of loss, that triggered her parting with Echidna?
Her emotions had nowhere to go. Sensing that the supposedly-frozen things had begun to pulse
again, Beatrice knew that the end to her fate was truly coming.
Beatrice did not know the details of what happened outside the mansion.
The boy returned from the Capital with a memento of someone dear from Beatrice's memories.
Seeing it, and feeling that the world had left her behind once again, Beatrice saw the boy's group off
as they left for SANCTUARY.
And, thinking that what they would bring back from SANCTUARY would be her answer, gave up.
216
※ ※ ※ ※ ※ ※ ※ ※ ※ ※ ※
Beatrice: “And so Betty has decided, in fact...!”
Before they could bring back her answer, Beatrice sensed deadly violence whipping through the
mansion.
Once she realised what was causing it, Beatrice understood that fate had truly deserted her.
Beatrice: “I won't break my promise to Mother. ...But it is meaningless to spend any more time in
this emptiness, I suppose!”
THEY would never come. But she could not stop waiting.
Meaning that Beatrice needed someone to steal the option of 'WAIT' from her.
If that meant losing her life, then she'd offer it without any hesitation.
If there was someone, anyone, who she felt she could entrust this duty to even somewhat, then she
could believe that her final wish would be granted.
So when the boy—Natsuki Subaru—burst into the Forbidden Archive this night, Beatrice's heart
was moved with more emotion than can be expressed.
It felt like fate, which had never once attempted to give Beatrice's mind solace, had finally rewarded
her.
If his hands would take her life and make her defy the promise, then even that would be—
Subaru: “I'm taking you out of here, Beatrice. —I'm dragging you out into the sunshine, where we'll
play until your dress is caked utterly brown with mud.”
—And he said this.
Beatrice: “Unwanted meddling, I suppose. Nobody asked for you to do that, in fact.”
She didn't understand. What on earth was he saying?
He had never, not even once, behaved anything like THEY before. He had never snatched her gospel
away and told her, “Sorry for the wait.”
Subaru: “Stop getting thrown around by a blank book and a four-hundred-year-old promise. —Be
the one who chooses what you want to do, Beatrice.”
Beatrice: “—”
—So then why was he, after all this time, disrupting Beatrice's heart after she had already steeled
her resolve?
I'm meeting my end, had been the only thought in her head.
She saw the boy upon his return, and hoped: I will end by his hands.
But he was trying to show her a future that diverged from her hopes.
217
This wasn't what she desired.
Her heart that could desire this hope had, over four hundred years of time, long ago withered to
nothing.
Beatrice: “I-if, you... were THEY...”
...Is what it was supposed to be, but while listening to the boy's indignant speech, something
changed in Beatrice's heart.
Her slumbering emotions shook like flowers taking bloom after winter. She raised her head.
There would be no taking this statement back, once she said it.
She was dispelling her four-hundred year obsession with her mother's binding words, and now
clinging to something entirely unrelated and new.
And though she understood that, from her mouth, the decisive words—
Beatrice: “Will... you be Betty's THEY?”
Subaru: “Are you stupid? —Of course I wouldn't be this weird mysterious THEY of yours.”
The instant he spoke it, his expression somewhat mocking, Beatrice's newly-budded hopes were
betrayed.
She doesn't really remember what happened afterwards, as she surrendered herself to anger and
expelled him from the room.
But she did know that she had said something she couldn't take back, and before it could develop
into something that couldn't be taken back, was snuffed out.
Beatrice: “—”
What an utter clown she was.
This meant that she had done nothing more than betray her mother's instructions. And her betrayal
had been barred from procuring results, degrading Beatrice's pledge into something horrendously
cheap.
Beatrice: “I'm exhausted, I suppose...”
Then all she has to do is let things proceed as she had originally intended.
It had been a mistake to consider taking his hand in the first place. That had not been the owner of a
heart so valiant that they could soil their hands for the sake of another.
That had been someone like Beatrice, constantly fretting about trivial things, indecisive and unsure,
constantly piling excuses upon excuses, the owner of a weak heart.
And so the DEATH to end Beatrice would come in a different—
Subaru: “Finally back! Hey, stupid. Stop throwing people out halfway through conversations. Now
just listen to me and—”
Beatrice: “—!”
Subaru: “Plot!?”
218
Butting in to Beatrice's contemplations, the boy bursts back into the Forbidden Archive.
The instant she sees the boy, edging on speaking something more, Beatrice's emotions seethe and
she blasts him away with a pulse of magic.
She watches him fail to endure it and shoot out of the Archive until the doors slam shut.
Their conversation had disintegrated, capped off with his decisive comment, and still. Just how
shameless was he?
Beatrice cannot comprehend how he could leave her with that statement, and then show up so
brazenly.
She puts her hand to her chest to deal with her irritation, gives a sigh, and—
Subaru: “How about cutting this out! Is this you throwing a tantrum!? If you're gonna resort to
violence first thing, the conversation's not going any—”
Beatrice: “You cut it out, in fact!”
Subaru: “Dua!”
The higher grade of magical pulse impacts his head, proceeding down to batter his torso.
Once she confirms that the screaming, tumbling boy strikes the wall outside the door, the Archive
once again severs its connection to the hallway.
She can't believe his persistence.
Is he ignorant to the concept of 'giving up'? Or does he not realise how deeply his thoughtless words
had wounded Beatrice's heart? Whichever it was, the boy is continuously rejecting GATE
CROSSING's goodbye.
Beatrice: “...This is truly no joke, I suppose.”
With that irritated mutter, Beatrice drags the stepladder over from the back of the room, and takes
her usual position opposite the door. She cradles her book of prophecy in her arms as she glares at
the portal.
—The boy would be belting that door open once again.
With his selfish logic and inconsiderate sales pitch, he would come.
Times upon times upon times, she would reject him and cast him away.
Because he was not THEY.
Because he himself had forfeited his right to take Beatrice out of here.
And so Beatrice would never, ever leave here.
She merely has to end here, alongside her unfulfilled promise.
Because that was the only thing that would now grant Beatrice solace.
※ ※ ※ ※ ※ ※ ※ ※ ※ ※ ※
219
Blasted out of the room, Subaru crashes head-first into a wall for his breathing to halt.
This is his sixth time being thrown out of the Archive after his first failure in persuading Beatrice.
He feels that all these repeated blasts in such a short timeframe have made him better at catching
himself when dealing with invisible attacks.
But Beatrice's magic pulses are beginning to feel out how intense they can go without seriously
damaging Subaru, meaning he absolutely mustn't slack.
Subaru: “This isn't the time to be polishing your stupid magic, fuck! She's not listening...”
Wiping away his sweat with his sleeve, Subaru demands that his knees get him to his feet.
He's been running constantly since yesterday, had blood shed and broken bones mended, meaning
he's physically exhausted. The utter fatigue makes his vision hazy, and the only thing keeping him
moving is willpower.
Subaru: “The fire's gonna be spreading for real around now...”
Subaru stoops himself low and turns his head this way and that, clicking his tongue, for fatigue
alone does not explain his poor vision.
The fire that killed the massive witchbeast is steadily engulfing the whole mansion.
The lower floor of the main block is nigh completely drowned in flame, and he can see plumes of
smoke wafting from the eastern and western wings too.
The spreading fire has driven most of the witchbeasts out of the mansion, so there are no monsters
to block Subaru's path as he sprints about. But the temperature inside the building is heating up like
an oven and his sweat is evaporating swiftly, his singed flesh bordering on charring at any moment.
The building will start collapsing before long, and Subaru's fate will drown to nothing in the fire.
Before that can happen, he needs to fulfil his goal and flee here with Beatrice.
But Beatrice's heart remains stubbornly closed.
Subaru: “It does help that the mansion fire's cutting down the number of doors, but...”
That's really the only conceivable benefit of the blaze.
GATE CROSSING only operates on the mansion's functional doors. So open doors or burned doors do
not apply.
The further the fire spreads, the fewer doors will potentially lead to the Archive.
Subaru: “That said, the fire's gonna cook me before the doors are cut down.”
And he doesn't want to think about what would happen if all the mansion's doors burn away.
Subaru doesn't know specifically how Beatrice's GATE CROSSING links spaces to one another.
Potentially, the incineration of the mansion may sequester Beatrice's Forbidden Archive, turning it
into a permanently isolated hyperspace.
There is one place Subaru can think of that GATE CROSSING might connect to outside of the
mansion, the laboratory with Lewes Meyer's sleeping crystal, but—
Subaru: “Would she link the mansion to there in her current mental state...?”
220
Beatrice's GATE CROSSING has sent Subaru to SANCTUARY once before.
Subaru has speculated on why this irregular event occurred.
Beatrice had emotionally detonated and forcibly expelled Subaru from the Forbidden Archive.
Her intentions strayed as she focused intensely on a 'farewell'—and her GATE CROSSING
consequently sent Subaru to the laboratory, is his idea.
That location is a symbol of sad and painful farewell for Beatrice. So perhaps that's why Subaru
was sent to SANCTUARY back then.
Making it inconceivable that Beatrice's GATE CROSSING would link to the laboratory now.
Beatrice is not focusing on 'farewell', she is focusing on 'end'.
If she loses her connection to the world, the mansion, Beatrice will reach her end.
It feels to Subaru that Beatrice's ultimate decision will be to do that.
Subaru: “I'm not letting you ever be ended like that!”
Taking a deep breath, Subaru breaks into a run while keeping low to the ground.
He leaves the previous door open and searches for the next door, batting away smoke as he
proceeds deeper into the mansion.
He hears the constant crackling of the building's structure burning in the inferno.
His skin is scorched and the boiling air threatens to sear his eyes. He endures both with a grimace.
The smoke slipping into his nose brings him near to choking, when he discovers a yet-unopened
door and pounces for the doorknob.
The blazing doorknob emits heat, and sears Subaru's hand. Already his palms are atrocious with
many ugly burns. He is quite used to gritting his teeth in agony.
With a stabbing pain piercing through his temples, he kicks the door open.
Subaru: “—”
He tumbles into the room with its cloying stench of ancient books.
He opens his mouth wide and takes a deep breath, having fallen face-up, and he glares at the dim
ceiling above.
A familiar atmosphere, and rage prickling at his skin—definitely the Forbidden Archive.
Beatrice: “You again, simply incorrigible...!”
Subaru: “Hauhh! Of, course I'm back! I'm coming here however many times it takes to kidnap you.
If you don't like it then let me drag you out of here right now! Then that'll be the end of these
exchanges!”
Beatrice: “Enough of your useless chatter, I suppose! I know that the mansion is burning, in fact! If
you don't flee outside immediately, you will simply burn to death in the fire, I suppose!”
Subaru jerks himself up, his breathing ragged as he glares at Beatrice.
She remains seated on the stepladder, her round eyes as sharp as they can get as she bares her rage
at Subaru.
221
For an instant, slight emotion dashes along the edge of those eyes, and Beatrice's lips tremble.
Beatrice: “Or... do you mean to burn dead with the mansion and Betty?”
Subaru: “Are you stupid! After everything I've said, you still don't get it!? I'm not thinking at all to
die with you! I'm here to drag you out without you dying!”
Beatrice: “—! Domineering without fail, I suppose! Leave!”
Subaru stands up, pouncing for a bookcase to bide through the first magic pulse.
He feels the gale battering him, and then a second pulse that utterly drains him of energy. He
glances up to find Beatrice with her left hand raised toward the ceiling, her face twisted in anguish
as she forces herself to smile.
Beatrice: “I pilfered your mana, in fact. You must remember this sensation, I suppose.”
Subaru: “You, little...”
Beatrice: “Should your grip on the bookshelf slacken, that is the end, in fact. Stop involving
yourself with me, I suppose!”
The moment his knees start to give out, the third pulse of magic strikes Subaru from head-on.
An invisible wall of force crashes into him. Unable to support himself, Subaru is again pushed
toward the door, proceeding to tumble and fly out the—
Subaru: “Nnngh!”
—Reaching his limbs out as far as he can, Subaru manages to catch himself on the door.
Pain runs through his limbs, and experience tells him that his arms are fractured and may be broken.
He grits his teeth and forces himself to ignore it.
Beatrice: “Wh—”
Subaru: “Go through it so many times, and even I can learn how to get through. So want to defer to
my efforts and start getting in the mood to talk?”
Beatrice: “You've lost your chance to speak with Betty, in fact. By your own actions, you are the
one who squandered it, I suppose. ...Why do you not understand that, in fact!?”
Subaru: “I don't get it, no. Since aren't you actually guilty for this as well?”
His hand against the door, Subaru gets to his feet and wipes away the blood dripping from his open
lip.
He watches how Beatrice's brows furrow in utter confusion, and slips a wry smile.
Beatrice: “What's so funny, I suppose?”
Subaru: “I just confirmed that my consecutive assault isn't fruitless. If you're seriously rejecting me,
stop with the finicky crap and just blast me away. You have the power for it. It'd be so much quicker
222
to just do that.”
Beatrice: “...You are telling me to kill you.”
Subaru: “Not that you can. That was me being a jerk. Sorry. But if you're seriously rejecting me,
then there should be easier ways for you to do it.”
Beatrice, bordering on tears, has refused to kill Subaru before.
Subaru has not advanced to a stage where he can understand what her sentiment or reasoning was
back then. So all he has is speculation. Assembled from what fragments of her past Subaru knows.
He had his suspicions, and still asked that question, astounding himself with how mean-spirited he
truly is.
But if he doesn't ask it, Beatrice won't realise.
Realise the contradiction between her thoughts and actions, and the fact of Subaru's presence here.
Subaru: “If you seriously don't want to see me, then seclude yourself in the Archive, Beatrice.”
Beatrice: “What... are you... Betty has not taken a single step out of the Forbidden Archive, in fact.
But you are forcing yourself in of your own accord, and...!”
Subaru: “Nope, that's incorrect. If you were serious about holing up in here alone, there's no
goddamn way I'd reach the place so many times in such a short timespan. Your rejection's just
superficial.”
Beatrice: “That! Is because... yes, is because you are enacting the method to cheat GATE CROSSING,
in fact. And the mansion is burning, reducing the number of doors...”
Stuck for words, Beatrice's rebuttal trails off to a weak end.
Subaru's statement has made her doubt herself. And even if not, Beatrice has lost the pillar that kept
her standing through these four hundred years, and is currently unstable.
She can no longer tell if Subaru's words are right, or if her emotions are right.
Subaru: “—”
And honestly, Subaru doesn't know either.
He has no clue why he's managed to reach Beatrice's Forbidden Archive so unfalteringly in this
short timeframe.
It may be because the mansion's doors are burning away, leaving him with fewer options.
Or maybe the emergency situation is prompting his yin abilities to showcase absurd strength, and
that's letting him defeat GATE CROSSING.
It might be that Subaru is actually correct, that Beatrice is not truly rejecting him, and the doors of
GATE CROSSING are open to him.
Subaru wishes it for it to be the latter.
But the reality is insignificant. What Natsuki Subaru needs to do here, now, is secure any possibility
of bringing Beatrice out.
223
Beatrice: “You... you! Are not Betty's THEY!”
Yells Beatrice, clutching at her skirt.
She gives up on thinking as she appeals to Subaru, howling.
Beatrice: “You said you weren't, in fact! You... you said you weren't, I suppose. If you were THEY...
even if you said it as a lie, Betty would have believed you. Even knowing it was a lie, all I could've
done was believe you, in fact.”
Subaru: “Beatrice...”
Beatrice: “But you said you weren't, I suppose. Said you weren't, said I was stupid, in fact. Why
yes, I suppose. You're correct, in fact. Betty is stupid, a stupid imbecile, who even now cannot
disregard a promise from four centuries ago... and so! Nothing you say will change that it is over, I
suppose!”
Choosing rejection, an invisible wind whips around the shouting Beatrice.
The torrent of magic gusts at her dress, at her long hair, filling the Archive with a tense and
turbulent air. Subaru senses that this is the greatest gale yet, his body shuddering in terror at the
coming strike.
His cowering heart wants to him to retreat, to flee outside the door.
He manages to suppress the urge, bites deeper into his lip, and raises his head.
To tell what must be told.
Subaru: “I...”
Beatrice: “—”
Subaru: “I'm not your THEY. I'll say it however many times. Your awaited prince isn't coming on his
white steed. Not to the end, not ever!”
Beatrice: “—! Then! Betty shall simply rot here, in fact!”
Subaru: “Not happening. I'm not letting you choose that. I saying however many times it takes for
you to change your mind. THEY isn't coming. You can't keep your promise. —But you won't be
allowed to die.”
Beatrice: “I just... hate you so much, I suppose!!”
With that, Beatrice's emotions explode.
The torrent of magic changes form as it adheres to a single goal, a white light dominating
everything in Subaru's vision.
He doesn't even have time to feel the gust of wind.
The shockwave pounds Subaru through his front and out his back, scrambling all the innards he has.
His blood flows backwards through him as everything inside him is wrung out his pores, the pain
agonizing.
224
His eyes spin, he loses his sense of balance, undergoes overwhelming vertigo, loses all perception
of sound and smell and light. This might be what humans call dying.
—But, Natsuki Subaru knows.
Subaru: “—What are you doing?”
Withstanding a nausea so intense his organs could spill out his mouth, Subaru forces himself to
speak so that his weakness is imperceptible.
The world exists underfoot, and the moment he recognizes that fact, he steadily regains his
perception. He has his limbs, has his head, his organs aren't spilling out his mouth, his soul hasn't
shed its vessel.
So what. Same thing as usual, just a near-death experience.
Natsuki Subaru is learned enough to know: this is not DEATH.
Beatrice: “You are, joking, in fact...”
His vision sways, blurry and unstable.
Regaining enough focus to somehow recognize that he is inside the Archive, he gazes at the girl in
front of him, her arms spread wide as though witnessing something unbelievable.
It's Beatrice.
Not even she can comprehend his failure to die, and the preservation of his fundamental shape.
But there's no mystery about it. Subaru knew it would turn out like this.
It is inconceivable that Beatrice would let herself kill Subaru.
Subaru: “Beatrice...”
Beatrice: “—”
His consciousness is hazy. But willpower allows him to anchor his near-forfeited mind.
The girl before him is wavering. She cannot comprehend her own self, unable to fully reject him, as
she looks at a ragged Subaru in terror.
Suspecting that his voice will reach her in this instant, he scrambles to assemble his waning
consciousness, and speaks.
Subaru: “I'm, not... your, THEY...”
Beatrice says nothing.
Subaru: “But.”
The repeated and repeated rejections put Beatrice on the verge of tears.
The conversation would usually end here. Before it can—before Beatrice's emotions can swell to
their limit—Subaru speaks.
Subaru: “I... want to be with you, Beatrice.”
225
Beatrice: “—!”
Subaru: “You're kind, and so you won't be sad, I want to be by your side.”
Beatrice: “Auh... ghh...”
Beatrice's expression twists.
It's as though she's suppressing fury, as though she's suppressing tears, as though she's struggling to
keep some utterly undocumented emotion from showing on her face.
But she swallows her words, sighs a ragged sigh, and picks up the book on the stepladder. She flips
through the pages, wrests through the pages, her fingers scrunching the paper, then gives quiet
whine.
When,
Subaru: “—Wh, at?”
Before Beatrice can take any action, Subaru's vision warps.
It has nothing to do with his hazy consciousness or deficient blood. It's a question of reality.
The Forbidden Archive is beginning to bend in front of Subaru.
The ground around him warps, the bookshelves losing their balance as they topple down one after
another. Books fall messily to the floor, instantly drowning the ground in a sea of tomes.
Even still, the world continues to bend.
The ground beneath Subaru's feet twists too, undulating like a bellows, preventing him from
maintaining his balance.
Subaru: “What... what's...!?”
Beatrice: “—”
While clinging desperately to the door, Subaru looks at Beatrice.
He finds that in this rippling room, Beatrice's surroundings alone are untouched. The stepladder she
sits on moves not an inch, supporting Beatrice's weight as she looks at Subaru.
Subaru: “—auh,”
Before Subaru can say anything, the ground beneath him tilts.
The floor under Subaru fissures open with a noise like the ripping of paper. A black space expands
from beneath the floor-tiles, unmistakably about to send him somewhere by methods other than
GATE CROSSING.
She might even be imprisoning him in some non-existent, hyper-dimensional space.
Subaru: “—Shit.”
It happens the moment he notices the hole and takes a step back.
The world slants in earnest, sending Subaru falling backwards in deference to gravity. The door's
gaping mouth swallows him, sending him back to the blazing mansion through GATE CROSSING.
Subaru: “Hhot!”
226
The heat of the wall he crashes into makes him wail.
He raises his head, to find that he has been ejected into a hallway fully engulfed in inferno. The
only thing he manages to recognize is the fact that he's in the main wing.
The flames singe him utterly as he looks at the door he just exited, and, noticing that the door's
lower half is already swallowed in flames, is stunned.
It's a miracle that GATE CROSSING even worked. He doesn't think for a second that jumping at that
door will bring him back to the Archive.
Subaru: “Fuck, ing... if, this is the main wing...”
Then he might be able to find a functional door upstairs.
Vaguely recognizing from the number of doors that this is not the uppermost floor, Subaru decides
to head for the stairway, engulfed in flames as it is.
The smoke stings his eyes, tears welling over. His lungs burn with every breath, though he manages
to keep the smog from snatching his consciousness by holding his jersey to his mouth.
Every minute counts. Like fuck he's actually going to reach the Archive—No. This isn't the time for
whining.
He cannot forget Beatrice's expression at the end.
Subaru: “Stupid idiot, making that fucking face again...”
The numbness in his limbs from Beatrice's magic pulse leaves his body.
He drags his body along, the thing more or less obeying his will, whittling at his soul as he runs for
the end of the corridor.
Beatrice's expression flickers through his mind.
It's the same face he saw in a previous loop.
When he and Beatrice faced Elsa, and the supposedly-defeated woman took Beatrice's life.
When Beatrice shoved him away to protect him, and had her stomach destroyed.
When she saw that Subaru was safe, and her body wordlessly turned to particles of light.
Subaru has not forgotten her final expression from back then.
It was not relief at having protected Subaru, nor joy at having procured her desired death, but a
grimace.
—I don't want to be alone. That kind of expression, obvious to anyone.
Subaru: “So like hell... like hell I'm gonna leave you on your own!”
With that, he leaps into the fire as he searches for escape.
He feels something squirming and wrong inside him, but the heat from his singed flesh and the pain
from his burnt skin prevent him from focusing on it.
Were Subaru an objective witness to this, he might unwittingly recoil from how repulsive it was.
Subaru, running through the fire with his pledge to bring out Beatrice, is wreathed by an
overwhelming mass of black miasma, embracing him almost like a protective vestment of shadow.
227
Oblivious to this, Subaru breaks through the wall of fire and reaches the stairway.
He gives a ragged exhale, looks at the staircase above, and recognizes that this is the second floor.
He proceeds to climb the staircase, thinking to dash straight for the uppermost floor—when.
Subaru: “—”
He hears the noise of something wet being dragged across the ground, and looks down.
The noise is coming from downstairs. His rationality tells him that this is impossible.
All he can hear around him is the crackling and booming of the burning building.
This is a mansion seconds from collapse, and that is the first floor of the main wing, where the
inferno started. Nothing should be moving down there.
Subaru's sprinting all through the mansion means he knows this conflagration, which even the
witchbeasts fled.
So this noise has to be a hallucination.
—But if it is, then what's that?
Subaru: “...No way.”
While dragging something along with it, a silhouette emerges from the flames.
It is destined for the upstairs as it climbs the staircase as Subaru had, stopping at the landing
between the first and second floor—and looks up as it notices Subaru's presence directly above it.
The silhouette is wearing black clothes, holds a black knife, has black hair, and is a woman.
Subaru: “Elsa...?”
Elsa?: “—”
The silhouette doesn't respond. But this definitely looks like the black-garbed woman Subaru
knows.
Why is she here? Could Garfiel somehow have lost? If so, then Subaru's battle—Subaru's battle to
save everything—has ended in defeat, and,
Subaru: “No, I'm off...”
Just as he starts getting those ideas in his mind, Subaru shakes his head.
Subaru has to trust in Garfiel's strength. Even supposing that his opponent was strong, Subaru was
betting on Garfiel to win.
Otto and Frederica had done everything they could to assist in evacuating Petra and Rem.
Garfiel would have done his absolute best as well.
How would Natsuki Subaru have possibly gotten this far without believing in his companions?
Subaru: “Garfiel wouldn't have lost. So, why're you...”
228
Believing in Garfiel's valiant fight, Subaru flings words at the silhouette below him.
This woman shouldn't be here. What is underlying her actions?
But just when he goes to question her, Subaru notices something.
Or no. He's forced to notice.
Subaru: “—You're not Elsa any more, are you?”
The dark eyes looking up at Subaru shine with not a speck of light.
The things are so hollow and empty that it's unbelievable that those are eyeballs in those sockets.
The noise is coming from the crushed lower body of the silhouette, dragging along behind it. But
the thing still acts like it's alive, which Subaru finds incredibly repulsive.
Subaru did think she had life force enough that she wouldn't die, but she's still incapable of dying
after all that destruction?
Subaru: “Though, this isn't the time to be pitying her...!”
Even supposing she's incapable of dying, Subaru has no words of sympathy.
Considering the fact that Elsa showed up before being half-dead, sympathy would be lenient
treatment even despite her state. That said, Subaru doesn't make a hobby of tormenting walking
corpses.
He rationalizes that she just needs to get caught in the mansion's collapse, and have the flames
cremate her.
Subaru: “Get swallowed in inferno. I'm leaving to get Beatr—”
Shaking his head, Subaru disregards the silhouette and determines to head upstairs.
Subaru: “—Huh?”
With a slight noise, the silhouette leaps.
Its mouth gapes open as it aims for Subaru, swinging its wicked blade.
Subaru: “—”
The wind from the knife as it grazes past his nose makes Subaru's lungs forget to breathe and heart
forget to beat.
The thing just tried to take Subaru's life, so natural that it may as well have been walking over to
him.
But its strike just barely misses Subaru, instead shattering the floor before the tips of his toes.
The enemy hadn't been going on easy on him, its dead lower half had simply lacked the leg strength
needed to pounce. If it had that leg strength, that attack would have killed Subaru.
Subaru: “You've gotta be kidding!”
He promptly kicks the silhouette as it pitches forward before ascending the staircase.
He dashes so intently that he forgets to breathe, glancing back at the shadow. The silhouette's head
229
sways from the kick and it jerks its limbs awkwardly to the ground like a marionette, then scuttling
like a spider in pursuit of Subaru.
Subaru: “Are you joking!?”
He had called her a spider-woman before, but he didn't think she actually was one.
Stunned at her inhuman locomotion, Subaru soars to the top of the stairway. He imagines the
silhouette pursuing him as he dives into the inferno of the third floor hallway.
In the very middle of this hall is the office. That room, being the sturdiest in the mansion, should
still be generally undestroyed—
???: “—σσσ!!”
Subaru: “Dhhah!?”
Intercepting Subaru as he leaps into the blaze, a lion-headed witchbeast roars.
Having lost its mane, and with over half of its body burned grotesquely, this is unmistakably the
witchbeast that Subaru's team supposedly killed in the dining room.
Apparently the near-dead beast returned to this door in adherence with its master's orders.
Meaning that Subaru is presently a moth darting into a flame.
An unanticipated meeting amidst fire. The pun is working disgustingly well.6
The half-burnt witchbeast swings its foreleg what with those giant claws. The attack grinds away at
the wall, closing in to strike Subaru's neck, more than strong enough to mow Subaru down easier
than a weed despite the beast's moribund state.
Subaru: “You're one-trick ponies!”
But Subaru dodges by ducking low and diving forward.
Subaru has learned from the other witchbeasts that they aim for their prey's vitals. Judging that the
beast will definitely aim for the head, Subaru dives into a forward roll to slip past the beast's flank.
This beast, fully capable of devouring Subaru in one gulp, roars in rage as it attempts to readjust
itself and face Subaru. But things will not come so easy.
Beast: “—σσσσ!!”
In pursuit of Subaru, the skittering silhouette bares its fangs at the half-dead witchbeast.
The beast, its back turned, is slow to react as the silhouette’s flourished blade showers a slash down
upon it. The beast's rear left leg is amputated at the joint, blood pouring from the crooked wound as
the creature's shrieks echo through the corridor.
The beast whips its snakelike tail, striking for the silhouette that crawls across the ground.
The silhouette avoids it nightmarishly, manoeuvring beyond human capacity to bat the beast's tail
away with its blade, stab its knife into the beast's open wound, and bore deep into the injury.
6 飛􀈨􀅚 火􀈀い􀈠夏􀈃虫􀅛 􀈄􀛇神聖􀛕まǸ􀅙ち􀈘􀈨􀅛 いうバンゼ􀈃曲􀛏神様􀛧􀈡􀅚 􀈄酷いな􀈟􀛐􀅚 出􀈠面
白い諺􀅚 􀛣􀛈意味􀈄􀛇􀛏ない􀈗知􀈞􀛤􀈀こいǹ􀛖自􀈞死􀈁􀛨ｗｗ􀛐􀛈読􀈖􀈠な􀈞􀛕まǸ􀅙ち􀈘􀈨􀈧聴く
􀅛 いい􀛈読􀈖ないな􀈞􀛕まǸ􀅙ち􀈘􀈨􀈧聴く􀅛 いい􀛈􀛕まǸ􀅙ち􀈘􀈨いい􀛈
230
Subaru listens to the earsplitting screech resound as he heads for the office's door, certain not to let
the opportunity escape.
He kicks the record room's door open on his way, but it fails to lead to the archive, instead leading
only to time loss. The beast and silhouette are still fighting behind him, but being that the only
howls he hears are from the beast, it's obvious how the scales are falling.
Subaru: “Beatrice!”
Having reached the office, Subaru prays to himself as he belts the door open.
If the Archive appears before him, he can say goodbye to the monster battle.
But what cruelly shows it self is only the sight of the dishevelled office.
Subaru: “Fuck... Then this wasn't it!”
Practically illustrating the strength of Beatrice's rejection, the office diverges from Subaru's wishes.
He can no longer search for other doors, or return to the lower floors of the burning mansion. If
there are any potential doors left, they'd be—
Subaru: “The hidden passage...”
It's difficult to call the hidden passage, which opens via a mechanism, a 'door.'
The passage opens by way of a sliding bookcase, and it's rather unlikely that passing through its
entrance would lead him to the Forbidden Archive.
If there are any other doors left, they'd be deeper inside the passage.
Subaru: “There should be a door midway through the passage that opens to a small room... but...”
In a previous loop, Elsa ambushed him from beyond that door.
But he doesn't know if that door falls within GATE CROSSING's area of effect. And above all, Subaru
has to think that this is Beatrice's doing, leading him from door to door to try and expel him from the
mansion through the hidden passage.
She may be aware of the mansion's current state, and be leading Subaru down a route that will give
him survival.
In that case, the hidden passage may not even lead to the Forbidden Archive.
He may be led outside the mansion, to the mountain cabin at the end of the escape tunnel, and
forever lose his chance to save Beatrice.
Subaru: “—Not giving me any time to think!”
Subaru hears the beast's death wail as the decisive blow is struck.
The witchbeast, which unwittingly put in a valiant fight to buy Subaru time, has most likely died for
real to Elsa's silhouette.
With a shake of his head, Subaru dives into the hidden passage.
A spiral staircase lengthy enough to reach the mansion's underground welcomes him—and it seems
that the inferno has reached even this tunnel, the heat and smoke precluding anyone from doing
anything here.
Subaru puts his hand to his chest to cope with the aching, steeling his resolve as he speeds straight
231
down the staircase. Descending right after ascending. The heat simmers him, and just imagining
what colour his skin must be makes for a terrifying thought.
After eventually reaching the end of the staircase, Subaru peers into the darkness of the passage, his
breathing ragged.
It seems like the smoke had been leaking in from a gap in the stairway wall, for he sees no effects of
heat or fire in the subterranean passage.
Instead of the threat of burning, Subaru has to deal with fumbling in pitch darkness.
He walks in deeper for another ten or so meters before reaching a somewhat wider space, finds the
door to the small room he's looking for, and stops.
Subaru: “Here...”
Subaru has never gone deeper into the hidden passage than this door. He doesn't know if any other
doors exist beyond this door.
Meaning that this is potentially Subaru's last chance for a door to lead to Beatrice. And if this place
functions as a proper hidden passage—
Subaru: “—”
Shaking his head to dispel his weakness of heart, Subaru reaches for the doorknob.
If Beatrice has lead Subaru here with intention for him to survive, then his chances here are poor.
Subaru fearfully touches the doorknob—
Subaru: “Hhht! This door's another...”
Crying in pain as his hand burns, Subaru grimaces and glares at the door.
The door's response, as if it had reflected Subaru's heart, makes a wave of disquiet surge up in him
and—he notices it.
Subaru: “The doorknob's, hot...?”
While the underground passage may be heated, there are no signs of fire.
The smoke and heat had likely been leaking in through a gap in the stonework that composes the
staircase. If Subaru's speculation is correct, then it's inconceivable that this door would be so hot.
This door is hot enough that you have to wonder if it's indeed been seared by flames.
Subaru: “...Beatrice. If you can hear this, please listen.”
Taking care not to touch the door, Subaru looks slightly upwards and mutters.
With belief that his voice will reach the absent girl.
Subaru: “Did you lead me here? If you did, knowing that the only escape route is through this
hidden passage, then honestly I'm speechless at what a schemer you are.”
Beatrice's tactics to lead Subaru this far were indeed quite considerable.
The encounter with Elsa's shadow and the witchbeast surely had nothing to do with Beatrice, but
she definitely led Subaru here move by move.
232
If he proceeds to open this door and reach the mountain cabin, Beatrice's plans will likely be
fulfilled.
Subaru: “But apparently thing won't go so smoothly. ...I could open this door, but I won't manage to
escape how you want me to. This isn't me being stubborn and insisting that I don't want to run away,
okay? I'm at least half in that mood, yes, but... it's something more serious.”
Addressing someone who might not even be listening, Subaru smoothly strings word after word.
He taps his nails against the door blocking the way before him and gives a sigh.
Subaru: “If I open this door, I'm probably dead. You and the others might not notice this, but right
now, that's how things are on the other side of this door. It's hard to explain verbally... but I
understand the soul of science and I can tell.”
Setting aside the failure in the dining room, Subaru's 21st-century knowledge is howling at him.
This door Subaru is presently looking at is a door commonly found during fire-related emergencies,
and must not be touched.
No joke at all, Subaru's life is in danger.
What comes next is a question of whether Beatrice is listening. And if she is, will she believe what
he's saying?
Subaru: “Beatrice. I'm going to open the door. —I'm leaving how you judge my statements up to
you.”
Although aware that this thing before him is a threat to his life, Subaru's heart is rather calm.
It's not that his nerves are steeled, or that he's resolved himself.
It's that he can calmly entrust his life to another.
I mean, after all.
Subaru: “—Beatrice, I trust you.”
With his hand burning in pain, Subaru flings open the door.
And—
※ ※ ※ ※ ※ ※ ※ ※ ※ ※ ※
Rather than climb down the spiral staircase, the shadow reaches the bottom via something closer to
'plummeting'.
Shadow: “—”
The blood flowing from the shadow is clouded like muddy water, its visage as it drags its crushed
legs along so ghastly it does not look a thing of this earth. With a wicked black blade in its right
hand, and the dead witchbeast's heart in its left, the shadow clenches its fist to crush the organ as it
proceeds deeper down the passage.
233
The skulking shadow has a human's shape, but not even it can determine whether or not it possesses
human will.
Its body has been destroyed such that it cannot function, its life has been whittled such that it cannot
revive, and it has already exhausted the absolute dregs of its vitality as a shadow.
If you asked how the silhouette could regardless be moving around like this, then the shadow would
respond: because its personality before it was a shadow was just that intensely tenacious.
The shadow eventually, silently, reaches the deepest part of the passage.
The shadow lacks a will, and possess no goal other than to corner anything moving and take their
lives. Sensing that its mark has gone through here, the shadow gives an easy flourish of its wicked
blade.
Shadow: “—”
With a clunk, the door in front of the shadow splits apart.
The shadow kicks the door's debris aside, and moves to peer into the darkness beyond,
Shadow: “—”
A slight wind breezes by, making the shadow feel that they are being sucked into the darkness.
White smoke overflows from deep in the darkness, and a haze begins to form before the shadow.
And then—oxygen flows into the room where incomplete combustion occurred, mingling with the
traces of the fire, instantly superheating and bursting out of the room.
Backdraft.
There's no way that the shadow, a dimwitted thing moving only to destroy, could have anticipated
the explosive phenomenon.
Shadow: “—”
The burst of flames engulfs the shadow, hellfire burning its body to nothing.
The shadow's body had lost means to either restore or revive itself, waiting only to rot, when
incinerating fires envelop it, exceeding carbonization as the blaze peaks instantly hotter—and burns
it to nothing.
The fire's momentum does not stop with merely the shadow as it proceeds to zoom through the
underground passage, transforming the spiral staircase into a sea of searing heat, and gusts into the
office to explode for even greater conflagration.
—The Roswaal Mansion now truly collapses as it meets its moment of demise.
※ ※ ※ ※ ※ ※ ※ ※ ※ ※ ※
Seeing how the Forbidden Archive has changed, Subaru swallows his breath.
234
Fissures run through the floor near the entryway, the hole to the hyper-dimensional space still alive
and well. The fallen bookcases have no hopes of recovery, and in fact a portion of the room is up in
flames.
The situation in the Roswaal Mansion has starting affecting the Forbidden Archive too.
Subaru: “—”
But, noticing the gaze fixed upon him, Subaru suppresses his shock and changes his gears.
For now, he shall focus everything on only one single girl.
—For this is surely his last chance.
Beatrice: “You're an idiot, in fact...”
Subaru: “That's seriously the first thing you say?”
Beatrice: “Well you are, I suppose. Betty put in so much effort so that you might escape, then you
squander the opportunity, and come back, in fact. ...The mansion no longer has any doors, I
suppose. The Forbidden Archive has caught aflame too, in fact.”
She's right.
The fire spreads to some of the fallen bookcases, turning the beloved books one by one into ash.
This entire place is flammable, and it's going to burn in a flash.
Subaru: “Which means this'll be the end both for me and for you.”
Beatrice: “...Yes. It's the end, I suppose. There is not much that Betty desires any longer. The fire
has spread to the knowledge destined for THEY, which utterly defies the promise, I suppose.”
Subaru: “Does it. Then, I want you to listen to my final speech.”
Beatrice's empty eyes look at Subaru.
She says nothing to encourage or refuse him, but the reaction probably means that she's at least
willing to listen. Subaru gives her a nod, and takes a small breath.
The words he hadn't managed to tell her before, at their previous parting.
Right now, he will tell her everything he wishes to tell, in full.
Subaru: “Beatrice. —Help me.”
Beatrice: “...Huh?”
Assertion, spoken with chest held high.
Shock dashes through Beatrice's eyes in response to sooty-faced Subaru's declaration.
She had surely attempted to imagine what he would say.
While drawing near to her unavoidable end, Beatrice had definitely run many simulations of what
words Subaru would accost her with.
235
I want to save you. I won't let you be alone. Perhaps those manly words, and the cool greeting she
had expected from THEY, where what she had been waiting for.
But if Subaru is to communicate his true feelings, such statements are impossible for him.
Subaru: “So I've been considering how I'm saying this cool stuff like, 'I'm bringing you out of
isolation', or 'I'm going to save you'. ...Really, they're all I could come up with while riding off
momentum to get through the situation. So I've been sincerely considering. What is it I think of
you? What do I think of you, and what do I want to communicate to you?”
Subaru presents his sincere, unadorned thoughts to the wordless Beatrice.
While turning a blind eye to how cowardly and unfair it is that he's leaving the reception of all this
up to her.
Subaru: “This whole me saving you thing's a joke, the truth of it is, you don't need my help at all.
You're strong, you're smart, you're cute... you can do anything you put your mind to, and can get
done anything you want done.”
Beatrice: “—”
Subaru: “You are more than capable enough of living on your own. Of course. If you weren't then
you wouldn'tve managed four hundred years. So not a word of this stuff about helping you or saving
you resounded with you.”
Beatrice: “—”
Subaru: “But even though you're strong and smart and can do so many things, it scared you to live
on your own. It hurt you. It made you lonely. Nobody can fault you for clinging to THEY.”
Beatrice: “After you rejected... Betty's feelings... what could you... possibly understand!”
Biting her lip, Beatrice glares at Subaru with something like hatred.
But that wavering emotion fails to fully be hatred. Beatrice holds on to that fading fury, frantically
trying to preserve it as Subaru shakes his head at her.
Subaru: “I do know. That you're kind. That when someone's having nightmares, you'll hold their
hand to ease them. That when someone's in unworkable trouble, you'll offer your hand and open a
path. That when someone you can't help hating loses someone close to them, you'll lament for
them.”
Beatrice: “Talking as if, you know anything...”
Subaru: “I'm powerless. I can't be any help to you. But if we're gonna say there's anything I can do,
not wanting you to be alone, then it's only cling and beg.”
Beatrice's eyes widen. Subaru presents his right hand.
It's raw with burn scars, disgusting to look at. But it's still better than his atrocious left hand after all
the damage it took.
He wipes it, prepares it, makes it clean enough to suitably hold her hand.
236
Subaru: “Beatrice. Help me.”
Beatrice: “—”
Subaru: “I won't be able to live with the loneliness without you. Help me.”
To a third-party listener, it would sound an overwhelmingly pathetic and shameful form of coercion.
I can't live without you, so please take my hand, is his threat.
He cannot do anything for the other, so he is teaching the other that they can do something for him,
and by that rationale, demanding that they live.
It's an excessively selfish, unreasonable, and hopeless means of coercion.
Beatrice: “Not, fair... it isn't fair, in fact.”
Subaru says nothing.
Beatrice: “Using, those words... and, saying it so... after all this, you... when you're not THEY... when
you rejected Betty, and yet...”
She is tongue-tied, lost for words, hesitant to speak, emotional, and anguished.
Her eyes remain set on the hand presented to her as she firmly embraces the book in her arms.
Tears spill from her eyes.
Beatrice: “I was alone for four hundred years! I spent all that time in isolation, so what could taking
your hand now, possibly... you'll just die anyway! Human lifespans pass like a blink of the eye to
Betty... after all of this! How could I cling to this!”
Subaru: “It's impossible for me to imagine your four hundred years. I can't talk like I understand it,
either. Four centuries, I haven't even lived a twentieth of that. I know I can't understand all of your
fear for what'll come after I die.”
Beatrice: “Then! Then... nothing you've said, presents any solution...!”
Subaru: “But, tomorrow, we can be holding hands.”
Beatrice: “—”
Subaru: “Tomorrow, and the day after, and the day after that too. It might not be four hundred years,
but we can spend our days together. It might not last for eternity, but tomorrow, and in this present, I
can treasure you.”
Beatrice: “—hk”
Subaru: “Beatrice. —Choose me.”
Subaru has already chosen.
Now he presents the choice to Beatrice. It all rests on her.
237
Will she stay loyal to her mother, and punctuate four centuries by being swallowed in flames?
Will she disregard her promise to her mother, abandon her meeting with THEY, and take Natsuki
Subaru's hand?
Beatrice: “Y-you are, THEY is...”
Subaru: “Not me. Don't equate me to some other guy you built up in your head. I'm me. Natsuki
Subaru. Take all your unreciprocated feelings for this four-hundred-year asshole you've never even
seen, and dump them.”
Beatrice: “—”
Subaru: “Rather than fear a goodbye that might someday come, live with me in a definite tomorrow.
I'm weak, but I'm still aiming so high... if we're together, you'll be so busy fussing over me you'll
stop having time to think about being bored or lonely.”
Beatrice: “...nng,”
Subaru: “Choose me, Beatrice.”
He'll repeat it however many times it takes for the words to reach her.
Because he understands her wavering feelings, and her wavering heart.
So that the selfishness of Natsuki Subaru can shoulder the burden of her guilt for her indecision, and
shame for breaking the promise.
So that this girl will never cry alone again.
Beatrice: “But you'll go away...”
Subaru: “It won't last forever. The future you're fearing will definitely come. The time when you're
left behind, eternal as you are, will almost definitely come. But if you think only of fear for
farewells, and throw away all the fun of being together, it takes far too much out of both of our
lives.”
Beatrice: “But you'll leave me...”
Subaru: “Let's be together. Let's live together. Let's go together. Let's pile memories upon memories,
enough to blast away your fears of goodbye, enough that you can smile and say with your chest
held high: I enjoyed it. Enough that you recover those four centuries you spent in solitude, and
counterbalance them.”
Beatrice: “Even if... that happened! I'll be alone, someday!”
He steps forward. Closes the distance.
The girl's wavering eyes reflect him.
He looks pathetic, he looks deplorable, he's a far cry from the prince she's been waiting for.
But right there is usual, mundane Natsuki Subaru.
238
Subaru: “You'll live forever, and the time you spend with me might only be a microsecond for you.
So I'll carve it into your soul. My microsecond.”
Beatrice: “—”
Subaru: “—That Natsuki Subaru was a man, who even through eternity, was too vivid to ever fade
to sepia!”
The Forbidden Archive crumbles to the sound of shattering glass.
The area around Subaru and Beatrice is surrounded in spacial fissures and scorching flames.
But in this second, he feels not fear nor fire.
The only thing in Subaru is Beatrice.
And the only thing in Beatrice is Subaru.
Beatrice's shaking hands clutch the book received from her mother.
With belief that unhooking her fingers means mending her centuries of solitude, Subaru reaches out
his hand.
And shouts.
Subaru: “Choose me! Beatrice!!”
Beatrice: “—auh,”
Subaru: “You want someone to take you outside! That's why you are always! Sitting opposite the
goddamn door!!”
With the decisive boom, the world meets its end.
The Forbidden Archive, the girl's isolated cage, is swallowed and disappears in rifts and fire.
But the instant before that happens.
—A single book thunks to the floor of the Forbidden Archive.
※ ※ ※ ※ ※ ※ ※ ※ ※ ※ ※
Having escaped through the hidden passage and reached the mountain cabin, Otto's group watches
the mansion burn from atop a hillock.
Otto, Petra, and Frederica. And Rem shouldered on Frederica's back. The four of them succeeded in
safely evacuating through the passage to the mountains.
The mountains, and particularly the area around the cabin, apparently have a barrier around them to
repel witchbeasts. They see no signs of either wild witchbeasts or witchbeasts in ambush in their
vicinity.
But not a single person here has the composure to rejoice about their survival.
239
All of them gaze at the mansion with something like a prayer, waiting for visible change to occur.
While trusting in the safety of Subaru and Garfiel, both still inside.
Otto: “—”
Putting the treatment of his wounds aside for later, Otto gazes at the mansion, regretting even to
blink. Petra stands beside him, clutching her arms with a strength inconceivable by her youth.
She's worried, so worried, so worried it's unbearable. Everyone knows that the young girl feels great
fondness for Subaru. Considering her grief, it's impossible that Otto not pray for Subaru's safety.
Otto: “—”
Otto gently places his hand atop her head to calm her.
He gives her a smile as she looks up at him in surprise, before returning his gaze to the mansion.
And he notices it.
Otto: “...There.”
In the middle of the burning mansion's main wing.
A massive explosion of flame bursts from the office with the hidden passage that Otto's group used.
The windows shatter, overflowing inferno spreading everywhere in an instant, before the mansion
loses its shape—and collapses.
Petra: “Auh...”
Otto hears Petra's cry of grief.
And Otto, too, having witnessed the same reality and figured the same thing as Petra, withstands the
urge to scream in denial. If he throws a fit here, it will be a disservice to the heart of the girl who
most likely wants to cry even more than him.
But Otto's thoughts are instantly invalidated.
Petra: “Otto-san, look!”
Otto: “Adagh!?”
Just when Otto borders on lowering his gaze, Petra's little hand slaps him across the cheek.
The impact startles him, sending sparks across his vision and dizzying him. But he soon sees Petra's
look of elation as she points at the mansion, hurriedly looks over as well, and understands.
Otto: “Hah, hahaha...”
—A pillar of white light is extending from the destroyed mansion to the heavens.
The light twists like a rainbow, changing its angle high in the sky, shooting far to the east.
Practically announcing that its destination lies there.
Otto knows what rests in that direction.
So his cheeks relax as he watches Petra cheer in joy, and,
240
Otto: “Now it's all up to you. —Truly, I am exhausted.”
※ ※ ※ ※ ※ ※ ※ ※ ※ ※ ※
Meanwhile, that same light that brought Otto relief is witnessed by Garfiel, half-naked and clad in
only a cloth around his waist. He clicks his fangs.
Garfiel: “Ha! So y'did pull it off, Captain! Knew ya'd do it! 'S a POSTHUMOUSLY TOO HOSHIN
KEEPS HIS PROMISES!”
Having escaped the burning mansion and sprinted into the woods, Garfiel puts his hand to his hip
and laughs like an idiot.
Lying on the ground beside Garfiel is a girl, her limbs bound in restraints made of the same cloth as
Garfiel's waistwrap—Mei Lee, unconscious.
Spoils of war! Is not how he's going to boast about it, but she's a living witness who was involved in
the attack, and there are many things they need to interrogate her about.
But above all, Garfiel's principles would not allow him to kill the young girl.
Garfiel: “'Said, th'shadow lady must'a been burnt t'a crisp.”
Garfiel gazes at the destroyed mansion, sighing.
He threw a witchbeast at her which crushed her—it's an indirect method that left no feeling in his
own hands, but Garfiel still did choose of his own volition to butcher a near-human life.
His fingers shake, and he can feel a wrenching pain in his stomach.
But Garfiel suppresses those feelings with a shake of his head, seating himself beside the sleeping
Mei Lee before leaning against a tree.
Garfiel: “F'now we'll put off th'aftertaste'v winnin' and th'feelin' of killin'. Nothin' my amazin' self
does now 's gonna accomplish anythin'. ...Countin' on you, Captain.”
Thrusting out his fist, Garfiel glares at the trail of white light, and:
Garfiel: “Once this's all cleaned up, we got a guy we both gotta give a good smack 'cross th'face!”
※ ※ ※ ※ ※ ※ ※ ※ ※ ※ ※
—She's been caught.
She knew this would happen, and she still grasped for it.
Even though she's known forever that, should she take this hand, should she cling to this warmth,
she would never be able to return to her nights of isolation and solitude.
Even though she'd admonished herself about how insanely foolish it was to live while depending on
241
an ephemeral warmth.
That voice, calling for her.
Those eyes, gazing at her.
Those hands, requiring her.
Even though she'd known how she could not possibly refuse.
—Subaru.
“Yes, that's it.”
—Subaru, Subaru.
“Yes. That's my name.”
—Subaru, Subaru, Subaru.
—Subaru!!
“And you finally called me by it.”
※ ※ ※ ※ ※ ※ ※ ※ ※ ※ ※
—The blizzard rages.
Blinding curtains of white unfurl, every puff of breath freezing the instant it touches the outside air
of this gelid world.
The breeze bathing her is frigid, and the blizzard winds carry snow so sharp it nigh cuts the skin.
But even amidst this ferocious storm, the girl with her silver hair fluttering holds strong willpower
in her amethyst eyes, and faces forward.
“I'm never, never... going to let you take anyone!!”
A glow cases her arms as she stretches them out, and unleashes a massive volume of magical power.
The blizzard amplifies the glacial magic that wreathes itself in pale light, which then slices through
the world like an incandescent sword, one-by-one slashing apart the white witchbeasts passing
overhead.
The unpleasant noise of their chittering fangs peals without end.
The embodiment of hunger—an ancient calamity beyond any salvation, specialized only to devour
its prey, something with which no-one could coexist.
Faced with the multiplying malice of 'hunger' there stands, not retreating a single step, the silverhaired
girl.
242
But her breathing is ragged, and she has lost some control over her gargantuan mana, with white
crystal beginning to cover her lower body.
If this continues, she will soon transform herself into an ice statue.
But, even though she knows this, she cannot retreat.
“—”
The girl glances behind her.
There rests everything that she must protect from the witchbeast's slaughter.
A dilapidated ruin, and several lives who are placing their hopes upon her small shoulders.
And a man, having not entered the ruin, who dazedly observes the girl's battle, and a dead-still pinkhaired
girl in his arms.
Half her body feels frozen. But a fire blazes in her heart.
Who could possibly winge and whine after witnessing them?
For what purpose, and with whose confidence, is she standing here?
“I... I won't let you be the end to anybody! Everybody's hands were linked together... and I'm going
to protect that! That is what I promised my Mother!”
A torrent of pale light crashes into the horde of approaching witchbeasts.
They cry no death wails, falling motionless amid the white gleam. They witness their companions'
sad deaths, before instantly choosing to cannibalize them and chewing into ice.
It's terrible to watch.
But perhaps, potentially, that's what people look like too when they're clinging to hope.
Even so. Even so.
“So long as I haven't forgotten about Mother and Juice, and about everybody today... and about
what he wrote for me, I am never giving up.”
Even if she does end up encased in ice, she will never regret it.
Cutting through the blizzard, the encroaching witchbeasts grow steadily and steadily nearer, closing
in on the girl and those relying on her.
If she has to, she is resolved to give her life.
But just when the girl is tormented with that thought, she hears a voice.
“No need to push yourself so hard, Emilia-tan.”
“—”
She knows that someone has just landed beside her, having descended from high above.
She looks aside. The blizzard blusters too strong, and she cannot make out their face through the
veil of white.
243
But she knows exactly who this is.
Their voice, their attitude, and above all, the fact that they would always come for her whenever she
most wanted them.
“You can hold off and fall back. —The inaugural battle of deliverance is here.”
“I'm sorry. That kind of went over my head.”
It feels like they're smiling.
The silhouette begins to walk, immediately followed by another, smaller silhouette.
She hears a second voice.
That sounds lively, as if the speaker's been waiting for a very, very long time for this moment—
“What comes next is a complete unknown, in fact.”
“Yeah, we'll be doing something about this. —Together, me and you!!”
Spirit Beatrice and Contractor Natsuki Subaru, two people who will from now on engage in battles
upon battles while linked hand in hand, commence their inaugural fight here.
244
CHAPTER 124B: YOU REFLECTED IN THE MIRROR
While facing the witch who stares back at her from the mirror, Emilia sighs.
Composed solely of monochrome black and white, the WITCH OF GREED, Echidna.
Having discovered Echidna in this dreamworld reproduction of her room, Emilia keenly feels that
this truly is a place constructed from her own head.
A peaceful, tranquil, kind world where her life in the forest continued forever.
A world where she could spend her days alongside Fortuna's, Juice's, Arch's, and everbody's smiles.
Emilia: “But that world doesn't exist, does it...”
Echidna: “Utterly not. This is a false world constructed with your memories and wishes as the basis.
However, the world-arranging algorithms that precede over the TRIAL transcend human knowledge.
The people you see in this world are most exactly who they would have been, had there been just one
flick of the switch.”
Emilia has just remembered the truth the day of behind Elior Forest's freezing.
Had there been no casualties back then, and the forest's tranquillity have been preserved, their lives
would have been ones where everyone smiled.
The sight of Fortuna and Juice, seated jovially at the dinner table, has seared itself into Emilia's
mind.
It is exactly the scene that young Emilia had wished to see from the bottom of her heart, and equally
was so for the present Emilia, with her memories restored.
Echidna: “Has witnessing the uncomeatable present made you want to submerse in this world?”
As if peering into Emilia's heart, Echidna assaults her with sweet temptation.
Emilia raises her head. Echidna gazes back, her eyes as cold as her voice. She strokes her snowwhite
hair, letting it flow over her shoulder and down her back.
Echidna: “Your mother, and that goodman. Does witnessing their happiness give you no desire for
this to continue forever? I'm sure you've thought it pleasant and so dreamed of spending your days
with everyone in the forest, and of your friends being so familiar with you.”
Emilia: “...What are you trying to say?”
Echidna: “Just some resentment, or something like it. That you've found me means that you've
already reached your answer regarding this world. And I know that this answer of yours is to choose
reality over dream, and exceedingly dull. If we're going to be seeing results regardless, I may as
well leave some faint indentations behind.”
Emilia: “—”
Echidna: “Rather than the happiness of your mother and your peers, you elect for a reality where
they met unfortunate demise. The result of your TRIAL is: you are ultimately a wretched woman
who prioritises herself over others.”
245
Echidna's fierce criticism lances through Emilia's chest.
Her words are so cutting that Emilia feels pain, and though she has not actually been stabbed, she
puts her hand to her chest and impulsively retreats a step.
Emilia's reaction makes Echidna snort.
Echidna: “So long as that's given you some self-awareness. Anyway, the TRIAL doesn't take the
personality of its challengers into consideration. So long as they're qualified, be they a hopeless
moral bankrupt, or be they a conglomerate of egotistic narcissism, the TRIAL will accept them
equally. Rest assured. You'll achieve your goals in short time.”
Emilia: “It's sooo... sore a spot you're going for. Are you like this with everyone?”
Echidna: “Not at all.”
Echidna shrugs in response to Emilia's strained statement.
Echidna: “Other than you, there's only two people in the world who I interact with spitefully.”
Emilia: “It doesn't make me happy at all to be chosen for that world three. ...I don't remember ever
doing anything that would make you hate me that much.”
Echidna: “There's no need to look so worried. My hatred for you has nothing to do with you being a
half-elf. It isn't a question of your pedigree. With no connection to blood or nature, I just hate
you. ...Or no, that may not be strictly correct.”
Emilia: “—?”
Echidna lowers her gaze, feeling something off about the latter half of her statement. Emilia
furrows her brows at the brooding witch, before giving a small shake of the head.
There's no way she can turn tail and just leave those previous comments sitting there.
Echidna has said so many things that need to be invalidated. Not only for Emilia's sake, but for the
honour of everyone in the forest.
Emilia: “I don't think there's much to do about you hating me. I know how hard it is for absolutely
everyone to like you. Since so many people have told me they hate me.”
Echidna: “If that's the case then it would've been nice of you to show some prudence and stay in the
forest.”
Emilia: “Well I'm not going to do that. I'm sure I said it in the last TRIAL. I'm going to melt the ice
and save everybody. Then I'm going to hold my chest high and teach everyone that now, the world's
an easier place to roam.”
Echidna: “Easier to roam. What a brazen lie. Discrimination between races remains great, and
people cannot easily accept those who differ from themselves. Which is why places like
SANCTUARY retain their function even today. The disagreements you're referring to will forever
result in compounding casualties throughout the world. Am I wrong?”
Emilia: “...You're not wrong.”
246
Echidna's severe comments put Emilia on the border of pessimism.
Emilia still remembers the days she spent with Puck in the forest. How the nearby villages feared
her, and showered her in more than a few curses and more than a little spite.
Echidna's merciless attitude makes Emilia think about those days. She can try not to recollect on
them, but the wounds and their unhealed scars continue to assert their pain.
Emilia: “But I'm going to act as if you are.”
Echidna: “—”
Still focused on that pain, Emilia firmly rebuts Echidna.
She watches Echidna narrow her eyes, and bites her lip, strength entering her eyes.
Emilia: “Being unlike others does, sometimes, make painful disagreements happen. Whether there's
lots or not many of you might be a big factor for what determines the victims and assailants,
sometimes, too.”
Echidna: “And it's been repeats of that, throughout history. People cannot accept those unlike them.
The disparity in numbers represents exactly the disparity in strength. The many oppress the few.
Now that you understand this truth, and have gotten a little bit wiser, what are you going to do?
Gather up the few, and create a utopia for weaklings? Now wouldn't that be exactly the essence of
this place we call SANCTUARY?”
Emilia: “That's... one option you could choose, I think. But I want to choose a different path. Even
if I can't change that there were victims or assailants, the future's another story.”
The second that Emilia says the word 'future', Echidna's expression freezes numb.
To Emilia, it feels like Echidna is angry, as if this is something she absolutely doesn't want to be
hearing from Emilia of all people. But Emilia continues.
Emilia: “I'm sure I'm going to do lots of things throughout the Royal Selection. I might face even
more insults and spite than I did before. But I want to always say that I will never stop. To ask
what's so wrong about being unlike someone else. To ask what's so scary about being unlike our
neighbours.”
Echidna: “I'd rather you stop making be say this, but this is fundamental truth. People cannot accept
the discrepancies between themselves and others. By essence, all creatures desire for others to be
the same as themselves. To like the same things, love the same things, hate the same things, abhor
the same things—they feel secure when matters are so, and love their capacity to sympathise. Your
platform will be denied. As the ramblings of the weak.”
Emilia: “But that's just a neglect to think! It's lame!”
Echidna: “L-lame...?”
Yells Emilia. Echidna's eyes shoot open, looking not to have expected that word in the least.
Emilia puffs out her chest.
Emilia: “It is!”
247
Emilia: “It's so lame. You're not like your neighbour, so you hate them... are you a child? It's
ridiculous that someone would block their ears for a reason like that. I'll say it countless times to
any of those nitwits. Rather than mindlessly yell that you don't like it, if you're looking to quiet my
endless tirades, it's easier to change your thinking a little.”
Echidna: “Absolutely self-centred. Incredible self-deception. You'll eliminate the opinions of others
that you wish not to hear, so that you may enforce your own?”
Emilia: “I'm not eliminating anything. It's up to them whether they unblock their ears. —I'm just
confident that I'm the more stubborn.”
Her hand to her hip, Emilia demonstrates to Echidna that her will will not bend.
Echidna's expression turns sour and she averts her gaze from Emilia.
Echidna: “Whatever you may assert, the world has not changed yet. The forest-dwellers, frozen in
ice—supposing that they are alive, and you do bring them into a thawed world, society is not
prepared to accept them. All you are doing is tossing those who were kind to you into adversity. All
for your hypocritical beliefs.”
Emilia says nothing.
Echidna: “You wish to free your friends as soon as you can. But should you free them, your friends
will suffer as the world rejects them. Living is suffering, and death too is suffering. In a world like
this, what can your individual willingness do? What can it change. What does it change?”
Echidna is sincerely inquiring this of Emilia.
She has verified Emilia's resolve through the two TRIALS of the past and impossible present. Now,
Echidna is asking Emilia about her resolve for the future.
About Emilia's prospects should she follow her intentions through.
About the route she will take to reach her imagined future.
About what Emilia will use as her cornerstone, and upon what concrete basis she will create this
path.
Emilia nods in reply, and:
Emilia: “I'll think about that after I finish the TRIAL!”
Echidna: “—Huh?”
Emilia: “It's putting the cart before the horse if I get so focused on the future that I forget where I
am. I know how this sounds when I'm the one saying it, but I'm a bumbler. When there's a wall I
have to scale, but I'm worrying about what's on the other side of it, I'll wind up falling into the hole
at the foot of the wall.”
Between the TRIALS and her argument with Subaru, Emilia feels that she has a rather correct,
objective view of herself.
She feels that her appraisal of herself is also unrestrained.
She is not someone so adroit that she can manage many things on her own.
248
It's a question of whether, after putting in her very best effort on the thing right in front of her, she'll
manage to procure results.
She has hope for the future. Prospects for the future.
Resolved to aim for those hopes and prospects, she must take the very first step on the road to
achieve them.
What she should be establishing right now is that exact, first step.
Echidna: “...I finally remembered how pointless it is to debate with you. Honestly this was all rather
idiotic of me.”
Emilia: “I know that you're smart, but I kinda think it's sooo unfair for you to shut down other
people's opinions like that.”
Echidna: “Do you believe that we exchanged any opinions? I presented questions, and you replied
with empty platitudes. I'd forgotten. That you're a hopeless child, unable to stand on your own,
constantly relying on others, a weak woman.”
Emilia: “You're right... I am a weak child.”
Emilia lowers her eyes and gives a small shake of her head.
But she immediately looks back up, and matches her gaze to Echidna's.
Emilia: “But,”
Emilia: “Is being weak really so wrong?”
Echidna: “...What?”
Emilia: “I know that the person who taught me something very important would say this. It isn't
wrong to be weak. It's wrong to want to stay weak.”
She thinks of the black-haired, nasty-eyed boy.
Lamenting his powerlessness, but kind and thus suffering more wounds than anyone else in his
efforts, a precious boy.
If it were him, who borrowed everyone's aid but nevertheless took a place for the most painful parts,
he would absolutely say that.
Echidna: “Reorientation.”
Emilia: “Mm. I was slow to reorient.”
Seeing how a smile arises on Emilia's face, Echidna perceives that there is truly no room for debate.
Echidna has no methods to stop the persistently optimistic, overly-enthusiastic Emilia.
Meddling in the issue any further would even begin to impact her dignity as a WITCH.
Echidna: “...Well, enjoy the remaining TRIAL. Once you've completed it, a reality far harsher than
these TRIALS awaits you. I'm sure you'll come to understand just how difficult it will be to uphold
your shiny platitudes.”
249
Emilia: “Thank you for going out of the way to talk to me. I'll make sure to remember what you've
told me. And...”
She must be moments away from dissappearing from the mirror.
Seeing how Echidna's reflection begins to fade in the mirror, Emilia continues her speech. Echidna
furrows her brows, looking sour. And Emilia,
Emilia: “Thank you for showing me this world.”
Echidna: “—”
Emilia: “It might be an impossible world, but it's still one I wanted to see. I never thought a day
would come where I'd see them, Mother and... Father Juice laughing together like this. Thank you.”
It did hurt when Echidna told her that this world was not real.
But even if it is an impossible world, these scenes are what would have occurred.
These scenes full of happiness and love, enough to make Emilia tremble in joy and sorrow.
I'm so glad I got to see this, thinks Emilia from the bottom of her heart.
Echidna: “...You.”
And so Emilia expresses her thanks—and Echidna's expression shifts.
Her expression has been one of witnessing something disgusting, her attitude has been one of
withstanding displeasure, her stance has been one of scorn toward all of Emilia's action, and she has
shown many such faces until now—but this expression is different from all of them.
—Echidna, looking close to tears, simply gazes at Emilia.
Emilia: “Echidna?”
Echidna: “I hate you. —I just, hate you.”
Says Echidna, voice strangled and face cast down.
Her image in the mirror then warps, and the white-haired witch disappears from the glass in an
instant. Instead what appears is a girl with long, silver hair and—
Emilia: “—hk!”
A wave of rejection spears through Emilia's chest as she promptly averts her gaze from the mirror.
Her pulse has accelerated, and her breathing has grown slightly ragged.
She's supposed to have steeled herself for this, but it still terrifies her to be reflected in a mirror.
Emilia: “—”
A century passed in the frozen Elior Forest before Puck saved Emilia from the ice. —She has never
seen what she looks like grown up.
250
The reason's simple. She's just scared.
Her century of slumber in the ice means that Emilia's heart has remained immature, while her body
has matured to womanhood.
Once she regained consciousness, and first realised that she couldn't control her body very well,
Emilia was struck with the illusion that her body may not be hers, and spent many nights in tears.
The reactions from the neighbouring villagers helped spur on that trauma of hers.
Emilia shared the same distinctive physical traits as the WITCH OF ENVY, and the villagers feared
her like a demon. Even though they realised that Emilia was going to do them no harm, they
continued to alienate her.
Once people knew that Emilia was not going to do anything, what awaited her was a life of
discrimination, spite, and curses. During that time, Emilia came to at least unconsciously recognize
that people hated her because she looked like the WITCH OF ENVY.
That would be when she started rejecting mirrors and keeping her eyes from her own visage, which
others detested.
Puck noticed Emilia's mental wounds, and removed everything reflective from her vicinity. He
would even call out to her when she was out fetching water, distracting her so that she would not
face herself on the water's surface.
—One of the clauses in her contract with Puck, where he was the one in charge of Emilia's daily
grooming, was most likely something to protect Emilia.
To protect his daughter, who could not look in a mirror, Puck used the contract as pretext to mask
her trauma.
Emilia: “...I really have had so many people looking after me.”
And how long has she spent sulking alone without realising how others felt?
This is the end of the time she's spent in ignorance of what she's been given.
She takes a breath. Freezes.
And raises her head, undertaking the personally momentous deed of sighting herself in a mirror.
Reflected in the mirror is a girl with long silver hair and amethyst eyes.
Who is glaring so intently at her, looking as if it's the end of the world.
Emilia: “—The heck.”
She says, the whole thing anticlimactic.
Seeing her matured visage in the mirror, Emilia sighs.
Emilia: “I look less like Mother Fortuna than I thought, it's too bad...”
After her sulky mutter, the world shatters into pieces.
This happy, desired, but inevitably-to-part dream world, ends here—.
251
※ ※ ※ ※ ※ ※ ※ ※ ※ ※ ※
Emilia: “—ah, hauh.”
After regaining consciousness, Emilia realises that she had fallen asleep while leaned against the
wall.
She had slumped to sit on the floor with her legs splayed out aside her, relying on the wall engraved
with Subaru's messages. She combs her fingers through her dishevelled hair and imagines the sight
of her own self.
So that was her appearance, feared by many as a WITCH, and what Subaru constantly said was 'cute'
or that he 'loved'.
Emilia, with her impoverished understanding of personal aesthetics, cannot tell which party is
correct.
However, Mother Fortuna is Emilia's conception of the prettiest and coolest of people. And so she
does not think nasty eyes are a bad thing, and actually she doesn't dislike how nasty Subaru's eyes
are either.
Emilia: “I just got back, this isn't the time for me to be thinking about weird stuff.”
Putting her hands to her cheeks, Emilia pulls the breaks on her own thoughts.
It's all so ludicrously spineless of her. She safely ends the TRIAL and returns, and just looking at
Subaru's handwritten messages seriously gets her this elated?
Emilia: “But... this does mean that the second TRIAL is really over, right?”
Mutters Emilia to nobody as she gets to her feet and starts thinking about her results.
Going from how Echidna was acting at the end, the TRIAL is most likely over. Unlike with the first
TRIAL, Emilia feels no particular sense that she has overcome anything.
But she indeed did wrest her near-captivated heart away, and managed to return.
Emilia: “—”
Fortuna and Juice. As Emilia thinks back on how close they were, her heart aches.
But she suppresses her sorrow and turns her back to the TRIAL room.
Supposing that the third TRIAL is ready, it will require Emilia to exit and enter again as she did with
the second TRIAL.
She'll coast off her momentum to defeat the third TRIAL, and liberate SANCTUARY.
For Subaru's sake, and for Ram's request, and to actualize the big talk she spoke to Roswaal, people
need her to take action.
Emilia: “—It's just pitch black.”
Passing through the dark corridor of the tomb, her footsteps pealing off the stone floor, Emilia
narrows her eyes as she notices how dim the light spilling into the ruin's entrance is.
Perhaps clouds are blocking out the moon, or this hazy glow is from starlight.
252
In SANCTUARY, which loses essentially all sources of light come nightfall, only the natural lighting
pouring down from above serves to rip through the nocturnal dark.
Emilia: “—huh?”
Is what Emilia ponders as she walks.
So when she steps outside the tomb, the horde of gazes focusing on her lead her throat to
unwittingly jam.
???: “W-we are in her presence!”
Somebody speaks up, and a chatter instantly spreads through the crowd.
The stir only unfolds further before the flinching Emilia, the overwhelmingly large group of people
all focusing their attention on her.
—These are the residents of SANCTUARY.
The people who live in SANCTUARY other than Garfiel and Lewes.
Emilia has not interacted with them any more than necessary during her time here. Partly because
Emilia's mental state hadn't been calm enough for it, partly because they had not been actively
trying to interact with Emilia either.
Emilia has a kind of resignation when it comes to people staring at her like this.
The residents detest Emilia's lineage, but hold expectations for her to liberate SANCTUARY, and most
of all must ascertain whether she is someone worthy of standing at their head.
And so Emilia had thought it impossible that they would show themselves to her in such great
numbers before she had succeeded in liberating SANCTUARY.
Emilia had been convinced that interaction with them would only ever come about once she had
achieved in attaining results.
So then why were they all gathered here?
And why were their gazes towards Emilia—filled not with loathing, but strong expectation?
???: “Can't say it's the nicest erv things...”
Before the bewildered Emilia, a girl steps forward from the group of villagers.
With her long, pink hair, this person is Lewes.
She steps forward to represent the villagers as she gives Emilia a smile.
Lewes: “Everyone here ers stuck at a standstill. Wondering what answer yer gonner give ter the
TRIAL, and... worrying about what will happen ter us after SANCTUARY's been freed.”
Emilia: “...I think it's inevitable that you would. But how would this be 'not the nicest of things'?”
Lewes: “Now thert's easy. Everyone in SANCTUARY, about Gar-bo and Su-bo's fight, er about your
argument with Roz-bo, or... well, lots'er things. We've all been derscussing them in detail, and from
there...”
Emilia: “D-discussed it!?”
253
While she watches Lewes scratch her cheek, Emilia's cheeks flush red.
Nevermind Subaru and Garfiel's clash of wills, Emilia's argument with Roswaal was just her being
pushy with her unrefined opinions.
She had rationalized to herself that it wouldn't be embarrassing for anyone to hear it, but now that
she knows that someone actually did hear it, it is making her embarrassed.
Emilia: “But, even if you did hear about it... Lewes-san, where did you?”
Lewes: “Hrm, so abert that... fer however I might look, I gert incredibly sharp ears. With it, yer
pretty much can't keep anything a secret so long ers yer in SANCTUARY.”
Emilia: “You do. ...Wow.”
Lewes's confession of eavesdropping winds up impressing Emilia more than angering her.
Failing to notice how the young-looking old woman sticks out her tongue, Emilia nods in
recognition of why so many people have assembled here.
And,
Villager: “E-Emilia-sama.”
Emilia: “Y-yes?”
Lewes: “Yer sound like yer met through a dating service.”
He's one of the villagers—and being that he's in Sanctuary, most likely a demihuman half-blood.
His canines are slightly long, and his pupils are slit. He looks about as old as Roswaal or maybe a
little bit older, seeming somewhat tense as he steps out before Emilia.
Villager: “I'm... no, we are, um... in complete sincerity, we are still undecided.”
Emilia: “—”
Villager: “About whether we may trust in you, or what it will mean to learn of the world outside
SANCTUARY. Plainly said, the outside is awash with things we don't know, and scares us. We were
all born inside here and have lived inside here. We know nothing of the outside.”
This was what Garfiel had also propounded, the way of life in SANCTUARY.
The four-hundred year barrier has forced the people inside into life here for generations. They had
no way to escape, and perhaps no need to think about the outside, either.
But now means to escape exists plainly before them, and this utterly foreign and unknown person
named Emilia is attempting to liberate them.
Of course people would feel unease and rebellion. And doubtful that many could burst into the
outside world, utterly confident.
Emilia had feared that Garfiel's anxieties had been the consensus of opinion inside SANCTUARY.
And this man in front of her is saying things that are validating that fear.
254
Villager: “We could perhaps come into Roswaal-sama's care outside, but how would that differ from
our present circumstances? ...Plainly said, we are more anxious than hopeful. The change frightens
us.”
Emilia: “...Mm.”
Villager: “However.”
Emilia nods and edges on lowering her gaze, when the man's statement stops her.
The man straightens his posture before continuing, his expression tense.
Villager: “Everyone has heard Garfiel's... has heard the boy's voice.”
Emilia says nothing.
Villager: “We know what that trooper was thinking, and how he felt. And know the exchanges
between him and that black-haired young man, and between yourself and Roswaal-sama
afterwards.”
His back still straight, the man's expression twists.
Regretful, and near to tears. It sticks in Emilia's chest.
Villager: “I, sincerely speaking, thought it pathetic. That a fourteen-year-old boy was so worried for
us, and that a child under twenty years old was howling at us like that. ...And even though Roswaalsama
stated that you could not do it, we listened to your words as well. And so, Emilia-sama.”
Emilia: “—Yes.”
Villager: “No matter what the results may be, and no matter what may occur after this, I believe
your effort to challenge the TRIAL incredible. Venerable. Not all of us share that sentiment, and not
even I have entirely accepted you yet. But I request that we may witness it to completion.”
Witness what? No need to ask.
Bathed in his wilful gaze, Emilia looks at those behind him—the crowd of people who are
accepting him as their representative—and nods.
Emilia: “Understood. I'll be sure to end everything safely... and you'll listen to what I have to say.”
Villager: “Yes. That is a promise. And to think of judging someone off hearsay, without ever
interacting with them... we're the last people who should be doing that, huh. —Wahgh!”
The man slumps his shoulders. When Lewes pinches his hip from behind.
The man springs up and turns around in objections, but Lewes just snorts a laugh.
Lewes: “Yer sure went on a while, sure are serious, aren't yer. And yer fell back int'er talking casual
halfway through. 'Cause yer ain't used ter doing this.”
Villager: “...M-my apologies.”
Lewes: “Anyway, there's what we're thinking. Apologies fer the meddler.”
255
With that charming little exchange, Lewes gets the man to stand down.
Emilia takes a deep breath, something other than oxygen puffing up her chest.
Lewes is giving her graces, and the people of SANCTUARY have come to see her efforts through.
Who could estimate how greatly it reassured her?
Emilia: “Thank you, Lewes-san. Now, I know I can try sooo hard.”
Lewes: “I see, I see. Well, good. ...Next one should be the last TRIAL.”
Emilia: “Yes, it is. —I'm going to challenge it right away.”
With the strength they've given her, Emilia turns around to face the tomb.
But halfway through her turn she freezes, remembering something, and glances back to Lewes.
Emilia: “Ah, oh... actually, Lewes-san, have you seen Ram? I'd like to tell her that I finished the
second TRIAL, but...”
Lewes: “...Ram's left here ter attend ter some business. But she she's praying yer good luck. 'You
have your tasks, and I have mine. Let us see them both achieved.'”
It sounds like Ram, and even though she knows it's just a report, it makes her want to give a wry
smile.
Ram's task—where, and with whom, will she achieve it?
Emilia feels something astir in her chest, but she consciously suppresses it.
Ram is believing in her. And so, she will believe in Ram.
Just how Subaru and the others made a path for her, she wants to proceed from their efforts and
make a path as well.
Emilia: “I'm going.”
Lewes nods in reply, and the villagers's jabbering sees her off.
Filled with even stronger resolve than the first or second times, Emilia steps into the tomb.
Where—,
<Face the impending calamity.>
The final TRIAL, approaches—.
※ ※ ※ ※ ※ ※ ※ ※ ※ ※ ※
Ram feels how her heartbeat grows a touch distant in her chest.
She has never been bathed in such hostility from this person ever before.
256
Physical contact with him, exchanging words with him, being ordered by him.
Those things were the epitome in joy for Ram, and her meaning in life.
And so the fact that she feels girlish elation—even when when he regards her with hostility—
overjoys her.
???: “...Hoooooooow dare you show yooooooourself here.”
Mutters the tall man opposite Ram, glaring at her.
His tantalizing voice makes a sweet ache run through her brain.
Just by having his heterochromatic gaze on her, everything below her waist feels like it could
shatter.
Although, this is naturally not the time to display such weak and girly things.
A woman like that would merely be deemed useless and discarded.
???: “Nooooooooow then, what could you have coooooooooome here for?”
Ram: “—That is simple.”
She replies as usual, her face expressionless and manner tranquil.
With her pink hair swaying, Ram draws her wand from beneath her skirt, before pointing it at the
beauty before her—pointing it at her dearly respected master,
Ram:
“I have come to snatch you away from your witch delusions.”
And confesses that she is here to burn her loved one, consumed by an insane love, with her own.
257
CHAPTER 125B: STARTING AS REVENGE
The wind rages.
A single, strong gust whips violently at their hair and clothes as they face each other.
The setting is the outskirts of SANCTUARY, near the hidden house where young Garfiel and
Frederica lived, in an unpopulated and unremarkable meadow.
There are no residencies anywhere near here, and even if there were, nobody would possibly pass
by at this juncture. All of the people of SANCTUARY should be busy waiting for Emilia's TRIAL
results.
To cheer Emilia on, and for Ram to exploit to clear out the crowd.
Roswaal: “Delusion, yoooooooou say.”
Ram does feel somewhat guilty about using Emilia like this, but refocuses her attention as she sees
Roswaal's lips relax into a smile.
Roswaal sweeps his long, navy hair down his back, then closes one eye and glares at Ram with the
yellow.
Roswaal: “When you are the one saying it, aware of my feelings and my goals, it's quiiiiiiiiiiiiiiiite
the sad thing to hear.”
Ram: “I have have simply kept silent, but always thought so. As I naturally would.”
Roswaal: “Natural... weeeeeeeeell, I doooooooo suppose so. From your perspective, it was a life of
prolonged prostration and disgrace.”
Ram: “—”
Ram responds to Roswaal's shrug by lowering her gaze.
She more or less understands what he's trying to say. Of course she would. Ram has always been
paying attention to Roswaal. She understands to a painful extent how he, recipient of her love and
loyalty, would perceive her allegiance to him.
Roswaal: “So, the first thing you do once unfettered from the contract is stray frooooooom my
plans. That would be what you did in supporting Subaru-kun and aiding in subjugating Garfiel,
correct?”
Ram: “It had carried dual meanings, both for my objectives and to rectify Garf's idiocy. ...Were I not
there, I suspect that they wouldn't have managed anything.”
Roswaal: “It does feel that everything worked out 'in the end'. Subaru-kun makes some rather
thoughtless bets, when so many precious things are involved and at stake. ...I would never even
think to make such an idiotic gamble for my precious one.”
It's something of a sermon: cynical about Subaru's decision, and insistent that his own ideas are the
rational ones.
And honestly, there is nothing about Roswaal's statement that Ram can refute. Many of Subaru's
actions were utterly unplanned and haphazard. He had the luck of Heaven on his side for the whole
258
Garfiel affair, including how Ram participated in it.
Ram's opinion of Subaru being a man of only good timing hasn't changed at all.
Should you focus only on the question of achieving a goal, then Roswaal's ideas are far superior.
Provided that the gospel can be trusted.
Ram: “Won't make gambles... because what came of prioritising accuracy was the gospel.”
Roswaal: “Eeeeeeeeexactly. Although you seemed not to trust it, and have aaaaaaaaaaalways been
adverse to it. Again, inevitable. You've been praying for its writ to divert at any point that it possibly
could.”
Ram: “...I will not deny that.”
Cannot deny that.
Ram truly was adverse to the gospel. But there's a huge discrepancy between Roswaal's conception
and Ram's real motives as to why.
And it racked Ram with a sorrow that she never let show on her face.
Roswaal: “Do you remember? The contract that we formed, with the gospel as our intermediary?”
Ram: “—That, provided that history is moving as stated in your gospel, I wager my life to serve
you. In exchange,”
Roswaal: “Should time proceed down a path diverged from the gospel's writ, my goals face a
standstill. Should I lose sight of my goals, my life loses all meaning. You are permitted to do
whatever you wish with my husk.”
Ram: “Your life or death rests upon me.”
Roswaal: “That waaaaaaaaas the contract.”
With that, Roswaal draws a black book from his breast pocket.
He cradles the thick tomb close, stroking its cover as he gives a sigh.
Roswaal: “It must have been truly long and painful for you.”
Ram: “—”
Roswaal: “After all... you had to spend your life swearing reluctant loyalty to a man partly
responsible for the destruction of your birthplace. Contrary to your prayers, your heart delights
when with me... it must have been agony. My deepest apologies for being so aaaaaaaaapathetic.”
Roswaal spins spiteful words to wound Ram.
Partly responsible for the destruction of your birthplace. Hearing that sentence, pain and memories
of her hometown, and family, in flames pass through her chest.
The ONI have a low population even for demihumans, but in exchange, possesses incredible
strength.
Ram's race had gathered up their scant numbers and established a village deep in the mountains,
259
then were exterminated overnight between fire and knives, leaving Ram and ▒▒▒ as the only
survivors.
She had formed the contract with Roswaal the morning after the fire, as she gazed dazedly over the
scorched village.
Ram accepted the contract for the sake of survival.
Without ▒▒▒ ever knowing anything, and equally without Ram ever telling ▒▒▒ anything.
Ram: “—?”
Feeling an inexplicable sense of awriness and a faint aching in her head, Ram furrows her brows.
She feels that there is an unnatural vacuum somewhere in her memories. That there's something that
has to be there, but it's being obfuscated by a network of lies, telling her that no such thing existed.
Even though Ram's memories make no sense without it—.
Roswaal: “The despicable longing within you, and the lust for revenge that your true heart fostered.
Even with these contrary desires squabbling within you, you proved a truly eeeeeeeeexcellent pawn.
Just how extensively have I used you, with your obedient conformity to the gospel?”
While Ram searches her memories to try and find what is off, Roswaal continues his speech.
This isn't the time for this, she thinks as she aborts her search for the vacuum and faces Roswaal,
who speaks sweetly as he praises her loyalty.
But the glances he sends Ram begin to adopt another kind of sentiment.
Roswaal: “But who woooooooould have thought that you'd betray me and ally with Subaru-kun. Do
you comprehend how much grief I have suffered because of this?”
Ram: “...I have not defied the terms of our contract. Should the world proceed on a course differing
from the gospel, I will adhere not to your words, but to my own heart. The contract... should I have
disobeyed it, then I would not have escaped unharmed.”
Putting her hand to her chest, Ram asserts the legitimacy of her actions.
This contract between Ram and Roswaal was, naturally, not any simple spoken-word promise.
Spells are engraved on both of their souls, and they will suffer more than appropriate penalty should
they defy the terms. Since this has not happened, Ram's heart has not defied the contract.
But Roswaal gives a big shake of his head.
Roswaal: “Thaaaaaaaat is what I'm referring to. Considering that you have not been punished for
disobeying the contract in this situation... your soul believes without the slightest of doubt that you
are adhering to the contract. And I must find that a terribly unfortunate judgement.”
Ram: “What might you mean?”
Roswaal: “It's simple. —The gospel's writ has not diverged yet. The contract between you and I
truly reaches its terminus further from now, in the future.”
Asserts Roswaal, his voice low as he looks Ram in the eye.
The statement makes even expressionless Ram's cheeks tense. What she is hearing differs greatly
from what the contract's spell acknowledged.
260
Even with all these conditions in place, Roswaal's stubborn heart is not surrendering in the least.
Ram: “The writ has not diverged? Barusu will not challenge the tomb to liberate SANCTUARY, and
Emilia-sama is not doing anything to bring about snowfall. How could you state that the writ has
not diverged in this situation, Roswaal-sama... has something happened?”
Roswaal: “Nothing at all, it's theeeeeee same as ever. While, true, neither of the things I stated have
come into fruition... they still may yet.”
Ram: “That will not happen. Barusu has left SANCTUARY, and Emilia-sama is defeating the TRIALS.
To then state that matters will resolve to fit the writ... is this the floundering of an obstinate child?”
Roswaal: “I am quite a mature adult and so can deny being an obstinate child, but I can't deny that I
am floundering. Iiiiiiiiiiiinded, here is my useless floundering. —An endless, over four-century long,
peeeeeeeeeerpetual stretch of floundering.”
Changing his course, Roswaal asserts that his own actions are 'floundering'.
The clown laughs from the back of his throat, his expression twisted in insane elation as he slaps his
knees, praising the perfection of it all.
Roswaal: “Floundering, exactly, it's floundering! There is the punchline! Is there any word to more
accurately describe this obsession of mine? Nooooooooope, there isn't! Floundering... floundering...
ahhaaaaa, wonderful. It had never even occurred to me.”
Ram: “Roswaal-sama!”
Roswaal: “A man floundering in dependant obsession, and a servant whose lust for revenge against
a madman has morphed into loyalty to him. Our circumstances are truuuuuuuly crooked and
comedic. Hoooooooowever, calling my actions floundering will do nothing to change my
intentions. You have acted prematurely.”
Roswaal's insane smile disappears as he presents the gospel to Ram, so that she can see it.
Roswaal: “No matter what you may believe, the contract remains unchanged. Until she overcomes
the tomb's TRIALS, nothing has diverged from the writ that Natsuki Subaru will liberate
SANCTUARY. And even should she not bring snowfall, no deviation will come to the writ provided
that I bring snowfall.”
Ram: “—”
Roswaal: “You may appeal to the terms of the contract, but I also act in equal compliance. And so
we sit upon parallels. The time has not come yet for you to enact your revenge.”
Roswaal lightly tosses the book, catching it in his other hand before stashing it in his breast pocket.
Flickering flames arise atop his outstretched right arm.
Roswaal shows off how the flames change colour from red, to blue, to green, narrowing his eyes.
Roswaal: “You are still subject to the terms of your employment. You have acted impertinently as
my servant and so face punishment. If you had truly believed that the world diverged from the
gospel, then all you had to do was wait for two more days. I would have presented myself to you
261
without resistance. ...Hastiness serves well for nothing.”
Roswaal shakes his head in lamentation.
Roswaal: “Although,”
Roswaal: “I do understand your desire to destroy me as soon as conceivably possible.”
Ram: “...So you truly do understand nothing.”
Roswaal: “—?”
Ram closes her eyes, murmuring feebly in reply to Roswaal's cynical smile.
Beneath her eyelids there rests a wave of complex emotion, never to show on her face. By closing
her eyes, Ram can see her own way of life, which she pledged to never show to anybody.
She raises her head. Mana converges at the tip of her wand, poised this entire time.
Ram: “There is no meaning in having you should it be after the contract is fulfilled. After you've
been destroyed, there is no meaning at all.”
Roswaal: “—Come.”
Ram: “As you wish.”
—Flames of vibrant hue crash into invisible blades of wind.
With waves of heat surging through their SANCTUARY, the oni and the warlock begin their crooked
dance.
※ ※ ※ ※ ※ ※ ※ ※ ※ ※ ※
Emilia perceives the exact instant that the TRIAL starts.
Her five senses vanish, and she forfeits the general concept of 'having a body'.
Her sensory organs depart from her control, leaving her as only a mind floating helplessly in space
—which is what she is right now, only a soul.
This one obviously differs in nature from the previous TRIALS.
Emilia: <—>
She can't speak.
She has no mouth. No eyes either, but strangely enough, she can perceive the world.
Or no. You could say that she perceives the world, but it's not such a coherent thing yet that you
could confidently call it a 'world'.
Emilia's consciousness floats in a void of darkness.
She can regardless recognize her own self because of the many lights speckling this dark.
262
The dim lights come in many colours, splayed about in considerable number.
They resemble the glow of a minor spirit, but they give a decisively different vibe from the living
spirits.
They may resemble minor spirits, but their light more closely matches that from a spellstone.
Regardless, being that these surrounding lights have scattered around to circle Emilia, she feels that
she will not lose sight of the world.
Emilia: <—>
Surrounded by lights, and relieved that she has not been left alone, Emilia starts feeling
progressively confused about the utter lack of happenings here.
The dim lights simply float there in their positions, not doing anything at all. Echidna has been
showing up at the start of these TRIALS to explain what has been going on, but this time she isn't
there to act as a guide.
Time simply passes on by—though Emilia cannot tell what the time disparity is between the inside
and outside of the tomb, she knows that doing nothing will lead to nothing.
Emilia: <—?>
I have to do something, thinks Emilia, and a change occurs.
Emilia's consciousness, formerly fixed in place and immobile, transfers over to another spot—close
enough to the lights that she could probably touch them.
She has no body, but she can touch light. It's a weird sensation.
But she has no other way to express it. If she did, then she might simply be invisible to herself and
instead have a body constructed of primal magic—she may just be od.
If her od is what holds her consciousness and soul, then that does somewhat explain her current
condition.
Reaching some amount of agreement, Emilia thinks to validate her ideas by heading for one of the
lights.
There have to be more than twenty of these scattered lights. With no particular reason for it, Emilia
reaches out for the light that glows a dim silver.
And the instant her od touches the light—she sees it.
???: “Hate, hate, absolutely hate you. Me, I loathe you. I really do. All of it, entirely true. Ever since
we first met... I've downright hated you.”
Emilia: <—!?>
Immediately following the voice, a vivid scene slips into Emilia's perception.
Beneath an overwhelmingly giant sun, in a burnt field, standing beside a massive and dilapidated
building, bathed in crimson sunlight, is a girl with blood wetting her silver hair—Emilia.
It's her fully-grown self, who she has just witnessed in the second TRIAL.
And she looks woeful as she stands before the ruin, assaulting someone with her words.
263
Emilia: “I've had the thought countless times, and denied it countless times, but... yes, a nightmare
really did catch up to me. And so I'll say it.”
Emilia: <—>
Emilia: “Maybe we really shouldn't have met after all.”
A tear streams down from the corner of her amethyst eye.
It trails down to her cheek, falls from her chin, and the instant before it strikes the ground, the world
bursts into nothing.
Emilia: <—>
Swallow her breath. As just an od, she's incapable of something so dexterous.
All Emilia can do is accept the scene she just witnessed.
What was that light? What was this scene?
That had definitely been Emilia, but she doesn't remember this at all. Or perhaps that had been an
impossible scene, like the one in the second TRIAL.
Emilia: <—>
It's not, thinks Emilia.
She calms her chaotic mind, searches through her memory, and remembers.
The words she heard in the tomb when entering the third TRIAL.
<First face your past> <Witness the uncomeatable present>
And now the third one. Yes, it was:
<Face the impending calamity>.
Impending calamity. So, the future?
She had seen the past and a present, and for the finish, here's the future.
So this is the baptism that the TRIAL shows those challenging these alternate worlds?
Which means that Emilia will eventually meet this future?
Where she is in such a dismal place, crying as she conveys her regret for meeting somebody?
Emilia: <—>
Emilia uses her feelings of denial to dispel her unease, recovering a superficial level of calm.
But, once her mind registers the darkness again, another change occurs.
The silver light that Emilia's od had just touched disappears.
A vacuum fills the space that the light once occupied, the thing now missing. Emilia is puzzled by
this, but promptly realises what it means.
If each of these lights represents a future, then Emilia needs to touch every one of these futures
before she will be freed.
264
—If this is a TRIAL, then she will have to make some kind of choice after she's seen all the futures.
If Echidna is waiting anywhere, then she'll be waiting there.
Meaning: Emilia must witness over twenty futures.
Emilia: <—>
Will they be differing futures, or all fragments of the same future she just saw?
While feeling her non-existent heart wilting, Emilia reaches for the neighbouring light.
This one is blue, reminiscent of something vast and deep, like an ocean—.
???: “You're absolutely right. They were our enemy, and the wound was deep. If we withdrew here,
being that neither of us can heal, maybe we wouldn't have managed any rescue.”
???: “In that case...”
???: “But they were just a kid. —And isn't that enough?”
Again, the scene changes.
Now she witnesses a thick forest, with two people standing at the edge of a sheer cliff.
She can't see their faces. But she knows both of their voices.
One is very familiar, and thought the other one isn't, she does remember it.
The two are facing off before the cliff, one of them kneeling, the other looking down at the kneeling
party. Both of them look horribly morose, Emilia feels.
???: “You... you are a hero. A hero's... all, you can ever be!”
???: “I...”
???: “Why thank you so very much for your help!”
One silhouette reaches their hand out to the other, who turns their face away and imparts those
cavalier words of gratitude.
This feels like a definite farewell between these two people.
A goodbye laced with only irreparable woe and disappointment.
The world begins to fade again, and Emilia's consciousness returns to the dark space.
Emilia: <—>
Emilia had not been present in that scene at all.
She knew who the people in it were, but it feels awry that she herself was absent.
She's meant to be facing these lights while conceiving of them as futures.
So why on earth is it showing her futures where she is absent, or scenes that she will not be present
for?
265
—Is she being shown how her decisions may affect the futures of those around her?
If so, then these scenes only present one possibility out of many.
It's telling her to witness how her decisions will impact those other than herself.
Emilia: <—>
The blue light vanishes as the silver light did.
Twenty lights still remain.
—Each one of them carries the weight of a choice.
Steeling herself for this, Emilia reaches out to see the outcome of her decisions through.
In the next future, and the future after that, Emilia's decisions await.
※ ※ ※ ※ ※ ※ ※ ※ ※ ※ ※
With a swish of her wand, she creates and unleashes a blade of wind.
Invisible and inaudible, the whirling blade closes in on its target's throat as an assassin.
Roswaal: “Is that all?”
But Roswaal easily evades the imperceptible attack by nimbly jumping away.
Of course he would. He is the head of the renowned Mathers family of sorcerers, a rare breed of
magician proficient in all six classes of magic. For Roswaal L. Mathers, perceiving others'
manipulation of mana is child's play. Even wind magic with its invisible blades is as visible to
Roswaal as fire in the night.
Roswaal: “My turn.”
With a swing of Roswaal's arm, three fireballs of differing hue rain down upon Ram.
A red fire, a blue fire, and a green fire—all three of them pursue Ram when she leaps backward,
quite annoying in how they tail her. She runs backwards, her breath slightly ragged, as she
unleashes another spike of magic. The windblade strikes the three flames, which Ram thought
would snuff them out, but instead they each react in differing ways.
Ram: “—!?”
The instant the red flame takes the hit, like taking a bath of oil, it combusts into a pillar of fire.
The blue flame is easily sliced to pieces by wind, its embers shooting out in all directions.
The green flame looks to be engulfed in wind, when it then absorbs the wind mana and changes its
shape, morphing into a snake of green fire that slithers across the ground in pursuit of Ram.
The fire pillar blazes at Ram, who kicks off from a massive tree to avoid the blue flames, and then
tumbles across the ground to dodge the green flame's fangs before again striking the fire-snake with
her windblade.
The snake bursts into small flares, which scatter over the meadow to smoulder.
266
Roswaal: “Oh my... that was only one exchange of magic, and yet you seem quite wounded.”
Ram: “Hahh... hauhh...”
Roswaal: “If you acted with belief that you could win, then I must say that your estimations are
raaaaaaaaaather naive. Why yes, I am currently devoting a large allotment of magic to the algorithm
to manipulate the weather. Hoooooooowever, I am not so careless to accordingly neglect what is
aaaaaaaaaaat hand.”
Roswaal tilts his head as he watches Ram, her shoulders heaving with every breath, and spreads
flames to encircle them.
He creates the three hues of flame again, which take the form of giant fireballs in his hand before
moving to revolve around him. Their numbers compound with every revolution, gaining speed. It
only takes a few seconds before Roswaal is veiled in a vortex of chromatic fireballs.
Roswaal: “This is from one flame of each colour. Ten flames of each type, for a total of thirty
fireballs. You won't manage to dispose of them all with your current abilities.”
Ram: “—”
Roswaal: “Although, were you intending to confront me while my combat strength was minimized,
it was the epitome of foolishness to aid in the fight against Garfiel. My abilities may be diminished,
but that means nothing when your abilities are diminished as well. I can tell from the mana
overflowing from you. —You transformed, didn't you.”
Asks Roswaal, his voice low. Ram settles her breathing and answers only with a glance.
Perhaps having expected no reply, Roswaal shrugs.
Roswaal: “Of course you would turn out like this, should you transform without my aid. You may
challenge me with only the slightest of mana, but you'll approach your limit within a minute of
fighting. If we view this in terms of you expending your best efforts for the sake of your goal, it's an
affront to the eyes.”
Ram: “An affront... to the eyes, you say.”
Roswaal: “Iiiiiiiiiiiindeed, an affront to the eyes. You did state this before. When I said that you
needed only wait two days to see if the world had utterly diverged from the gospel, you stated that
would be pointless. I had been wondering what you meant at first... but I've contemplated it, and
come to a solution.”
Her breathing is calming down, but neither her stamina nor magic is replenishing. Roswaal knows
this, and so he is holding off on attacking Ram to have this conversation.
It's another story if she starts being an obstacle, but Roswaal doesn't intend to kill Ram.
And Ram has to feel that this complacency of his is an insult.
Roswaal: “If we take your goal to be revenge, then the answer is simple. You may brutalize me
when I am a cripple, but that will not appease you. That is the only reason I can conceive that you
would abandon your chance for definite revenge by challenging me now. It is only when you slay
me, partway through my own goals, that you will achieve revenge.”
267
Ram: “—”
Roswaal: “That was partly my mistake for pressuring you into a choice at a critical moment when
you were still young. It may have panicked you, after time passed and you realised thaaaaaaat fact.
And so you've run amok to ensure the opportunity does not escape you. ...Though, you can see how
that turned out.”
Ram: “—auh,”
A sound slips from Ram's throat.
A hoarse, breathy sigh.
Roswaal's odd-coloured eyes fixate on Ram, making sure not to miss a single one of her actions.
With that gaze upon her, Ram thinks back on everything she's done for the last half of her life.
Although she always knew it, recognizing it again, after all this time, does prick her.
Feeling the pain, Ram opens her mouth.
Wide, so wide, as she looks up at the sky—
Ram: “Ahahahahaahahahaha!”
Roswaal: “—Ram?”
They're mirroring each other.
As she thinks of how Roswaal chortled earlier, the thrill only escalates inside her.
Her reasoning is entirely different to Roswaal's, but yes indeed this is amusing. She has to laugh.
And of course she would. Because, in the end.
Ram: “After all the interactions, after all of that contact, you still haven't realised how the other
party feels.”
He's dim, he's insensitive, no, it's something on an entirely different level.
He's stubborn. He is fixated. He has determined that this would never happen, and so not moved an
inch.
To him, it's inconceivable that the passage of time would see feelings that started as revenge
transform into yearning.
Ram: “I have been by your side... because of the contract.”
Roswaal: “Yes, indeed you have. In that smouldering village, you and I formed a contract of
vassalage. I still remember how, even without your horn, your eyes blazed wet with fury. And so I
sealed that away through the contract, and redirected your vehemence into loyalty. Although, I did
believe that a day like this would someday come...”
Ram: “You're right. You were right. I wished to murder you. But you stole that opportunity from
me, and I proceeded to spend my days in the mansion with this inexplicable loyalty... and.”
Roswaal: “Unfettered from the contract, you have today determined to sate your desire for rev—”
268
Roswaal is lining up his theories. It's hilarious.
It's truly as if he pays no attention to anything except his own feelings, she thinks.
Ram: “Roswaal-sama, I am in love with you.”
Roswaal: “—”
Ram: “I wound up falling in love with you. That is why there is no purpose in attaining you once
you are broken. That is not the Roswaal-sama who I desire.”
Roswaal's eyes shoot open as his body freezes rigid.
He is stunned, as if he had truly, seriously not anticipated this in the slightest.
He promptly shakes his head, attempting to come up with words, but his lips merely quiver with
nothing meaningful coming out of them.
Ram: “Is something the matter?”
Roswaal: “Of, course there... are you, mocking me? After all of this, mocking me? You recognized
that your strength is too lacking, and so are attempting to shake me mentally, and...”
Ram: “How could I possibly believe that such wiles would work on you, Roswaal-sama? I am
simply stating what I truly feel.”
Roswaal: “That only makes it even less conceivable!”
Yells Roswaal, stomping at the ground.
Reflecting his agitated mental state, the shroud of fireballs flies into disarray. They soon come to a
halt, floating at various points around the surroundings as Roswaal glares at Ram.
Roswaal: “You love me? What on earth are you saying. You detest me. I'm a man you detest. I'm a
man partially responsible for the destruction of your birthplace. You're meant to hate me so much
you'd like to murder me!”
Ram: “I did at first. But not now. Now, I love you.”
Roswaal: “This idiotic...! Who would, think such a cheap...!”
Feelings that started as revenge must proceed to be revenge.
Feelings that become yearning must only ever start as yearning.
Roswaal stubbornly believes that people's desires and feelings cannot change.
And so he cannot believe that Ram has changed her mind so dramatically as to alter her way of life.
Roswaal: “What about your revenge! Did you not pledge for it! Did you not face your ashen village,
and swear upon the souls of your dead brethren that you would accomplish revenge!”
Ram: “I do think it wrong toward my brethren, and it does pain my heart to think of my birthplace.
However, I cannot change that I have fallen in love. I am prioritising my own feelings over those of
the dead.”
269
Roswaal: “—!”
Ram: “And you are not my direct foe, Roswaal-sama. Should my lust for revenge obscure my
vision, that would be the more shameful course. ...Would be my excuse.”
Roswaal is utterly lost for words.
Understand the situation right now!! would probably be an unreasonable demand. Roswaal is a man
who has gone for a very, very long time while sticking to his feelings.
Wholeheartedly, persistently devoting his love to one single person, doing everything he could to
make his wishes come true.
His emotions, his heart, and his belief that things ought to be this way are far too strong.
And so he cannot understand feelings that change over time, or understand that strength.
There's really nothing she can do about the fact that she finds even this aspect of him darling.
Ram: “I shall never allow you to become an invalid.”
Roswaal: “...You're contradicting yourself. No matter what your feelings are—no, doubly so
presuming that they're exactly what you stated—I don't understand why you are challenging me
now. If the gospel diverges, then I lose my purpose in life and mentally suffer. You are aware of
this, so why!”
Ram: “Because this is the moment. Barusu, Emilia-sama, Garf... now that all of them have brought
your heart close to wavering, I face my single and only moment of opportunity.”
So long as the contract persists between Roswaal and Ram, Ram cannot defy Roswaal. That Ram is
currently disobeying Roswaal is because her soul has judged that she is unfettered from the
contract, as Roswaal pointed out.
But is she truly? If one party believes that they fit the conditions, then they are exempted as a target
for the contract. Does the system of 'contracts' truly posses such a vague and loose set of judgement
criteria?
And so Ram pleads.
That she is not the only one who believes that the requirement to disregard the contract, the
divergence of the world and the gospel, has been met. That some corner of Roswaal's mind has
registered the same thing.
That this situation has arisen accordingly.
Roswaal looks utterly confused as Ram turns to face him, holds her breath, and dashes forth.
She draws her wand, wringing out the dregs of mana she has to cast a spell.
Roswaal: “—! It's useless!”
Ram's actions lead Roswaal to dispel his turmoil and order his floating fireballs to strike and stall
her. But not a single one of the fireballs hits her as she keeps low to the ground, their heat doing
nothing more than singeing her skin.
Ram has fulfilled the criteria needed to follow the gospel's future until now—and he cannot
determine whether to discard her. The fact that he cannot perceive Ram's designs also plays into it.
270
Perhaps he might even regret killing her.
If so, then that alone is enough to elate her so magnificently that she forgets her previous
melancholy.
Ram: “—El, Fula!!”
She concentrates the powers of wind, invisible destruction detonating before her.
Roswaal has prepared himself in fighting posture, but he is not her target. She aims for the ground
beneath it, rupturing it open and sending a great explosion of dirt to drown out his field of vision.
Roswaal: “Do you think this smokescreen will...!”
Ram: “—!”
One sweep of Roswaal's arm shatters the momentary veil of dirt into pieces.
The barrier fades to nothing, and as she watches it, Ram gives a sharp exhale and concentrates
power to her forehead.
Ram: “...auh, ghh,”
Agony. Her vision drowns in scarlet as bloody tears spill from her bloodshot eyes.
Her muscles, her bones, both of them creak as she hears the noise of her tendons ripping.
She ignores all of it, gritting her teeth so hard that she shatters them as she steps forth. The ground
beneath her shatters, and in that instant, Ram has transcended the limits of mortals.
Roswaal has batted the screen of dirt away—and Ram soars at him faster than a nanosecond.
He notices Ram, but before his eyes can even shoot open, she moves. Her outstretched arm reaches
for Roswaal's torso, and he swallows his breath as he realises that her hand is contacting his chest.
Transformation. Nothing else could have fostered this advance in Ram's abilities.
Although it is only momentary, Ram's strength currently exceeds the limits of the human body.
Roswaal must realise that it was his blunder not to consider that she could shatter his ribcage and
pop his heart.
However,
Roswaal: “—Wh, at?”
When the shock and pain fails to come, Roswaal can only blubber in astonishment.
In the blink of an eye, Ram has skidded to a stop about ten meters away from Roswaal. She faces
down, and vomits blood as she falls to her knees.
Roswaal furrows his brows, unable to comprehend the purpose behind Ram's actions.
But once he sees what is in Ram's hands, his expression instantly shifts.
Roswaal: “That!”
Ram: “To, me... this is, the root of all evil.”
His face pale, Roswaal moves to start sprinting over. Ram responds merely by glancing up before,
271
without any hesitation of all, giving a swing of her arm.
—And the gospel in her hands goes flying into one of the smouldering green flames.
Roswaal: “—!”
Roswaal screeches mutely, but still the blaze consumes the gospel and bursts even hotter. Alongside
a satisfying boom, the ancient book transforms into a pile of green ash.
Ram watches on, as if she has been yearning to see this for a very long time,
Ram: “—Now, finally,”
Ram sighs in satisfaction, her cheeks growing flush.
—The fireball thrown out of rage pierces through her petite frame in the very next instant.
272
CHAPTER 126B: WE'LL NEXT MEET AT A TEA PARTY
—She views the future.
???: <—Gone without, you cannot even wield a sword. Thief!!>
???: <Witness. The victor remains I.>
???: <Subaru, Emilia-neesama, I know you must be so tired. I'm sorry. But I'm going to wind up
being a burden too. I'm sorry. All the thanks I'd wanted to say could never be enough...>
—With every coloured light she touches, Emilia sees a different future.
???: <To think that someone I wanted to kill so much was actually a kind person, what an incredible
nightmare.>
???: <There exist feelings which musn't be spoken. Does it satisfy you, now that they have come to
light?>
???: <Does this make you feel that you've seen your promise through? If it does... if it does, then I
was better off bound and dead in that cave! If I was going to see this dawn, then I should have just
offed myself sooner...! Shit, shit!>
???: <God I'm sorry. I'm weak and so this. God I'm sorry. I couldn't make the kill, god I'm sorry.
Now ▒▒▒ will always be alone forever. God I'm sorry for being so weak...>
—Woe, ire, death, rebirth, farewells, meetings, the future comes to her in many forms.
???: <Yes... my dear grandchild... must've grown up well...>
???: <I shall never perish to such nonsense as a curse!>
???: <It's simply that I realised something. ...That along the path up to today, I haaaaaaaaaadn't been
walking alone.>
???: <How come... there's no soul inside!?>
—Must the future be despair? Is there nothing but sorrow and suffering?
???: <Just 's promised, 'm fuckin' killin' yer! Yeh!? NATSUKI SUBARUUUUUUUU!!>
???: <Am I being so covetous? Am I saying anhything so indulgent? Don't anhybody die, don't
anhybody weep... what is so complikkated about it?>
273
???: <After all, we must bleed ourselves to our very last drop to atone, yes?>
???: <Right and wrong and good and evil's all a bunch've bullshit. You're stopping right there. Say
it's Dragon or say it's Witch, if you're blocking the way then I'm... then we're, gonna smash you.>
—Then, was it wrong of her to choose this path? Was she mistaken to wish for any favours?
???: <—I believe that to pray for favours is hubris. Prayers are for when you seek forgiveness.>
—In the final world of light, a girl that Emilia has never seen awake and speaking talks.
I'd like to have a proper conversation with her, she thinks.
The sentiment proves more than enough for her deny the rejection of everything.
※ ※ ※ ※ ※ ※ ※ ※ ※ ※ ※
Emilia's vision clears, and she realises that she is in a breezy meadow.
A hillock with a white table. Emilia herself sits upon a white chair, unable to remember what
happened only a few seconds ago. But she does know that she is in a dream world.
Emilia: “Echidna?”
If anyone is going to greet her at the end of the TRIAL, then it's going to be the thing's supervisor,
Echidna. Emilia casts her gaze around in search of her.
But even though she can see this field stretch on to the horizon, she sights no shelters or anything
indicating the presence of people. And should she leave the table to go walking around, she might
lose the table and never find it again.
She's definitely right here in this spot, but it strangely feels like she might fall off the horizon.
Emilia takes deep breaths to calm herself down, and decides to start moving if nobody's around.
Perhaps there's an exit somewhere. She'll find that, and get out of here. She's got nothing to gain by
wasting time here.
???: “It's been like this forever—haa—but why is it that these situations—huu—always wind up
being my post—haa? I can't say I'm thrilled with it.”
Emilia: “...auh,”
Seeing the ball of hair that suddenly appears across the table from her, Emilia freezes.
She stares at this thing before her in shock, still halfway into standing up.
And gulps.
274
???: “Mm... an understandable reaction—haa—and the correct one—huu. The kid from before
must've been a tad obtuse—haa.”
Emilia: “—”
Every word out this person's mouth comes mixed with a gloomy sigh.
She is a rather listless woman with overwhelmingly long magenta hair, wearing a black robe. Her
comments are not thorny at all, and she looks relaxed as anything.
—But Emilia regardless feels a pressure so intense it's practically strangling her.
If this person felt like it, then Emilia's head would be vanished in an instant.
Emilia has regained her past, and can now manipulate such a vast quantity of mana that her body
cannot contain it all. Even though she has gained a massive boost in her capabilities as a solo
fighter, she feels that she has no chance against this woman.
She'd kill Emilia as easily as swatting a fly—and Emilia knows this.
Woman: “You don't need to be so wary—huu. I'm not looking to hurt you, or to get hurt—haa.
Since that'd be a drag—huu. But Echidna just doesn't want to see you so she—haa—forced me
here.”
Emilia: “I-I, see...”
Emilia gives a timid nod.
The pressure wreathed around this woman shows no signs of letting up. Nothing has changed about
her ability to easily decimate Emilia. But if nothing is going to change about the fact that the
woman can kill Emilia whenever she wants, then that'll stay the same regardless of whether she's
scared or not.
Emilia inhales, holds her breath, exhales. Doing this, she forces herself to calm down.
Emilia: “You're here in Echidna's place... so you're also a witch?”
Woman: “—. I see—haa—so you're braver than I thought—huu. That you're not timid during the
critical moments—haa—might be you taking after your mother—huu.”
Emilia: “You know about my Mother?”
Woman: “I can't tell you anything, but yes—haa.”
The unexpected relation makes Emilia gulp, but the woman looks utterly exhausted after making
that comment. Emilia could try to probe into it, but she probably wouldn't get anything.
Thinking to herself: Someday, Emilia decides to temporarily shelve the topic of her mother. She has
seen her past, seen an impossible future, and now Fortuna and Juice's light remains shining in her
heart.
For now, that's more than enough.
Emilia: “What would you like me to call you?”
Woman: “It's nice when children don't throw tantrums—huu—I'd like Typhon to get a lesson from
you—haa. My name's Sekhmet—huu. As you've guessed, I'm the Witch of Sloth—haa.”
275
Sekhmet leans her body onto the table, looking up as she gives a faint smile.
The bags under her eyes and the unhealthy-looking pallor to her skin are something of a concern,
but her features are attractive, and she is a beautiful woman. Still, the word 'witch' and the ghastly
aura she emanates do indicate that she is definitely not anyone ordinary.
Sekhmet: “I really couldn't—huu—care less about how our names as witches are treated in the
present—haa—so that doesn't matter—huu. I just want to get this request done with—haa—and
settle down into self-indulgent slumber—huu.”
Emilia: “Erm, if it's such a bother for you... could no one else have done it? Echidna doesn't have to
be the one if she doesn't want to... but aren't there any other witches?”
Sekhmet: “You're not going to—haa—get a conversation out of anyone else—huu. Minerva's the
only one who could manage an actual conversation here—haa—and she can't show her face to you
—huu.”
Emilia: “Minerva...”
Sekhmet speaks with awful rhythm thanks to her pauses to sigh. But hearing that she offers a better
conversation than the other witches makes Emilia terrified of imagining what the others are like.
But even that sentiment is overpowered by the strong feelings Emilia has for the word 'Minerva'.
Emilia: “Minerva...”
Mutters Emilia to herself as she tilts her head.
The word feels horribly nostalgic, something that would stimulate her memories. But that said,
Emilia cannot remember hearing it in any of her memories up until now, or in any of her recovered
memories either.
But it's a mysterious name, that could evoke thoughts of someone very close to her.
Sekhmet: “No sense talking about someone who isn't here—haa. Anyway, I'm just here to pass a
message along from Echidna—huu. Then I'm leaving it up to you what ideas you come up with to
end the TRIAL—haa. Pretty easy job for me—huu.”
Emilia: “Erm, thank you for your efforts...?”
Sekhmet: “I'll pretend that worked—haa. Now, listen closely—huu.”
Sekhmet calls out to the brooding Emilia, and lies her head sideways upon the table. She gazes up at
Emilia, and with a sigh, sets her right hand on the table too.
Sekhmet: “In the third TRIAL—haa—you would've seen the future—huu. Those futures are
possibilities of what will happen—haa—in this future where you decide to overcome this tomb—
huu.”
Emilia: “Possible, futures.”
Sekhmet: “There's a chance they'll all happen—haa—and a chance none'll happen—huu. Though,
considering Echidna's personality—haa—even I can tell that the futures you saw weren't the nicest
276
ones—huu.”
What do the other witches think of Echidna? At the very least, it seems like Sekhmet considers
Echidna as someone mean. Emilia can't exactly say much on that.
Sekhmet's opinion of Echidna is actually a little worse than what Emilia figures, but it's difficult to
demand a worse appraisal than 'mean witch' from Emilia.
Sekhmet: “The future splits into infinite pathways, and so derives possibilities—haa. But the
futures you saw were all seeds thick with tragedy—huu. After they sprout and bud, what blossoms
will come of them...? Haa. Are you prepared to wilfully walk a path of poison blooms that may
leave everyone unhappy...? Huu.”
Emilia: “—”
Keeping silent, Emilia gazes earnestly at Sekhmet.
Sekhmet looks fatigued after giving such a long speech. But she soon furrows her brows when she
notices Emilia's gaze.
Sekhmet: “...I'm pretty sure that I already gave you the question, haa.”
Emilia: “Huh, what? That was the question? I answer that, and the TRIAL ends?”
Sekhmet: “That's what it'd be—huu. ...Though, considering your goal, you could say that the Trial
was over the instant that you managed to get here—haa.”
Sekhmet makes it sound like a free round. Emilia gives a wry grin.
Emilia doesn't mean any ill. But the issue is just so banal it surprised her. After all, it's obvious how
Emilia would respond.
Emilia: “Worlds that end tragically for everybody. No, I'm not prepared to see those at all.”
She has to think of memories that rip at her chest, that claw at her heard.
In that world of darkness, amid those coloured lights, Emilia heard their wails times upon times.
Emilia: “These are futures where everyone might meet a sad end. In the dark world before this, I
saw a lot of them. Where everyone was crying, suffering, angry. I don't know the details of what
happened, but I don't want to see a future like that.”
Sekhmet: “...But, I can assure that if you continue on the path you're on—huu—it's highly likely for
such things to happen—haa. Is that going to make you flee? Huu.”
Emilia: “No. That's going to make me face it.”
Sekhmet narrows her eyes as Emilia shakes her head and puffs out her chest.
The overwhelming pressure threatens to consume her, but Emilia's spirit will not yeild.
If she comes close to losing heart, memories of her mother and father support her. If she comes
close to giving up, she has someone who will encourage her to keep going.
Emilia: “We'll sprint so fast we dodge the sad futures. But if that isn't going to work, we'll ride our
277
momentum to soar over them. If people fall in the jump, we'll put in our all and pull them back up.
And if we keep doing this, we'll wipe away every single tear.”
Sekhmet: “You sure sound confident for being so reckless—haa. When you merely talk about ideals
and what's convenient for you, you'll break the instant that you slip up—huu. You don't think that'll
happen? Haa.”
Emilia: “If I were alone, it might.”
Emilia responds fearlessly to Sekhmet's mocking words.
In a sense, Emilia's stance is one that means being dependant on others. But that is the option that
Emilia has left, after never being able to choose a single thing for herself.
Sekhmet: “—”
And Sekhmet looks utterly floored.
She immediately looks down, the table and her hair concealing her expression. When,
Sekhmet: “Pff, khaah... haah, hahahaha! Ahh, yes! So that's it! Yes, that's it, that's definitely it, of
course you'd give that answer now! Ahhh, hilarious!”
Emilia: “Is it really that funny?”
Sekhmet: “It's an absolute riot to me—haa. Okay? Huu. So, Echidna, right—haa. She's this terrible
wacko even after her death—huu—who enjoys watching the TRIAL's challengers agonize over their
pasts and presents and futures alone—haa. The idea that her plans would be destroyed, and like
this... ahh, it's hilarious—huu.”
Sekhmet laughs uproariously, taking pained breaths while speaking with cheer. She lifts her head
and sits upright, leaning against the chair back to view Emilia from straight-on.
Sekhmet's eyes host a nostalgic gleam as she smiles,
Sekhmet: “The TRIAL presumes that you're taking it alone—haa—and you answer it by saying that
you won't face your challenges alone—huu. —If Echidna heard this, she'd moan sour grapes all day,
all while looking dead serious—haa.”
Emilia: “Oh. So that's the reply I could've got. ...Mhm, I sooo want to see that expression on her
too.”
Sekhmet: “She's a terrible loser, so I doubt she'd let you see her looking like that—huu. That's a
privilege reserved for us dream-dwellers—haa.”
Emilia: “So unfair.”
Emilia pouts, which just makes Sekhmet's expression more gleeful.
To an outside observer, the harmonious joy abounding from them might make them look like
friends who have known each other for decades.
Sekhmet: “Though, in exchange for that, I'll bestow you with your TRIAL results—haa. As you'd
expect, there's nothing to complain about—in fact, you pass with a gold star—huu.”
278
Emilia: “Should it really be that simple?”
Sekhmet: “Did you want a more oblique answer, or some dramatic spiel—haa? Apologies, but you'd
be wrong to expect something like that from me—huu. I'm the supervisor right now, and my word
goes—huu. ...The TRIAL's over without any issue—haa.”
With a deep breath, Sekhmet snaps her fingers. She fails to get a sound on the first attempt, or the
second, but on the third try finally manages a click—and a breeze gusts from behind Emilia.
Emilia glances behind her, her silver hair swaying, to find that a door has appeared at the bottom of
the hill. It doesn't look like it leads anywhere, but Emilia intuitively knows that this door is the
dream world's exit.
Emilia: “You mean... once I go through that door, the TRIAL's over?”
Sekhmet: “That's the one—haa. Congratulations—huu. In the four hundred years—haa—since this
tomb was made and Echidna's TRIALS came into operation, nobody had defeated these TRIALS—
huu. Well, not that there was an abundance of challengers in the first place—haa.”
Emilia: “...Yeah. Not many people have been to SANCTUARY, and meeting the requirement to get
trapped in SANCTUARY is actually surprisingly tough.”
Sekhmet: “There's that too, but... well, it doesn't really matter—huu. It's all over anyway—haa.”
It does bother Emilia how Sekhmet starts getting vague, but she doesn't pry into it. More
importantly, she's elated to hear that the TRIAL is over.
Honestly, she doesn't feel any sense of achievement yet. It hasn't hit her yet. She had struggled so
much with the first TRIAL that she'd almost broken down, thinking this whole thing impossible.
She did feel that she came here resolved not to lose, but even so.
Sekhmet: “You don't look like you agree with it—huu.”
Emilia: “Erm, well I am kinda bothered. Sooo just kinda bothered.”
Sekhmet: “Echidna doesn't present problems that can't be solved—haa. It's incorrect to say that's the
whole of it, but that's basically the whole of it—huu.”
When it's one witch saying it about another, it's probably right.
Emilia nods reluctantly in a show of agreement. Sekhmet glances at her, examining her, before
giving a small wave of her hand on the table.
Sekhmet: “Once you exit—haa—that door behind you, it's goodbye to this dream castle—huu.
Which also means that's the end of the TRIAL—haa. And that you're qualified to enter the room—
huu—in the back of the TRIAL chamber—haa.”
Emilia: “Open, the door. Mm, right. And go in there... what's in there?”
Sekhmet: “The mechanism that keeps the tomb functioning is—huu. Once it's stopped—haa—
SANCTUARY's duties will come to their end—huu. You'll how how to stop it once you go in—haa.”
279
Emilia: “I stop the tomb's functions, and SANCTUARY's duties end. So the barrier disappears.”
If the barrier is extinguished, then Emilia and the people of SANCTUARY will be able to exit the
forest.
She doesn't know how many people will leave for the outside world once the barrier is opened. Or
whether life on the outside will truly be to their benefit.
But they can't stay closed up in here any longer.
Just like how Subaru argued Garfiel down, Emilia has to convince them. This is the end of a period
spent in a place with stopped time.
Once time is moving again, how are they going to make a place for themselves to live?
If possible, then Emilia wants to search for the answer with them.
She can guide them by the hand, give a push to their backs, and no matter how hard it is, she can
walk at their side.
Though it's an unreliable, shaky, and fledgeling demonstration of leadership.
Sekhmet: “It's enough.”
Says Sekhmet, as if she's seen into Emilia's thoughts.
That comment alone doesn't come with any of her characteristic sighs. Sekhmet said it for her while
looking her straight-on, and it makes Emilia gulp.
And smile.
Emilia: “Mhm, thank you. That's how I want to go my way.”
With that, Emilia gets to her feet.
She brushes her hair into order, before bowing her head to Sekhmet.
She doesn't really know why she's doing it.
But it feels like simply saying a goodbye won't be enough. Why is it that she feels so grateful?
Sekhmet surely won't tell her.
She pushes her seat in, and descends the hill on her way to the door.
The door feels emepheral as it stands there in the middle of the meadow, and Emilia realises that
she feels somewhat sad to be leaving the castle in a dream.
White table, crisp breeze. Bright sunshine, perfect weather.
It would be so fun to hold a tea party around that table.
Emilia: “Sekhmet-san. Can you tell Echidna something for me?”
Sekhmet: “...Let's hear it—haa.”
Emilia: “If we ever get the chance to see each other again, let's have a tea party. Even if I'm doing it
in a dream, I'll definitely welcome it.”
Sekhmet: “—No problem at all. I'll tell her.”
280
Her hand on the doorknob, Emilia glances back to address Sekhmet, who smiles.
Emilia returns the smile, and opens the door.
Beyond the door is darkness.
But for some reason, she feels no hesitation about stepping into it. Emilia already know exactly
where it leads.
She has overcome her past, chosen her present, and now meets a door to the future.
※ ※ ※ ※ ※ ※ ※ ※ ※ ※ ※
—Feeling somewhat suffocated, Emilia sits up on the hard ground.
Coming back from the TRIAL isn't the same as waking up from sleep.
It's not that her body fell into slumber, but that her consciousness was taken from her body led
somewhere else. Her body and soul were in different places, and seeing that her soul wasn't
sleeping, of course it's different from sleep.
If this were the same kind of thing as normal sleep, then considering that Emilia is rather bad at
waking up, quite a lot of time would pass until she was really awake. Puck would be the one to
wake her up before, but he isn't here now, and so it would've eaten considerable time.
And now she will need to learn how to deal with this on her own, for the future.
Emilia: “—Ah, gotta stop.”
Emilia shakes her head to dispel her sleepy thoughts, and puts her hand to the wall as she gets to her
feet. She feels pretty much fine. It still doesn't feel like she's overcome the TRIALS.
But if what Sekhmet told her in the dream was true—
Emilia: “I should be able to open the door.”
She looks to the back of the chamber, sighting the stone door across the small room.
The door hadn't moved an inch when she pushed or pulled it before, and just like how the tomb's
walls glimmer slightly to Emilia's vision, this door also looks to be cloaked in light.
Unlocked. Might be what it means.
Emilia's footsteps peal as she approaches the door. As she stands before it, she holds her breath for a
moment.
On the other side of this door will be something that liberates SANCTUARY.
Sekhmet said she'd know what to do, but honestly Emilia's a little worried that she won't. Emilia
isn't exactly confident about her smarts.
Is she not allowed to bring anyone along with her? Though, alongside the fact that not many people
can get this far inside, she gets a feeling that the door won't open if anyone else is around.
Perhaps this is all happening because of how smoothly it all went: Emilia cannot erase her paranoia
about this door.
Perhaps it's all a deception, she wonders. You could that being warier than before, but it's a
281
wariness limited to things connected to Echidna. A sense of caution she gets because she knows the
personality of the person who set this up.
Emilia: “Anyway, have to go in. Okay, here I go.”
She balls her hands into fists to psych herself up, and moves to put her hand to the door. Should she
push or pull? While she considers the issue, and just as her fingertips graze the door—
—The stone door slides sideways to make a path for Emilia.
Emilia: “...I feel like Echidna's smiling so nastily right now.”
Mutters Emilia, pouting at her spoiled start.
Emilia gets the feeling that this door's gimmick is some very elaborate pestering from Echidna,
which slightly calms her tension.
She gives a sigh, gets herself back in the mood, and steps into the room.
The door opens into a room less than half the size of the TRIAL chamber.
It's smaller than a room that's already small. Just two beds from the Roswaal Mansion would be
enough to occupy all the space.
She hadn't expected the room to be this cramped. Her eyes widen at how constrained it is, before
she spots the thing in the back of the room and puts her hand to her mouth in shock.
—In the back of the room is something like a transparent coffin, with a woman lying inside.
Her time is frozen, keeping her so beautiful that you could wonder if she was only sleeping.
The coffin looks to be made out of spellstone, and when Emilia touches it to examine its purity, she
is shocked at how superior it is. Such high-grade crystal would excel even Puck's old anchor.
A woman is sealed in spellstone capable of sealing things superior to the Great Spirit Puck. —Of
course, she isn't breathing. Emilia feels no life from her, and what remains is a husk.
Her long, sleek hair is white as frost. Her cheeks and neck, what areas of skin are visible, possess
the beauty of virgin snow. Emilia's breathing near hitches before her stunning visage.
Her beautiful form is garbed in perfectly black raiment, with not a single superfluous colour
present, the dress-like vestment crafted to her in miraculous concord.
A beautiful woman who can be described with the two hues 'white' and 'black'.
True beauty—the utter lack of need for any superfluous accessories—would probably feel terror
when faced with this black and white countenance.
Emilia: “She's beautiful...”
Emilia's thoughts escape her lips.
Emilia would find another strikingly beautiful woman if she looked in the mirror, but her sentiments
have nothing to do with that.
She is simply so enraptured by the beauty of this thing before her that she is absolutely moved.
A beautiful woman of black and white.
That would be someone she met in the castle of dreams, the WITCH OF GREED.
282
In the depths of the tomb, waiting there beyond the defeat of the WITCH OF GREED's trials is,
Emilia: “She looks like Echidna... but who is she?”
A woman reminiscent of the Thirst for Knowledge Incarnate, but who Emilia has never seen before.
283
CHAPTER 127B: NEVER QUIT
The only observable thing in this room is the white woman in the coffin.
Emilia: “Then, this thing she's entombed in... is the mechanism to turn off the barrier?”
Says Emilia after looking over the room, looking perplexed with her head tilted.
There are no nice and obvious levers, or spellstones you just have to crush. A dim glow shrouds the
transparent spellstone encasing her, and Emilia can tell that it is siphoning mana.
The only functioning thing in this place is this coffin.
Emilia: “Seriously, who is she... maybe Echidna's mother?”
Emilia thinks back on the witch who always looked so disgusted around Emilia.
She also had white hair and wore black clothes, like the woman in the coffin, and Emilia remembers
vividly how attractive her features were as well.
The visage of the witch in her memories and of the woman in the coffin have many points in
common.
Like the positioning of her closed eyes, or the shape of the bridge from her lips to her nose.
Echidna had looked like a late teen, while the woman in the coffin is more in her early twenties.
Perhaps it's better to think her Echidna's older sister than her mother.
Emilia: “And... there's no name. But this is supposed to be Echidna's tomb.”
Except Emilia goes in, to find that the woman in the coffin is not Echidna.
Perhaps the tomb's name was a deception, or—
Emilia: “Maybe this is Echidna, and the girl I saw in the dream wasn't Echidna?”
It's a crazy theory, and even Emilia has to shake her head.
Leaving aside whatever Echinda would say, Sekhmet surely would have mentioned something. And
now it's too late for Emilia to simply regard anyone else as being 'Echidna'.
Emilia: “It's Echidna's tomb, but someone else is sleeping here... might be what's happening.”
If so, then they better change the name of the tomb.
It says that ECHIDNA RESTS HERE. But it's someone else's place of slumber, which causes lots of
problems. Offerings will be going to the wrong person, among other things.
It's not the most clear-cut of conclusions, but still Emilia reaches it as she inspects the coffin, taking
care not to touch the thing.
She glances over the flow of mana. It appears that the coffin and the tomb are absorbing minuscule
amounts of mana from the earth linked to the tomb, and are using that mana to power some kind of
algorithm.
It's an infinitesimal load of mana it's absorbing, but it's still powering as something as huge as the
barrier, indicating that it's gathering the mana from quite a large area.
'Earth linked to the tomb' had been a literal statement.
The entire breadth of the forest inside the barrier is probably the tomb's power source. And the tomb
284
takes tiny loads of mana at a time so that it won't affect that power source.
Emilia: “It's amazing... so amazing, that I have no idea what it's doing...”
The algorithm is siphoning a flow of mana, powering the magical faculties.
Emilia can write simpler algorithms, but the complexity of the algorithm for the barrier around
SANCTUARY far exceeds her comprehension.
If she stops these processes, she doubts that they will ever restart.
Not that there's any need to restart them.
Emilia: “There. If I cut off this flow, that will probably sever the supply.”
Emilia follows the flow of mana and locates the origin point for the barrier, which uses the coffin as
its nucleus.
Inside the tomb, where the woman's hands are folded atop her stomach—is the exact point into
which the mana flows. If Emilia meddles with the mana there to disrupt the algorithm, then that will
terminate all of this tomb's faculties.
Emilia: “—”
For a moment, she hesitates.
Terminating the tomb's faculties will probably damage the mechanism that starts the TRIAL. Which
means that she'll no longer be able to enter the castle of dreams.
—She will probably never get to have that tea party with Echidna.
The witches, or at least Sekhmet, know about Emilia's mother.
She had felt both awe and nostalgia for Sekhmet's overwhelming power. She wants to know what
exactly that sense of familiarity signifies.
If she cannot enter the castle of dreams, she is furthering herself from that goal. And that—
Emilia: “—I just can't let go, can I?”
With that mutter, Emilia disrupts the weak flow of mana transmitting from the coffin to her
fingertips.
A shift occurs in the power that supports SANCTUARY's faculties and comprises its barrier. It
meddles with the critical parts of the algorithm, compounding from a small into a massive
alteration.
The glow eventually melts away, all signs of the algorithm vanishing from the spellstone coffin. All
that remains after one last flash of light is the pure spellstone, with the woman still sealed inside.
Emilia: “...I guess that's the end.”
Having observed no visible changes, Emilia timidly looks around the area. The flow of mana
previously circling through the tomb is gone, leaving the tomb as nothing more than massive stone
building.
With a quiet sigh, Emilia leans against the coffin.
The tomb has probably stopped rejecting the unqualified now. Emilia ought to bring Roswaal or
Lewes inside, being that they probably know what's going on, and ask them who the person
285
slumbering here is.
Emilia: “It's over... yes, it's over...”
By repeating the statement over and over, Emilia attempts to catch the truth that she is not feeling.
She thinks back on the lofty talk she gave to Roswaal before challenging the tomb.
Roswaal had told her: All you have to do is procure the results you desire.
Emilia couldn't suppose what his sentiment had been, but she doubted that he wanted her to beat the
TRIAL. Though, he was also the one who beckoned her here and was endorsing her as a Selection
Candidate, leaving her befuddled as to his reasoning.
Emilia: “Teacher... is what he said, right?”
What she also recalls is this person who Roswaal called TEACHER.
Even someone at the pinnacle of magicianhood like Roswaal would, naturally, have had a master.
Roswaal's master, that being this person called TEACHER, had started SANCTUARY with him.
Emilia: “And maybe... that was you.”
Thinks Emilia as she strokes the coffin.
If Roswaal had his Teacher, someone irreplaceable to him, then perhaps this white woman would
suitably be it.
Emilia: “—I need to talk to everyone.”
Emilia shakes her head and pulls her gaze away from the coffin.
Though, she will have to postpone the talk about the entombed woman. According to Subaru, if
they fail to exit SANCTUARY before tomorrow night—that is, dawn of the day after next—then
something terrible is going to happen.
If anything obviously out of the ordinary happens in SANCTUARY, run away as fast as you can, he
said.
Though she has a whole day of extra time, she doesn't know whether any unforeseen circumstances
are going to pop up.
She trots out of the room and into the hallway, making her way to the exit. If things are still the
same, then Lewes and the people of SANCTUARY should be waiting for her outside.
Emilia's footsteps peal over the stone as she runs down the corridor, before exiting the dark tomb
for open plaza.
Where,
Emilia: “—Huh?”
Met with a blizzard raging through SANCTUARY, Emilia breathes a hazy, white breath.
※ ※ ※ ※ ※ ※ ※ ※ ※ ※ ※
286
The snow encompasses everything in sight.
The gale roars close by, and the snow thieves her body of warmth. After a white puff of breath,
Emilia's amethyst eyes blink as her throat freezes in shock.
—What on earth happened!?
???: “—lia-Sama!”
The wind howls. Her chilled ears throb in pain.
Frigid gusts feel to slice at Emilia's skin, dressed lightly as she is, when she hears a voice calling
from beyond the blizzard and stops still.
Snow has already accumulated up to Emilia's knees and threatens to swamp her down. She takes
every step forcefully, trudging through the frost, to find silhouettes gathered beyond the veil of
white.
They must be the people of SANCTUARY. Meaning that they waited for Emilia in this blizzard,
without ever retreating indoors—
Emilia: “Everyone! Why are you all outside in this sn... huh?”
Emilia imagines everyone huddled together to stave off the cold, when she stops.
There are about forty SANCTUARY dwellers including Lewes. That's a huge number to start with, but
Emilia also spots someone who shouldn't be here.
???: “Emilia-sama! Is the TRIAL over!?”
The speaker is a young man with a crew cut.
Emilia knows him. Because she spoke with him before coming to SANCTUARY, and she would have
spoken to him even had he not acknowledged her.
It's a youth from Arlam Village's young men's brigade.
Seeing him, when he's supposed to have left SANCTUARY several hours ago on Otto's instructions,
makes Emilia's eyes shoot open. And what surprises her even more is that it's not just him.
With crewcut as their leader, Emilia spots several other people from Arlam. They have come in
carriages, huddling with the people of SANCTUARY inside the vehicles or in its shadow to endure the
blizzard.
Emilia: “Wh-why is everyone...? But, didn't you evacuate?”
Man: “Yes, we did. On Subaru-sama and Otto-san's instructions. They said that the dragons know
the way, so just run.”
Emilia: “Then why!? Didn't you hear that it's going to be dangerous here?”
Man: “We have heard. And we were told.”
The youth grits his teeth, before raising his head and pointing beyond the forest.
Man: “To wait outside the forest, return once the signal appears from SANCTUARY, and retrieve
287
those still here.”
Emilia: “Huh?”
Man: “Such as Ram-sama and the others. Anyway, they would fire magic into the sky. We were to
return to SANCTUARY once we saw it, load the residents into carriages, and leave.”
Emilia: “Who gave these instructions!?”
Man: “Otto-san did.”
Hearing Otto's name makes Emilia think of that flaky-looking merchant.
Though, no matter what impression he gives, he is Subaru's friend. Every time she sees the two
talking jovially, it reaffirms Emilia's assessment that he's someone capable of rivalling Subaru.
Otto had definitely planned a lot of the happenings in SANCTUARY, starting with the Garfiel affair,
while acting as Subaru's co-conspirator.
Meaning that these instructions are hugely significant.
Emilia: “B-but, this was still reckless. The blizzard is blowing so hard... you should've known that
doing this was crazy!”
The man says nothing.
Emilia: “What's wrong?”
The man makes an awkward-looking expression and averts his gaze. Emilia doesn't overlook his
reaction, instead pressing him further.
Emilia's amethyst gaze pierces him. He puts his hand to his brow, and sighs a frigid-white sigh.
Man: “Otto-san told us that the truly dangerous thing would be if it snows prior to the signal. Since
snowfall marks the time limit... he told us to immediately leave the forest then.”
Emilia: “They even knew about the snowfall... no, just, nevermind that. Why did you come, then!?”
Man: “—Because it snowed.”
The man straightens his back and gives his firm reply to Emilia's wails.
His gaze is so strong, Emilia falls speechless.
They knew that snowfall meant danger.
And they saw it snowing in SANCTUARY, and understood that they had reached the time limit for
that danger. With that knowledge, they chose to come here.
They sped here, to where the residents of SANCTUARY were in danger.
Man: “We suspected that Subaru-sama or yourself would have done exactly this.”
Emilia: “—”
With a wry smile, the man answers the question in Emilia's throat.
So the evacuees overlooking the carriages behind him were Arlam's young men brigade. Since their
288
goal is to evacuate the people of SANCTUARY. Everyone unneeded must have left them and
evacuated. That said, those who left would be forced into the tribulation of evacuating by foot.
And these men were here, because they judged that this was correct.
Man: “Emilia-sama, if the TRIAL is over... can they exit this place?”
Emilia: “Y-yes, they should. But, with this snow and wind...”
The man gazes at the ground, clicking his tongue in frustration.
Snow has piled so thick that walking even a short distance is a trial. Carriage wheels won't find any
purchase in this; they are stranded.
But if they could at least find somewhere warm, where many people could bide through the cold—
Emilia: “If we can't relocate as far as the cathedral... let's get everyone inside the tomb. The mana
there keeps the inside warm, and we don't have to worry about the building collapsing beneath the
snow.”
Man: “It's possible to go in?”
Emilia: “I turned off the tomb's dangerous mechanisms, everything's dandy now. Anyway, are you
able to transport everyone as far as the tomb? And the dragons should be loosed from the carriages
and let inside too.”
The six dragons had accommodated the brigade and brought them all the way back here. Even in
this instant, the dragons' carriages are protecting two digit columns' worth of people.
It's inconceivable that they could possibly abandon the dragons.
The man nods with a, “definitely.”
This should be good enough to deal with the snow for the moment. The issue now is that something
dangerous is going to happen alongside the snowfall.
Emilia: “I wish we'd actually talked about this beforehand!”
Emilia mourns the lack of time she had to speak with Subaru before challenging the TRIALS. This
probably happened because Subaru didn't want to leave Emilia with anything that would needlessly
worry her.
Though she's glad for his thoughtfulness, it's ridiculous that it's going to hamper her reaction to the
danger.
Emilia can think of three people who, like Subaru's group, probably know about the snow. That is
Roswaal, Ram, and—
???: “Yer've done well ter make it back ter us, Emilia-sama.”
Emilia: “Lewes-san!”
A pink-haired girl hops out of a carriage and onto the snow—Lewes. With now short she is, the
snow that reaches to Emilia's knees reaches to her thighs. She trudges laboriously through the snow
while Emilia hurriedly approaches her.
Emilia: “The TRIAL's all over now! Is everybody here!?”
289
Lewes: “All erv SANCTUARY's people, en all erv the humans who came back fer us err present, yes.
But...”
Emilia: “But?”
Lewes: “Miss Ram and Roz-bo ain't here. The two'erve them have been somewhere else since
before it started snowing.”
Emilia gazes over the people and the carriages.
She does not spot that familiarly bizarre outfit, nor that dependable pink-haired girl.
Emilia: “If I don't search for them... Lewes-san! Do you know? What's going to happen if we stay in
SANCTUARY with all this snow?”
Lewes: “—”
Lewes's cheeks stiffen and she lowers her gaze. Emilia recognizes what this means.
Lewes knows what is happening. She knows what the danger is.
Emilia: “Please tell me, Lewes-san. We have to prevent it.”
Lewes: “But yer see, the timing fer it's off. Su-bo said that Roz-bo's planning fer snow ter fall
tomorrow night, so there muster've been some mistake fer it to be snowing now...”
Emilia: “What mistake, it is snowing right now! So! We need to do whatever we need to do when
the snow comes! Lewes-san!”
Emilia puts her hands on Lewes's small shoulders as she attempts to persuade her.
Lewes's sour expression shifts, until she's left staring at Emilia in dumb shock.
Emilia: “Wh-what's wrong, Lewes-san?”
Lewes: “...Emilia-sama. Have yer gone into the building deep in SANCTUARY's forest?”
Emilia: “Deep in the forest? No, I haven't...”
Emilia tilts her head in confusion.
Lewes: “That isn't posser...”
Starts Lewes, before looking at the tomb behind Emilia.
Lewes: “Then maybe there wers sermthing in the tomb... that seemed special, perhaps? Like,
perhaps.... a giant spellstone, er something similerr.”
Emilia: “—There was. A sooo giant spellstone. I kinda wanted you and Roswaal to look at it later...”
Emilia glances around the area, then draws her lips near to Lewes's ear.
So that nobody else can hear her, as they begin preparations to move the dragons.
290
Emilia: “There was a woman inside the spellstone. I don't know who she was.”
Lewes: “—!”
This information rocks Lewes's expression.
Lewes's eyes shoot open as she stares at Emilia. After a long, long sigh,
Lewes: “Then...”
Lewes nods as if agreeing with something.
Lewes: “Understood. Emilia-sama, ask whatever yer wish. I'm obligated ter answer you. Obligated
ter follow yer orders.”
Emilia: “I'm not ordering anything!”
Lewes: “Listen. That thing yer touched in the tomb ers a spellstone that picks who's qualified ter
command LEWES. Yer now hold those qualifications instead erv Gar-bo. I... no, we, shall obey you.
Please order us however yer wish.”
With that solemn reply, Lewes attempts to lower herself while thigh-deep in snow. This will result
in her kneeling and burying herself head-deep in snow, and panics Emilia.
She promptly grabs Lewes by the shoulders to stop her.
Emilia: “Awuh! Right, okay! So I can ask things from you, Lewes-san. Then I'll ask this. Please tell
me what happens when there's snow in SANCTUARY.”
Lewes: “...Su-bo says that once it snows in SANCTUARY, the witchbeast SIZEABLE HARE will come.
It's drawn here by the mana in the algorithm ter do something as massive as change the weather ter
snowfall... ers the word.”
Emilia: “Algorithm to change the weather... then, somebody's behind this!?”
Lewes silently nods.
This is magic immense enough to manipulate the weather. Puck could easily do this, if he was being
serious. Which makes Puck the most suspicious candidate, but considering Lewes's attitude and the
context of the situation, Emilia immediately lands on the culprit.
Emilia: “...Is it Roswaal?”
Lewes: “Most likely. I think Miss Ram left ter try and stop him. But if the snow came anyway, then
it's possible that...”
Emilia: “Stop. I don't want to think about it. Anyway I need to find them. Lewes-san, I'm going to
start searching the village for them. If you have any ideas where they could—”
Lewes: “No need fer that, Emilia-sama.”
Lewes interrupts Emilia with incredible confidence.
291
It's like she knows exactly what Emilia's thinking, and it makes Emilia gulp.
And,
Lewes: “Us Leweses keep a close eye on everything in SANCTUARY. —We'll find and get yer ter
them in a jiffy.”
Lewes gives Emilia her stamp of approval.
※ ※ ※ ※ ※ ※ ※ ※ ※ ※ ※
Ram, as she lies unconscious, almost looks to be merely sleeping.
Roswaal: “...Ram?”
Roswaal draws the fallen, limp girl into his arms, jerking her . But Ram gives no reply.
This girl. Who would put aside anything to give Roswaal's words priority. Ram.
Of course she doesn't reply.
Ram is dying this very instant. And it's all because of Roswaal.
The burning of the gospel had sent him into a fury. His vision seethed with crimson, he had no idea
what was anything anymore, but he knew that he could not forgive Ram for doing this and—
Roswaal: “—”
—Struck her with a ball of fire while she was undefended, blasting her away.
She had overtaxed herself with imperfect oni strength, and burdened herself with the exact same
fatigue only hours earlier. Ram's body had reached its limit.
When a fireball blasted her.
Her life hangs in the balance.
Roswaal: “...Ram.”
Roswaal cannot remember what he thought as he drew near to her prone form and touched her.
Even now, as he holds her close and gazes at her sleeping, he does not think anything.
Roswaal regarded Ram as an incredibly convenient pawn.
She had gone through ordeals by his hand, and their contract preserved an extremely simple
relationship between them.
He exposed his true thoughts only to Ram, and spoke of his goals only to Ram. He believed that,
once that goal was achieved, he would hand himself over to her as his reward for his accomplice.
But Ram betrayed Roswaal partway through his course.
Ram's statements had been correct; going by her contract, the script for the situation had not
unfolded as Roswaal intended, and her rebellion was her pre-established revenge.
So he will not fault Ram. If forced to say anything, then he would've liked her to postpone her
revenge and administer it once the situation about the barrier had been definitely determined.
Then there was the topic of his bet with Subaru. Garfiel had been unexpectedly pliant, and some
292
sympathetic-sounding talk had seen Emilia reattempt the TRIAL, but ultimately Subaru's speeches
were the ramblings of a weakling.
It is impossible to defy a predetermined future. The path to reach that future may change, but events
will still lead to the destined end. Should someone stray from the path leading to the correct ending,
what awaits is doom.
But they're still resisting it, and it makes Roswaal laugh. And the fact that Roswaal knows this, and
knows how weak he is for fearing their actions, also brings laughter.
Why are they trying to change anything? He can't understand it.
Once any feeling reaches its peak, once it apexes, it will never fade in intensity. If you love
someone, if your heart ever blazes with love for someone, then that heat, that brilliance, ought to be
eternal.
And the same concept applies even if the emotion in question is hatred.
Feelings you have held for a long, long time ought to ascend to legitimacy. Feelings fostered over
time are ironclad, never to yield to anyone. They absolutely must be.
Garfiel's hatred for the outside has shattered.
Emilia has accepted her detested and sorrowful past.
And Ram's endless, vengeful hatred for Roswaal has,
Ram: <I am in love with you, Roswaal-sama.>
Roswaal: “—!!”
A love confession like a curse, burning deep in his ears.
Words that came from the mouth of the girl in his arms, which absolutely never should have.
Had the contract been binding her heart or soul, then he would have understood it. Her burning
desire for revenge had been converted into subordination to Roswaal, and her hatred into affection.
Which was why Roswaal had Ram assist him in his goals more than anyone else, and trusted her for
what would come after their realization more than anyone else.
Because Roswaal believed in her love-converted hatred, and her vengeful desire to kill him. Because
he believed in the hatred in the eyes of the girl he first met, and how she gazed at him with absolute
murder.
—And yet Ram betrayed her own vengeance, to extol love.
Roswaal: “Why did you, Ram? ...I don't understand it...”
Roswaal hears how her faint breathing grows distant, and senses that Ram's life is ending.
Her heartbeat fades. Something screams that this mustn't continue. His right eye aches. Aches, so
terribly. Stop! Stop asserting yourself. He's going to lose himself.
What should he do? What must he do? He cannot tell what it is he needs to do, and what it is he
mustn't do. He cannot remember it. He cannot conceive it.
He looks around the area. Nothing here is what he seeks. The gospel, which told Roswaal of the
correct path, has been lost in flames. Nobody will teach Roswaal. What is the choice he must make
293
here? Nobody will teach him.
There is nothing for it now.
Roswaal: “—Wailing wind beckons the snow, light upon the earth repatriates to sky. Each droplet is
silence given form, ivory untouched by past karma's favour laments unchanging eternity—”
A canto.
This hummed, lilting canto gives direction to the power wreathed around Roswaal L. Mathers. The
vast store of mana interacts with the refined algorithm, bringing dark clouds to the night forest.
Frozen wind whips past, and a chill cold enough to freeze to the core rages through SANCTUARY.
Clouds burdened with snow shroud all of the enclosed forest, and white frost dances to the earth.
—This is the power of the massive-scale magic algorithm ULTIMILLION.
Roswaal: “—ugh, khh,”
The canto ends, and the extensively-held magical power is released.
A massive load of mana is ripped out of Roswaal, and even he, who boasts a transcendental store of
mana, feels somewhat dizzy.
Mana for magic this extensive should truly be built up over several months, and its should be used
on a smaller area. Roswaal is irregular for procuring the mana over only two days, and for affecting
a range more than twice the size of the usual.
After the magician who achieved this feat gives a long sigh, he finds himself utterly lost on what to
do.
Roswaal: “I've made it snow, as the gospel tells... what do I do now?”
Roswaal has forgotten that he has made it snow one day earlier than what the gospel's writ stated.
Or actually, not even the bet occupies any corner of his mind any more.
Roswaal does not pay any heed to the process. His only concerns are for how the events around
SANCTUARY conclude. Snow falls, and the barrier is undone.
Should that happen, should that happen—then what happens?
Roswaal: “Ram... yes... Ram.”
He can no longer hear Ram's breathing.
Roswaal looks down at her face, and gently touches her forehead. Her transformation means that
her scar, where her horn used to be, is bleeding. Roswaal wipes away the blood, and as he always
does with Ram, injects colourless mana formed from a combination of all six mana types into her.
This was a ritual the two had always done, so that Ram's oni blood would not conquer her.
It's not that he's thinking anything.
Roswaal unconsciously understands that he is merely betting that her vitality as an oni will keep her
alive. He has no questions about saving her.
Ram needs to live. For the sake of Roswaal's goals, and for what comes after the realisation of those
goals.
Roswaal: “Teacher... Teacher, I... What! Am I supposed to do! Teacher... Teacher! Please tell me...
please... guide me, again...”
294
Roswaal's confusion reaches its pinnacle, and he cannot even comprehend his own heart as he
wails.
Though he is trying to ensure Ram's survival, his anger about her betrayal remains. He knows that
he has lost his beacon, but still searches for that old light.
The snow falls, encasing Roswaal and Ram in white flakes.
Everything drowns in the white, disappearing.
With the thought of, and perhaps that is fine, not present in him in the slightest.
※ ※ ※ ※ ※ ※ ※ ※ ※ ※ ※
Emilia cuts through the snow, breathing white puffs as she dashes onward.
Emilia: “Huma! Again, Huma!”
She shouts, casting ice magic upon ice magic.
She is doing it to avoid time loss from her feet getting bogged in the snow. She uses her magic to
purposefully harden the snow, giving her a path to sprint upon.
Some people might slip and find themselves in quite a bit of danger by using this method, but,
Emilia: “All! Right! Got it!”
Emilia is a practitioner of ice magic, and grew up in Elior forest. She is accustomed to frozen
ground. She dashes over the freezing snow of SANCTUARY as if she owns the place, with her small
escort running after her.
Emilia: “Is this honestly working for you?”
Asks Emilia, out of breath, to her guide. The girl looks up at Emilia, and replies with only a nod.
They can communicate, but she won't talk to Emilia. This is exactly what Lewes—what the
representative Lewes personality—had told her to expect.
Lewes had suddenly begun showing special respect to Emilia outside the tomb.
She informed Emilia that she was an entity born from the soul of a girl named Lewes Meyer, and that
there were several duplicates of her in the same circumstances. These Leweses functioned as EYES
spotted around SANCTUARY, went searching for Roswaal and Ram in the community, and were now
guiding her to them.
There exists in the world extraordinarily rare magic called 'duplication magic'.
Emilia had never heard about it being utilized on living creatures before, but perhaps it had been
done as a kind of forbidden magic. Emilia had kept herself from asking all the questions she wanted
to ask, ran through SANCTUARY while relying on the Lewes double, and dashed all about in search
of Roswaal and Ram.
Emilia: “If I don't hurry... the Sizeable Hare will show up!”
295
The witchbeast SIZEABLE HARE.
Even Emilia, ignorant of the world as she is, knows the name of this creature.
It is one of the three witchbeasts alongside the White Whale and Blacksnake, and like those other
two beasts, regarded as a calamity.
It is a witchbeast of weak, frail, tiny little hares. But the beast itself is a group of individuals, a
horde of creatures. It is not each individual hare, but the entire group of them that is the calamity
called the Sizeable Hare.
With its endless hunger and overwhelming numbers it would devour everything in its path. But still
that would not sate it, and it would proceed to wander the world while cannibalizing itself. Indeed a
calamity.
The terrifying thing is how it can multiply itself infinitely. The Sizeable Hare will usually be low in
number, cannibalizing itself to stave hunger when there is nothing to eat—but should it lay eyes on
prey that stokes its appetite, it cannot be stopped. It will compound endlessly in number, gnashing
away until the prey is destroyed, then cut its numbers back down as it moves on and leaves behind a
wasteland. That's what this thing is.
Emilia determines that she must face this incredible witchbeast.
They have already lost the time they need to flee the Hare's attack. The accumulated snow hinders
their escape, leaving Emilia and the others without options.
The non-combatants will hide in the tomb, while a frontline is formed at the entrance.
That is the only strategy they have for opposing the witchbeast. It'll be Emilia and Roswaal. If
possible they'll include Ram, needing to assemble all the combat power available in SANCTUARY.
And so—
Emilia: “—”
Snapped treetrunks and buildings battered from battle. Gashes in the earth, and unnatural pilings of
snow. —A man and a woman, close together in a tree's shade.
Having found Ram limp and sleeping, and the dazed Roswaal, Emilia shouts.
Emilia: “—Roswaal! Ram!!”
Emilia leaves the silent Lewes double behind as she slides over the frozen snow. She manipulates
the ground beneath her however she wants, scattering flakes of ice as she moves like a snow pixie,
before grabbing Roswaal's shoulders as he lies motionless and half-buried in the snow.
Emilia: “Are you listening!? Roswaal, come on, Roswaal! We're in trouble! We have to save
everyone! This isn't the time to be frozen!”
Roswaal: “—”
Rocking him makes the snow fall off Roswaal's head. It reveals his expression, and Emilia clicks
her throat.
Roswaal's face as he looks at Ram, his eyes dim, looks feeble.
Emilia: “Roswaal...?”
Roswaal says nothing. He hasn't even noticed Emilia.
His lack of reaction scares her, and she lowers her gaze to what is cradled in his arms. There sleeps
296
a pink-haired girl,
—With snow on her cheeks, showing no signs of melting.
Emilia: “—! Ram? Ram!”
Emilia calls to Ram in Roswaal's arms, and tries waking her up.
But Ram gives no particular reaction. Of course she doesn't reply, but she doesn't open her eyes
either—in fact, her eyelids don't even twitch. Emilia touches her cheek, and her lips, to find them
abnormally cold. As if she's—
Emilia: “That, isn't happening!”
Emilia rejects her ineffectual thinking as she grits her teeth and reaches into Ram's clothes. Her
hand strokes across Ram's chest, where she finds a faint heartbeat.
It could disappear at any moment, frail, and feeble.
Emilia: “—She's alive! We're okay! We still have time, Roswaal!”
Yells Emilia with hope as she glances back to Roswaal. But Roswaal remains with his hand on
Ram's brow, looking utterly dazed.
And Emilia notices it.
There is a massive amount of mana flowing from Roswaal's hand and into Ram. And this is acting
as Ram's lifeline.
Emilia: “Then, you're saving Ram's life...”
Roswaal: “—”
Emilia: “—!”
As she hits upon that truth, Emilia also hits upon the bitter truth.
Ram is unconscious, in dire condition, and Roswaal must administer the delicate treatment to heal
her. They cannot participate in the fight.
Meaning that Emilia must face the Sizeable Hare on her own.
—Can she do it?
This monster is one of the three that has survived for four hundred years, since the WITCH OF
ENVY's era.
Who could guess how many people had steeled themselves to face this thing, just as Emilia was
now? None of them had managed to destroy the beast. How does Emilia propose to fight it alone?
Without Puck. Only Emilia.
Emilia: “If we go now...”
Maybe they can still run? But what are they meant to do if it chases them?
If they encounter it without any refuges or hiding places, then Emilia cannot protect the civilians
from the beast. Guarding somewhere like the tomb presents the most potential.
It hurts that Roswaal and Ram can't help in combat, but Emilia musn't abandon the fight.
297
Emilia: “Roswaal. Bring Ram and come along with me. Everybody from SANCTUARY... mm,
everybody is taking shelter in the tomb. And I'm going to protect them. Don't give up on healing
Ram, and—”
Roswaal: “It's useless.”
Emilia meets Roswaal's eye level and begins to tell Roswaal of her resolve, when his whisper
interrupts her.
Roswaal stares at Ram's face, his eyes still hollow.
Roswaal: “Useless. Everything is... I don't know the future. I don't understand myself. ...This world
is done.”
Emilia: “So you're back to saying this! Who cares about the book! Maybe someone kind of
important wrote it, but how does that have any say in what we do!”
Unable to bear his resignation, Emilia raises her voice at Roswaal.
Why is this happening? This is not the Roswaal that Emilia knows.
Always composed, making bold decisions like nothing, acting like he knows absolutely everything
there is to know, all with a grin. Wasn't that Roswaal?
Who is weak man, who has given up on everything, looking like a cornered and lost child?
Emilia: “Roswaal. I can't understand what you're feeling or how you're hurt right now. I do want to
understand, but there's no time for me to learn. ...But I want to make that time. And so I need you to
work with me.”
Roswaal: “—”
Emilia doesn't understand Roswaal. He could continue being like this, and she still wouldn't
understand him.
But if they converse, and divulge their feelings, there are things she will understand. And things she
will never understand if she never does this. And things that will never be communicated, if the
time for them is never given.
Emilia needs to create the time they need to grow closer to one another.
Emilia: “Please, stand up, Roswaal. Neither of us are ending here. We won't let Ram end either.
We're all going back to everyone, together, and—”
Roswaal: “I...”
Emilia is insistent. But Roswaal does not meet her gaze.
He continues staring down at Ram, his scarlet lips moving to say:
Roswaal: “I, quit...”
Spoken so quietly, it could disappear.
The frigid, whistling winds do whip by, and the words are barely audible.
The whisper hardly left his lips. It's questionable whether Roswaal himself even heard it.
298
But she definitely does hear that quiet sound of surrender.
And so, Emilia—
Emilia: “—Don't you dare say that!!”
—Grabs Roswaal by the collar, and screams in anger.
The movement rocks Roswaal's head, and he whimpers in pain. Emilia assaults him, unrelenting,
with her words.
Emilia: “You quit!? What are you saying 'you quit'!? There is nothing out there to possibly quit!
There is nothing for you to quit! Don't you dare give up! Don't you dare surrender! Not me, or Ram,
or you, have any single thing we're possibly done with yet!”
Roswaal: “—”
Emilia: “I finished the TRIAL! The past I was so scared of! A happy present that could've happened!
Sad futures that might come! I saw them all! And I still decided to walk this path... and with that
resolve, I can finally walk it!”
She howls.
Wrath beyond what Emilia can ever remember surges up inside her.
Yes. There it is. Listen to that whiny voice, hear those pathetic opinions, see that gutless spirit. This
is what it looks like when you accept surrender as your end.
Emilia's roaring makes Roswaal's cheeks stiffen, and he averts his gaze. This is not him being
worried for Ram, this is him distracting himself and running from something he doesn't want to see.
Emilia grabs him by the jaw and forces him to face her.
Emilia: “Look at people's faces when they are talking to you!”
Roswaal: “—hk”
Emilia: “You won't understand what people are thinking if you don't look them in the eye. You
won't understand why people are doing what they're doing if you don't look them in the eye. Keep
your eyes on mine, hear my voice, stand up, and follow me.”
Roswaal's odd-coloured eyes blink as if realising something.
His lips twitch. But he manages no words.
Roswaal: “—auh,”
Emilia: “I'll never let anyone say that they quit. As long as you're alive, there's nothing out there for
you to quit. And—I am not letting anyone die here!”
Emilia gets to her feet. Turns around.
Over ten Lewes doubles have assembled here. All of them kneel reverently, awaiting orders.
Emilia takes a breath, and shouts her command.
299
Emilia: “Take Roswaal and Ram back to the tomb. I'm protecting everyone, no matter what.”
Speaking grandly, and aware that she only acquired this right by coincidence, Emilia leads the
obedient Leweses as she breaks into a sprint through Sanctuary's snow.
The Leweses group together to support Roswaal and Ram, taking turns to make the path while
following after Emilia.
—Emilia no longer hesitates in her course for an instant.
※ ※ ※ ※ ※ ※ ※ ※ ※ ※ ※
And the tales—
“No need to push yourself so hard, Emilia-tan.”
The boy who cherishes the girl who decided to protect everything returns to her side,
“You can hold off and fall back. —The inaugural battle of deliverance is here.”
“I'm sorry. That kind of went over my head.”
Their usual banter makes her smile as she supports her failing body, her eyes tracking the white
silhouettes as they press forward.
The two silhouettes, walking hand in hand.
She hears two voices as well.
They sound lively, and, feeling that she has been waiting to hear this, the girl's heartbeat pounds.
“What comes next is a complete unknown, in fact.”
“Yeah, we'll be doing something about this. —Together, me and you!!”
And the tales converge, their wishes perfect mirrors as they enter the finale.
Knight and Princess, facing beast in blizzard-swept SANCTUARY.
A Knight who cannot manage on his own brings a magician at his side, consecrating everything to
victory.
—The final battle of SANCTUARY commences.
300
CHAPTER 130: FACES IN THE SNOW
Icy winds whip past. Frigid temperatures slice at his skin.
A horde of white hunger swamps everything in sight. The hand he is holding is warm.
Natsuki Subaru feels not a speck of hesitation or doubt about standing here.
Subaru: “Great that we had that cool entrance and all, but isn't this a little weird!?”
Yells Subaru about the unanticipated scene as the snow batters his cheeks.
Roaring wind rages through SANCTUARY, which is currently embroiled in thick snow. Subaru was
ready for this to happen eventually, but the date is mismatched to what he remembers.
SANCTUARY would be buried in snow and lure the mob of white witchbeasts at morning—there was
supposed to be over half a day of surplus time left.
Behind Subaru there stands a silver-haired girl, breathing white with her shoulders heaving. Emilia
has been unable to fully restrain the mana overflowing from her body, and half-encased herself in
ice. Her left side is covered in white, and though it must be painful, not a speck of anguish shows on
her face.
Subaru mentally praises the bold Emilia, while simultaneously suspecting her as causing the snow.
Was she unable to control this frenzy of magic, bringing snow, and beckoning the Hare?
Subaru: “But then the order's off...”
The sequence between the uncontrolled magic and the Hare's arrival are backwards.
Emilia used her magic to oppose the Hare, which resulted in her suffering damage. If Subaru is
following the correct course of things, then the real cause is—
Subaru: “—”
Behind Emilia, Echidna's tomb looms.
Subaru acknowledges the gazes peering at him out from the entrance, and nods. If the people inside
are the residents of SANCTUARY, then they are not feeling the effects of the tomb's mechanisms.
That means that the tomb's operations have terminated, otherwise said that Emilia has defeated the
TRIAL.
Emilia has overcome the TRIAL. Snow is falling earlier than anticipated. There's the state of
SANCTUARY's citizens, and Emilia's resolute shouts and expression. And there's also,
Subaru: “Roswaal.”
Roswaal: “—”
Roswaal, dazedly staring at Subaru while sitting beside the tomb's entrance. Subaru doesn't have
time right now to check if Ram, sleeping in his arms, is okay.
All he can do is trust that she is.
Beatrice: “Subaru.”
301
When the small hand gripping Subaru's own gives him a tug.
Hit with an unfamiliar form of address from a familiar voice, Subaru chokes.
Subaru: “oughbbhnuh”
Beatrice: “...Explain that bizarre reply, I suppose.”
Subaru: “It just feels so novel when you say my name, so. Can you do it again but sounding
bashful?”
Beatrice: “What!? You are actually mad, in fact! This is no time for buffoonery, I suppose!”
Beatrice snaps at Subaru's silly request, her expression terrifying.
Subaru reluctantly drops the issue, expecting her to ignore it no matter how much he pesters her,
when,
Beatrice: “S-Subaru... there, I did it, in fact.”
Subaru: “Beako you are adorable.”
Beatrice: “—! I'm never saying it again, I suppose! I'll remember this for after we're done, in fact!”
Yells Beatrice, her face red as she swings her held hand in a huff.
Subaru looks at her, charmed, while also directing his attention to the horde of approaching hares.
He licks his dry lips.
Subaru: “So, Beatrice. We're fighting the Sizeable Hare, where's your mental prep sitting?”
Beatrice: “I am moments post-contract. The opponent is one of the great witchbeast triumvirate. We
are unprepared and conditions are poor. My contractor is a novice. I haven't participated in battle in
four hundred years.”
Subaru: “And?”
Beatrice: “I could ask for no handicap finer, I suppose.”
Beatrice smiles fearlessly as the beasts, their teeth chattering, swoop in to close the distance. Subaru
steps forward to face their attack and glances to Emilia behind him.
Subaru: “Me and Beatrice are about to crush the Sizeable Hare. Emilia-tan, I'm sorry for this, but
some're gonna slip past so I want you protecting everyone!”
Emilia: “I'm...”
Emilia cuts her sentence off there, hesitant for a moment.
But after closing her eyes and taking a quiet breath,
Emilia: “Right. Leave it to me. —And I'm leaving it to you.”
302
Subaru: “Yup, all mine.”
Put the right people in the right places, split the roles up between them, do what's best for you to do.
Emilia gives a deep breath as she concentrates on controlling her magic and erects a defensive line.
The snowfall continues to rage as Emilia forms a blockade of ice.
Subaru steps out from Emilia's line of defence as he gazes at the white typhoon.
Red eyes and sharp fangs stretch on as far as his eyes can see. Coated in pure white fur, this is the
witchbeast spurred by the most primitive and insatiable hunger in the world. The Sizeable Drove—
otherwise said, the Sizeable Hare.
The chittering of their fangs makes the ache in Subaru's soul spread to his whole body.
He has died gruesomely, flesh devoured and innards ravaged, to those fangs. He has felt the agony
of a hole gaping through his abdomen, spouting blood while teeth severed his windpipe. And he
knows the overwhelming feeling of loss from death, his body chewed up and missing limbs, in
Emilia's arms.
To complete this loop series, Natsuki Subaru must surmount this witchbeast.
Beatrice: “—Are you afraid, I suppose?”
Asks Beatrice to Subaru, holding his breath as he gazes at the beast.
Her face is impassive as she glances up at him. But her eyes, and her expression, inform Subaru far
more eloquently than her words.
—Inform him exactly who it is that stands beside him.
Subaru: “Nope. Not at all.”
Beatrice: “Oh?”
Subaru: “Emilia's at my back and you're at my side. It's like I'm strongest man in the world.”
Beatrice: “Doubtlessly, in fact.”
Beatrice's cheeks relax into a smile.
So you do get it, says her expression. Subaru joins her in her wicked smile.
The Sizeable Hare enters a frenzy, rushing for the brazen duo.
Beatrice points her free right hand, the one that is not holding Subaru's, at the Hare.
Beatrice: “We'll begin with a warm-up, I suppose. —El Meenya.”
Space spirals alongside the canto as purple crystals materialize around Subaru and Beatrice,
surrounding them.
These things, with the brilliance and bearing of icicles, are the magical stakes that Beatrice used in a
previous loop to skewer Elsa. In a single instant, forty of them have formed.
It takes less than a moment for one to aim and silently shoot off—without its aim deviating in the
least, to spear straight through the open mouth of a hare. The skewer proceeds to plummet through
303
the air and plunge into the rearward horde of hares, where it explodes. Fragments of crystal shred
through the hares around the site of impact, slivering them.
That is what one shot can do, and Beatrice fires forty at once.
The looming omnipresent destruction brings bloody flowers to blossom through the white world.
The ruthless opening attack annihilates hundreds of hares. Aftermath of the destruction litters the
clearing, where the surviving hares shriek in agony. The beast can multiply infinitely and there are
still units of it left, but even so, it works Subaru up.
That is, Beatrice's unimaginably devastating destructive capabilities do.
Subaru: “W-woaaaaaaaaaaaaaaah!!”
Beatrice: “I-is it that incredible, I suppose? It isn't anything so impressive, in fact. This is the lowest
of techniques from Betty, I suppose. A piece of cake, in fact.”
Subaru: “No, what, the... this, savage magic! What affinity!?”
Beatrice: “It's obviously going to be yin, I suppose. I'm not the best at other types of magic, in fact.”
Says Beatrice, not looking entirely satisfied about Subaru's praise.
The ravaged witchbeast immediately starts cannibalizing the gore from the corpses and multiplies
itself again, but Beatrice pays this not the slightest of mind.
Beatrice: “Pay attention in fact, Subaru. Here's a lecture from one yin user to another, I suppose.”
Subaru: “What, is that all?”
Beatrice: “Huh?”
Subaru: “Was our relationship just about both being yin...”
Beatrice: “Th-that wasn't what I meant, in fact. You're a fellow yin user, my contractor, and also
umm... Betty's Subaru, I suppose. Yes. And so here's my lesson to you, in fact.”
Beatrice, flustered, probably doesn't even know what she's saying. She coughs before raising her
finger and lowering her voice.
Beatrice: “About the apex of yin—the apogee of Yin Magic.”
Subaru: “What do I need to do?”
Beatrice: “Hold my hand, and keep me from being alone, I suppose.”
Subaru: “I mean I do think that's important, but...”
Beatrice: “...It seems you don't quite understand spiritualism, which gives me some concerns for the
future, in fact.”
She can be as exasperated as she wants, it won't change that he doesn't know what he doesn't know.
304
Beatrice shakes her head at Subaru as he frowns, and pulls him forward by the hand.
Beatrice: “Fundamentally, a spiritualist and a spirit fight on the battlefield as single entity with
separate minds, I suppose.”
Subaru: “A single entity with separate minds...”
Subaru thinks about Emilia's fighting style.
The most striking battle that involved both Emilia and Puck was the one with Elsa in the loot house.
Emilia had placed Puck on offence while she took charge of defence. She would also use simpler
techniques to buy time so that Puck could unleash massive attacks.
That bald old man mentioned that that was the basis of how spiritualists fight.
Subaru: “So I just have to do that. Okay, time for Shamac!”
Beatrice: “Being subject to your defective Shamac would probably damage us as well so I would
rather we not, in fact. And Subaru, your gate is...”
Beatrice trails off, looking reluctant to speak. Subaru feels apologetic that he forced her into giving
this consideration. His gate is probably junk.
He abused it. He can feel that it's broken. Again, he is speaking fantasies.
Beatrice: “—It's coming, I suppose.”
Mutters Beatrice halfway through her speech. The instant after Subaru grunts in confusion, he
realises that his feet are no longer touching the ground.
Beatrice kicks off the ground, and the jump carries the two of them straight into the air like a spring.
That exact nanosecond, a horde of witchbeast's fangs closes in on the spot the two had just been.
The Hare's fangs clatter against each other as the hares leap off the ground in pursuit of the two.
Subaru: “We're flying!?”
Beatrice: “We only jumped, in fact. I've diminished the effects of gravity with the yin spell MURAK,
I suppose. If we desired, we could fly by riding the wind, in fact.”
Subaru: “You see we're falling though!?”
Beatrice: “We could keep riding the wind if we were simply fleeing... but we are annihilating them,
I suppose.”
Like leaves tossing in the wind, Subaru and Beatrice are buffeted by blizzard. They regardless fail
to gracelessly flip upside-down midair, probably by Beatrice's doing.
The two are on slow descent from their ten-meter high peak. The hares wait below them with their
mouths gaping open, leaving Subaru to put his hopes in another rally of magical spears.
Beatrice: “Subaru, a continuation in fact. Spiritualists don't cast magic by using their internal mana,
but by directly manipulating the ambient mana, I suppose. A contract with minor spirits is essential
for this, so you are not currently meeting those requirements, in fact.”
Subaru: “Ah, uhrm, Beatrice-san? There's, there's kind of a whole bunch of them right under us!?”
305
Beatrice: “Just listen to me, I suppose. Your gate is trashed, and you cannot use minor spirits. So
poor useless hopeless Subaru's only role is to stay at Betty's side and praise Betty's magnificence, I
suppose. Why are you even here, in fact?”
Subaru: “That's what I wanna know!”
Beatrice: “Then I'll teach you, I suppose.”
The witchbeasts leaping up from below them will start reaching their feet in no time at all. If their
fangs bite on, the hares will never let go. Even he has to find it overwhelmingly lame to take huge
damage and start crying after how cool and composed he acted.
Subaru yells rather hysterically at Beatrice.
Subaru: “What do I do!?”
Beatrice: “Visualise, in fact. Imagine the same crystals that I made before, I suppose. They are
crystallized mana, spears weaved from corporeal magic. They taper to sharp points, with ruinous
shards packed inside them, piercing through defences and stabbing into flesh. —Visualise this
attack.”
Subaru: “Visualised!”
Beatrice: “Now all you must do is incant, I suppose!”
The horde of hares waits below them, mouths agape.
Red eyes, bloodstained maw, sharp fangs, instincts that view Subaru as merely a wad of meat.
Utterly repugnant, utterly loathsome, this is the greatest adversary in SANCTUARY.
Both: “—El Meenya!!”
Subaru and Beatrice's cantos mirror each other, and the conjured spears rain down at the ground
from on high.
Explosions and destruction rock the earth of SANCTUARY, eviscerating the ugly witchbeast.
※ ※ ※ ※ ※ ※ ※ ※ ※ ※ ※
Emilia: “Amazing...”
Sighs Emilia in admiration as she freezes a hare that slipped past solid.
Her amethyst eyes stay fixated on Subaru and Beatrice, fighting the beast beyond the shroud of
snow.
More specifically, Emilia's eyes stay fixated on Beatrice as she holds Subaru's hand.
Emilia herself is a spiritualist, who is using the minor spirits' magic this very instant. She
understands to a painful degree how incredible this magical confrontation is.
First, Beatrice is not receiving any magical reserves from Subaru.
306
They are definitely connected by the pass from their contract: it's simply that Beatrice is abstaining
from doing so. Subaru was thrown into combat immediately after forming this spirit contract. If
Beatrice siphons the mana she needs from him, he won't last.
Beatrice understands this, and is taking care not to burden Subaru.
Second, it's not that Beatrice is taking magic from Subaru—she's giving it to him.
It's not the most accurate phrasing, but it's the truth. Subaru, as he holds hands with Beatrice, is
receiving Beatrice's support, allowing him to use magic that should be inaccessible to him. He isn't
using his gate, and is instead using Beatrice's presence itself like a gate.
There is no way that Subaru can possibly understand how monumental this is.
Beatrice the spirit is supplying the magic for both herself and Subaru not from some outside source,
but her own magical stockpile.
And third, she is legitimately witnessing advanced yin magic.
The class of a magician's magical affinity greatly influences their future. Specialization in any of the
four main types of magic will demarcate them into distinct roles, and the same applies to the two
special types of yin and yang; meaning that their essence differs greatly from the other four, even
before reaching the advanced stages.
And then is the fact that they initially look to lack uses. They comes with lots of problems, like the
time needed to procure results or required quantity of magical power, that are also cons.
So the yin and yang affinities are both rare, and have few advanced practitioners.
Many spells have been lost over time, unlike with the main four, making it a difficult environment
to produce any new great magicians.
Yin has all of these glaring issues, and Beatrice has mastered it. And she is using ancient magic,
long lost to time and history, as if it's nothing.
Emilia: “Woah, they went really high that time. Huh? They're gone... oh, there they went.”
The way they fight is so dreamlike and phantasmal that it makes her lose her sense of reality.
Though part of it probably comes from the fact that Subaru and Beatrice are so amicably holding
hands.
Emilia can tell that Subaru is fighting desperately, but Beatrice is even smiling.
She must be having a lot of fun. It's not that she enjoys fighting, or flaunting her power. It's just that
doing this is fun for her.
Emilia: “—”
Emilia blinks, and Subaru and Beatrice have moved to a completely different spot. It's teleportation
magic akin to the more limited GATE CROSSING. Purple spears blast through a row of hares from
either end, the beasts shrieking furiously as they try to leap at the two, only for their bodies to catch
on something midair and shred apart.
Emilia strains her eyes. She spots it.
The fragments from the detonated spear have not vanished, and instead sit suspended in space, as if
frozen in time. The leaping hares shred themselves on those splinters, ripping themselves apart.
The crystalline trap is spread all across the area as the witchbeasts move, jumping, tumbling to
resolutely attack the two, all while triggering the trap quite comically.
307
The Sizeable Hare is a fearsome witchbeast, but the individual hares are not that threatening.
They lack any great power, and should an experienced fighter pay mind to the hare's ferocity while
combating it, they will definitely come out ahead.
A fighting style as reckless as 'follow your instinct to eat' will learn nothing. They want their fellow
hares to be caught and dismembered in the traps, because their hunger is everything. So they pay no
heed to the fact that they will die caught in the exact same trap, jump at them, and become a
cadaver.
Emilia: “Ah!”
Emilia strikes another hare that escaped the siege with her magic.
She dashes over to the frozen hare and kicks it to pieces without any hesitation. It shatters into
shards of ice, so utterly deceased that it cannot reform.
Subaru and Beatrice have been putting in such a good fight that only a surprisingly few hares have
slipped past to Emilia. Emilia can even concentrate on suppressing her own magical power.
But even as she watches Beatrice's display of overwhelming strength, Emilia cannot erase the
kernel of anxiety within her.
Beatrice's snare is powerful and cunning. The Sizeable Hare keeps catching itself in the trap,
building a mountain of corpses. But Emilia cannot see the end.
What Emilia witnesses is one of the hares trembling, when another hare appears as if sprouted out
of the first one's back. The hares repeat and repeat this, the beasts multiplying like mice.
100 hares compounds into 200 in an instant, and into 400 in the next.
It has numbers, and wretched instincts ignorant to the concept of 'stopping'.
Which is why this beast is counted as one of the great three, and has gone four hundred years doing
whatever it wishes as a CALAMITY—
Emilia: “Subaru, Beatrice.”
Emilia calls their names. Though they look to have an overwhelming advantage, they mustn't fall
negligent.
Emilia will never forget how she shivered after returning to the tomb with Roswaal and Ram, and
first confirmed the Sizeable Hare's presence.
Those eyes regarded every single thing alive as nothing more than its food.
An entity truly incapable of any co-existence will make those who oppose it feel that utter despair.
To oppose that overwhelming absurdity, Emilia needed to demonstrate comparable power.
And that was what she had intended to do.
A torrent of magic churns within her, not fully under her control. It surely cannot all belong to her
alone, and should she unleash it, it will annihilate the Sizeable Hare.
She would be offering her life in exchange. And she was prepared to do that, if it came to it.
Emilia: “Subaru...”
She murmurs his name as he fights on.
Her had known about the Hare's attack beforehand, and it doesn't seem that he's fighting it without a
plan. He's brought Beatrice out of the Forbidden Archive, and has her so full of life.
308
He would never do anything to bring gloom to that smile.
And so Emilia believes in Natsuki Subaru.
White magic, capable of ending everything, asserts its presence in her heart. She holds it down,
advising that its time has not come yet.
—She believes in his words.
※ ※ ※ ※ ※ ※ ※ ※ ※ ※ ※
For Subaru, using magic has always been tantamount to whittling away his soul.
At first it had been exactly like what Puck and Roswaal had said, that Subaru possessed not the
slightest of talent as a magician. It was so bad that, when he first used Shamac, he couldn't keep
himself from wringing out his mana and so fell immobile.
He next got by on hits of Bocco Fruit. He used magic during his duel even when he was prohibited
from doing so, and ultimately he abused his gate so terribly that it collapsed.
He has not any hope of being a magician.
Magic had saved Subaru many times, but he considered it something like whittling away at his
already delicate core, sharpening it down, something like that. He thought it inevitable that it broke.
And so he had only dreamed about doing what he's doing now, firing off consecutive blasts of
incredible magic, and could only think this reality impossible.
Subaru: “Hey, Beatrice! Should we really keep blasting them like this!?”
The Sizeable Hare generates more hares than what Subaru and Beatrice defeat. The hares eat their
dead brethren, steadily compounding in number. It seems like they're using their multiplication as
energy, for each hare grows more forceful the more that their number compounds.
This does encourage some dim hopes that, if they keep buying time, the hares will eventually run
out of energy to multiply themselves. But,
Beatrice: “There's no limit to their propagation, in fact. That's how they were crafted to be, I
suppose. Even when they verge on destruction they will not be destroyed. Unless you annihilate
them all at once.”
Subaru: “So what do we do? Do you have any ideas?”
Beatrice: “Subaru, are you trying to rely on adorable Betty for everything, I suppose?”
An explosion of crystal opens a hole in the mob, blasting the hares away, to be dismembered on the
suspended shards. Beatrice sees this through as she pulls Subaru's arm and hops into the air. Though
neither her tug nor her jump are that forceful, she easily succeeds in both.
Beatrice walks on air, dancing through space to avoid the hares' fangs as she weaves through gaps
in her crystalline snare. The lack of a single drop of blood sullying her extravagant dress proves
that, in this fight, she feels not the slightest agitation or unease.
309
Beatrice: “We're moving, in fact.”
Subaru: “Right.”
With that, space bends, and the two engage in a short-range teleport.
They cross through space in a manner unlike GATE CROSSING, reappearing behind the horde of
hares. The beasts sniff, but having lost Subaru and Beatrice, remain fraught with openings.
Beatrice: “You take the left, I suppose.”
Subaru: “Right's all yours.”
Visualize. Beatrice's magic reacts to Subaru's fantasy, manipulates the world, and brings about that
transformation.
He definitely feels that he is benefiting at her expense, but that's why he's not playing around in the
slightest.
The purple crystals of yin's Meenya spells form in accordance to Subaru's imagination.
Subaru generates winding grooves on the projectiles to magnify their piercing force before firing
them off all at once. His hands never touch them, but they do fire according to his will.
It's like he's drawing a mental bowstring, to shoot incorporeal arrows.
They spear through the air, landing a direct hit on the undefended hares, blasting the mob of them
screeching away.
Beatrice's destruction does the same thing to the right end of the mob, scattering them in all
directions.
Fissures in space swallow mobs of hares, sealing several hundreds inside a closed space as if in a
picture frame. The hares hop about beyond the looking-glass. Beatrice fires a crystalline spear at the
heedless mob of hares—shattering the planar world to pieces, sending the hares inside to their end.
Subaru swallows his breath, astonished at Beatrice's multifaceted sorcery.
While Subaru keeps repeating Meenya like an idiot, Beatrice keeps repeating entirely new
combinations of yin magic to annihilate the Sizeable Hare.
It's as if she's showing off every card she has in hand to Subaru. Or as if she's doing it to remind
herself of her skills.
Beatrice: “About now, in fact.”
Subaru: “Hm?”
The Sizeable Hare has been cut down in number, only for it to instantly regenerate the exact
quantity it lost.
Subaru witnesses this, and again feels the strangeness that he has been feeling for a while now.
Putting that together with Beatrice's muttering, Subaru feels the urge for a conversation.
Subaru: “Beatrice. They've been recovering the same number they lost... but doesn't it feel like
they've never gone over their original amount?”
Supposing there are one thousand hares, if Subaru defeats one hundred of them, it multiplies to
make one hundred more. If he defeats two hundred hares, he gets two hundred more hares. The
310
scales have not tipped once, no matter how many of them he kills.
But Subaru has never seen them multiply beyond that highest number.
Beatrice nods to Subaru.
Beatrice: “Their multiplication itself may be unlimited, but there is likely a ceiling to how many
hares there can be, in fact. So they cannot multiply beyond that, I suppose.”
Subaru: “Then, if we can finish off that ceiling all at once...”
Beatrice: “Theoretically, that will destroy it. ...But that presents its own difficulties, in fact.”
Subaru sees hope, but Beatrice makes a complicated expression.
Well, of course. There are enough hares to drown out everything in sight. If they had the magic to
burn everything in visible range then they might be able to destroy the Hare, but how much power
would it take to do it all in one second, and get all of them?
It's a violent plan akin to missile bombing the whole region. And if even one of them survives, they
will all instantly regenerate. The risk is far too great.
Subaru: “Then... okay. That's it.”
Beatrice: “You've thought of something, I suppose?”
Subaru: “It's me being utterly dependant on you yet again but yeah.”
Subaru watches the witchbeast multiply as he whispers into Beatrice's ear.
Beatrice lowers her gaze in thought, and nods.
Beatrice: “I've been thinking the same thing, in fact. But doing it would require...”
Subaru: “I know there's a bottleneck. However! You better not get the wrong idea, Beatrice!”
Beatrice: “—?”
Subaru: “It's not like we have to solve this problem on our own, yeah?”
Beatrice's eyes widen at this. She gives a quiet sigh, pitching over in Subaru's direction to set her
forehead on his chest.
Beatrice: “Truly, Subaru... you present some extraordinary solutions, in fact.”
Subaru: “I do promise to be such a thrillingly fresh and novel contractor that you'll never ever get
bored.”
Subaru shoots her a thumbs up, his teeth sparkling. Beatrice smiles wryly before looking up, her
face against his chest.
Beatrice: “Fine I suppose, let's do it in fact. But even Betty needs time to pull this off, I suppose.
Let's see you manage well over that period, in fact.”
311
Subaru: “Just pretend you're relaxing on a safe sturdy boat. It's what I'm doing.”
Beatrice: “We'll see who'll be doing the paddling, I suppose.”
Beatrice pushes away from Subaru's chest.
She takes a breath, closes her eyes, and begins focusing on escalating her magic.
Seeing this, Subaru psychs himself up and kicks off the snow.
The witchbeast's fangs click and clatter as it chases Subaru, running. Silhouettes come swooping for
his legs. But they're too slow. After these two days of butcheries, the Sizeable Hare looks wimpy.
Subaru: “Out of the way! Move it! I don't have the time to deal with you right now!”
Subaru dodges the fangs, kicks away the hares.
He incants, using crystal spears to force open a path as he charges through the clearing with
Beatrice cradled in his arms, sprinting back to the tomb.
Emilia: “Huh, wha, Subaru!?”
Emilia looks shocked as she witnesses Subaru's return.
Subaru skids to a stop beside her before placing Beatrice, her eyes closed, on the snowy ground
beside him and stroking her head.
Subaru: “Sorry, Emilia-tan! We're having some trouble pulling it off on our own!”
Emilia: “I-I mean, that's fine, but... what do we do now? Right, I'm going to—”
Subaru: “No, we have an idea for how to beat it. You don't have to use your suicide bomber
absolute death moves. Or actually just don't use them. It'll make all our efforts until now pointless.”
Emilia swallows her breath and stares intently at Subaru's face.
Did she seriously think he wouldn't figure it out? She seriously did, didn't she.
Of course Emilia would, if truly backed into a corner in a situation like this, bring harm to herself to
land the decisive blow. What an impossible girl.
'It's okay to hurt myself if it saves everyone?' Just stop.
Subaru: “It's best that everyone's safe and everyone's saved, duh.”
Emilia: “...Subaru.”
Subaru: “So Emilia-tan, I have kind of a crazy request. If it doesn't look feasible then I'll think on it
more, but if it looks feasible then I want to see your best. —Let's all win this together.”
Emilia: “—”
Emilia puts her hand to her chest, seeming to feel something about Subaru's statement, blinking
several times.
Subaru conjures crystal spears and fires them at the witchbeast horde to hold them in check, buying
time for Emilia to come to her decision. It does not end up taking long at all.
312
Emilia: “Alright. Let's do this, Subaru. I'm ready for anything.”
Says Emilia, steeling her resolve, her gaze determined.
Subaru pumps his fists as he glances back to her.
Subaru: “That's the spirit. Here we go!”
※ ※ ※ ※ ※ ※ ※ ※ ※ ※ ※
Subaru feels incredible swells of magic beside him, coming from both sides.
Emilia stands on his left, and Beatrice on his right.
Each of them holds one of Subaru's hands, linking the three of them together.
There was no real significance to them doing this. It's just to motivate Subaru.
In context of battle, you call 'motivation' 'morale'. And high morale is essential for dictating the tide
of battle.
Subaru: “Visualise, visualise, visualise!”
Subaru envisions the wicked, powerful, magical assault.
He creates pointed amethyst spears and bombards the expanse of approaching hares with them. He
fights his hardest, repeating volley after volley to keep the hares from reaching either themselves or
the tomb.
Subaru is not using his own mana to cast this magic. So he is casting without suffering any strain—
would be a complete misunderstanding.
He is getting the mana he needs to cast from Beatrice, but Subaru is the one regulating the magic.
He visualises the spears' force, their aim, their quantity, materializes them and fires them, then
instantly moves to the next attack.
He would be suffering even more bodily fatigue alongside this, were he an actual magician. He
cannot hope to imagine the immense burden and concurrent workload. He can agree with his lack of
talent for it.
The spears strike against the ground, shockwaves and detonations sending the hares flying as they
screech in protest. Their fangs click and chitter and click and chitter and click and with the howling
blizzard as accompaniment, it sounds like the cog-wheels of hell, or something to that effect.
The cogs on the grim conveyor to send Subaru's team to the guillotine press ever closer.
Subaru: “Meenya! Meenya! Ah, crap! Biting my tongue on this magic!”
While grumbling about the unpronounceable incantation, Subaru takes aim at the charging Hare.
He fires the conjured crystals, and the leading hare's head—goes untouched as the spear strikes the
ground before it, and the shockwave pushes it back into the mob.
The plan is in phase one.
Subaru is controlling the horde with his conjured spears, but he isn't killing them. They want to
avoid disruption to the ceiling, and having the hares multiply at some indefinite juncture.
He is keeping the Sizeable Hare at its ceiling while pinning it in place. Although,
313
Subaru: “If you're attracted to mana's smell, then there's no way you're prying your attention from
us.”
After all, there are two people here maintaining nigh-unwitnessed magnitudes of mana. And they're
both beautiful girls. Subaru, right now, has flowers in both hands. Anyone would envy him.
Subaru: “Visualize, visualize, visualize... come on, you gotta be jealous! Wanna try coming closer!”
Hums Subaru, not neglecting to taunt the animal.
Part of it is to inflame the enemy, but it's more about Subaru encouraging himself. If he feigns that
an extraordinary situation is an ordinary one, he can manage to keep himself going.
If he doesn't do this, he cannot assure himself steady knees. Both of his hands feel a warmth. With
this touch on his palms, he absolutely cannot show the pathetic side of himself.
Subaru: “Visualize, visualize, visualise...!”
Mutters Subaru over and over as he strains his eyes.
The horde of hares has pushed forward; there is a limit to how far Subaru can restrain them. But
preparations are not in place yet.
Not Emilia's, or Beatrice's, or Subaru's.
Emilia: “...Subaru.”
He feels someone squeeze his hand, and looks to find Emilia gazing at him, her eyes faintly open.
Her preparations are in order, then? She is smiling, awaiting Subaru's signal.
Subaru: “—hk”
Pushed onward by Emilia's gaze, Subaru strains his bloodshot eyes further.
The curtain of blustering blizzard is thick, constantly concealing and revealing the places he is
trying to see. But the sight of their wriggling, white forms does tell Subaru of the slight difference
between the witchbeast and the snowbanks.
—Just a little more, a tiny, right there, there, there, there!
Subaru grits his teeth. Waits for the moment.
Confirming that the front, the sides, all of it, everything is correct, Subaru's eyes shoot open.
Subaru: “Now, Emilia! Follow the lines!!”
Shouting, Subaru squeezes down on Emilia's hand.
Emilia's amethyst gaze focuses firmly to the front as she looks at the lines Subaru drew.
While he kept the Hare in check with conjured spears, Subaru had been simultaneously drawing
lines across the earth with mana. Using formless mana to gouge into the earth had been the utmost
in difficulty.
But Subaru, as talentless as people called him, overcame that ordeal by a combination of focus and
PRETENTIONS that far exceeded those of the ordinary person. The ones that disallowed him from
314
looking uncool around others, those pretentions.
He drew four lines in total.
Four long lines, that form a box around the mass of hares.
Lines that would tell Emilia where to aim.
Emilia: “Excellent, Subaru! You did sooo wonderful!”
Cheers Emilia at his beautiful set-up, saying things she would usually never say.
Emilia raises her right hand, Subaru's hand still in her grip, and places her half-frozen left hand atop
it. And, incants.
Emilia: “—Al Huma!!”
The multitude of magic surges as the world transforms in accordance to Emilia's canto.
Mana rushes to Emilia and Subaru's linked hands before shooting into the atmosphere, piercing
through the earth, and converging with Subaru's lines of mana.
—The earth bellows as something incredible occurs.
Subaru: “Woah...”
Says Subaru, astonished, as he watches what happens.
Well of course. Anyone witnessing this would react the same way.
Emilia's magic traces over the lines that Subaru drew—and all of the snow within the box starts
levitating.
All of the hares within the box remain atop the snow platform, but they have not noticed that these
tremors happened because the ground beneath them is floating.
It may be a limited space, but the floating platform is still about twenty by twenty meters.
This sight, of so many hares crowded together and shuddering on this platform, beautifully
demonstrates the supernatural nature of 'magic'.
Subaru: “Emilia!”
Emilia: “Got it! I'm not letting them get away!”
But if they stop here, then the Hare is just going to jump off the platform.
There is one more thing they have to do to keep it from escaping.
Emilia raises their linked hands up high—and swings them right down.
The floating snowfield rumbles. Surely, the Hare never imagined what would happen.
A roar, and a frigid blast of stabbing wind.
It showers over Subaru and the others as they keep their eyes fixated on the platform, to see the
results through.
—By the time the wind stops, the snowfield is vertically shut.
The left and right ends of Emilia's floating platform have folded to meet at the centre.
315
The ground has been shut in the same manner as a book, sealing the Hare inside the snow without
any means of escape.
Subaru hurriedly looks over the closed platform's surroundings. They missed—none. Movement—
nowhere.
All of the hares are in one place, trapped in an extraordinarily small area. With this,
Subaru: “The big one's all on you, Beatrice!”
Subaru calls to Beatrice, telling her that the secondary set-up is complete. Hearing this, and having
quietly chanted the canto the entire time, Beatrice's eyes open.
Seeing the sight before her, Beatrice laughs quietly.
It's not surprise or anything like that. A smile abounding with trust arises on her face,
Beatrice: “Here is the pinnacle of yin. —Al Shamac.”
The instant she murmurs the canto, shadow drowns out the world.
※ ※ ※ ※ ※ ※ ※ ※ ※ ※ ※
—For a moment, it is manhandled by something like vertigo.
But it really does only last for a moment.
The vertigo stops, and a shock impacts its feet. Then the bondage pressing on its body disappears. It
starts off by giving a big shake to get the snow off its fur.
It sniffs the air, looks around the area.
Its eyes, its nose, its ears, all get the better of it as they prioritize the hunt for prey. Its red eyes
glance about as it searches for sweet-smelling game.
Nothing. There had been prey so delectable that it made its stomach wrench painfully, right in front
of it, just a second ago. With tender flesh and sweet blood, prey that might sate this starvation even
temporarily had definitely been right there.
Its nose smells nothing. Its eyes see nothing. Its ears hear nothing.
The prey is gone. It looks around. Nowhere in sight.
Hunger instantly overwrites its disappointment. To distract itself from its hunger and urge to chew,
it decides to bite into the white mass beside to it.
It gnashes at it, shreds its flesh, slurps at its blood while clawing out its innards. It chews away to its
heart's content, swallows it down, and then notices that identical meals are unfolding all around it.
There's less prey now.
It doesn't feel like it's in danger, but in accordance with its survival instincts, it bites off the head of
another white mass that frantically consumes all around it. Bites into it, and swallows it down.
And this repeats. And repeats. Spurred on by endless hunger, it goes to the neighbouring prey, and
316
the prey neighbouring that, and the prey neighbouring that, and the prey neighbouring that, and the
prey neighbouring—.
Eventually, after devouring everything around, it is the only thing left.
It licks up the blood soaking the ground, leaving not a single scrap of gore or blood-soaked grass
left. Once it tidily cleans up the remains of the meal, it truly is alone.
But even with meat in its stomach, starvation far exceeding its body mass assaults it.
It cries out, teeth chattering, near to madness. Unending starvation, insatiable hunger. The
maddening lack of release, no matter how much it eats.
Mother must have felt this too.
For an instant, a mysterious thought passes through a mind dominated by hunger.
The indistinct thing had been a simple flash of emotion, nothing so cultivated as to reach language.
And it, too, vanishes eternally in the face of maddening hunger.
The creature trembles, trembles violently. It shrieks as it feels its innards churn about, and it
unconsciously creates another entity.
This sudden, new white mass tumbles back-first onto the ground, as if it's forgotten how to walk.
Every single one of its organs registers this thing prey, and it bites into the tumbling mass without
any hesitation.
It swallows it down without allowing it even to shriek. After eating, the hunger still torments it. And
following all this agonized struggling, another creature other than itself is born into the world.
And it repeats, and it repeats, the same thing going on and on and on and on.
It's alone now. Nothing else exists in this world. There are buildings, and forests, and earth, and air
and wind, but no prey. It's alone.
And it proceeds to eat.
Eventually, even IT is devoured by another stomach, and disappears.
The new lonely one repeats and repeats it all until it is that no longer. The world turns.
—Insatiable hunger is never to be sated.
※ ※ ※ ※ ※ ※ ※ ※ ※ ※ ※
The momentary presence of the incredible shadow makes Subaru swallow his breath.
Subaru: “—”
The black orb that Beatrice's canto created swallows the snowfield trapping the Hare that Emilia
sealed, then proceeds to shrink smaller and smaller, before eventually shrinking smaller than a
317
marble and silently vanishing.
Even Subaru, who does not know the theory behind this feat, understands what this means.
Al Shamac, the greatest of Shamac spells, is magic that affects space.
The magic swallowed the Hare and the snowfield, then blasted them all into another dimension.
Neither regeneration nor multiplication mean anything any more.
Because it's literally another world's issue.
Subaru: “I know I did... ask you to send them into an isolated space like the Forbidden Archive,
but...”
Beatrice: “Do I hear malcontent, I suppose?”
Subaru's voice trembles before the incredible feat, while Beatrice pouts beside him.
She puts her hands to her hips, quite displeased with Subaru's attitude.
Emilia: “Seriously, wow...”
The whole thing makes Emilia's eyes open wide as well.
Emilia is more learned in magic than Subaru, so her surprise is happening on another vector. Her
powers have probably settled in somewhat after half-freezing herself and using such immense
magic. Once she figures out how to control it, she'll probably be fine.
Subaru looks around, confirming that there is nothing where the Hare used to be.
Then he glances behind him, and confirms that the tomb is secure too. Peeking out from the tomb is
an expressionless mob of Leweses. Looks like the Lewes doubles have all managed to reach safety
too.
Roswaal is leaning against the wall beside the tomb's entrance, with Ram in his arms.
Ram's hand is touching Roswaal's cheek, and Subaru can see that Roswaal is crying.
Subaru: “—”
Witnessing that, Subaru feels the weight in his chest disappear.
There are still so many things that they have to talk about. Otto, Garfiel, and the others are still back
at the mansion. He does believe they're safe, but they need to meet up and talk. And on this side,
too. He has so many things to ask Emilia.
But somehow, it feels like everything is all right.
There are so many things he hasn't verified yet. But seeing Roswaal crying, and Ram smiling softly
as she watches him, makes Subaru feel that: hey, everything's all right.
Emilia: “Subaru, come on!”
Subaru takes his breather, until Emilia suddenly pokes his cheek.
Emilia smiles at Subaru when he looks back at her, and then gestures to the area behind him. Where
there Beatrice stands with her arms folded, still looking sulky.
Beatrice: “I believe that this ace deserves a few words, in fact.”
318
Beatrice puffs out her cheeks. Subaru replies with a nod.
And,
Beatrice: “Ah, eep!”
Subaru slips his hands under her arms and lifts her right up.
He ignores her adorable yelp, embracing her as he spins around on the spot,
Subaru: “You did it! Knew you could, I'm so in love with you, Beako!!”
Beatrice: “Wh—hold it! Sto—let me—let me go, I suppose! Betty isn't...”
Subaru: “Yes yes yes! You are adorable! Beako is wonderful! Beako is supreme! All hail Beako!”
Showing her in praise, Subaru spins round and around with Beatrice in his arms.
Beatrice's face flashes beet red as Emilia watches them frolic, her gaze awfully gentle.
The spirit and contractor, spinning and spinning in an energetic expression of delight—
Both: “Ah!”
—lose their footing at the last moment, and happily plunge face-first into the snow together.
319
INTERLUDE: EACH GIVES CONCESSION
Subaru: “—Aaand, done!”
Subaru sticks the two twigs into the heap of snow before him, then wipes the sweat from his brow.
It's an amateur work, thrown together in an hour, but he still has to be impressed at the results.
Murmurs of admiration spread through the onlooking crowd as well.
Subaru: “Yeah, I must have a talent for this stuff. If we're ever hurting for food money, we can make
it snow, and make it as the esteemed snow artists of the nation.”
Emilia: “Stop being so silly. I'm not going to make it snow to help you with that. ...But, it really
does look sooo good.”
Says Emilia with a white puff of breath as she sits on the stone steps, observing Subaru's work.
Reflected in her amethyst eyes is Subaru's snowman—but since labelling it as a 'snowman' wouldn't
quite describe it correctly, perhaps it's better to call it a 'snow sculpture.'
There are now about 20 sculptures of Puck crafted from the leftover snow in SANCTUARY. What had
compelled Subaru to make so many? Ask him, and he would only be able to answer with: copious
romanticism.
But it's making Emilia and SANCTUARY's people happy, so the shallow rationale will suffice.
???: “I'm sure that you're not trying to be, but you truly are an idiot, Barusu.”
Says someone else, judging Subaru harshly.
The speaker is a girl, seated on the steps with her head on Emilia's lap. She has dressed out of her
trademark maid uniform and currently wears a simple white outfit.
Her clothes burned as she wavered between life and death. While her face does look paler than
usual, neither her tone nor venom suffer for it. So everything's good.
Subaru: “The two of you keep ganging up to call dumb... I did put in quite a bit of work throughout
this whole mess, so can't you be nicer to me? I could use a little more commendation.”
Emilia: “Mm, you're right. Thank you sooo much, Subaru. But I was the one doing work when you
were away, so actually I'd like commendation too.”
Subaru: “The stuff you've started saying, Emilia-tan...”
Though, Emilia does deserve praise for protecting SANCTUARY during Subaru's absence. It's
uncertain whether the residents would have escaped the Hare had Emilia not instructed them to go
in the tomb. And had Emilia not cleared the TRIALS, there would've been nowhere to take shelter
anyway.
Neither is it certain that Subaru would have thought to use the tomb as a shelter. Since his thoughts
had been fixated on escaping before the snow came.
Subaru: “Well, we'll call it a happy mistake that the Men's Brigade came back and sparked your
motivation, Emilia-tan. ...Seriously, thank you.”
This is true for previous affairs too, but this whole series of events involved far too many gambles.
320
It feels like Subaru couldn't manage on his own, and constantly had others rescuing him. Even
though he'd decided to take the hardest parts upon himself, ideally.
Emilia: “But of course, though. If you do absolutely everything for me, Subaru, I'm going stop
knowing what I'm even doing here. You've done enough zipping around that it's okay for you to rest
a little.”
Subaru: “No it's just that when I want to help with all the brains and brawn I don't have, running
around like an idiot's all I can do.”
Emilia: “But that's going to change, yes?”
Says Emilia teasingly, suppressing a laugh as she strokes Ram's head. Subaru instantly understands,
and rubs his finger under his nose as he replies with a, “yeah.”
He made many mistakes, and others were constantly rescuing him, but he managed to save basically
everything he needed to. And he would never agonize over these issues alone again.
Subaru would no longer hesitate to rely on others, would not slack in his own efforts either, and has
people to give him a good kick in the ass when he needs it.
Subaru: “—”
Subaru looks up, shifting his gaze from the clearing to the tomb.
His gaze goes past Emilia as she sits on the steps, all the way to the mouth of the tomb. Inside that
place, its TRIAL mechanism absent, are two people.
What could they be discussing inside? It does prey on Subaru's mind, but,
Subaru: “Well, even I have enough tact not to interrupt them.”
There's a wealth of opportunities they have to speak, but they couldn't stand to wait.
Surely. They have mountains of things to discuss.
※ ※ ※ ※ ※ ※ ※ ※ ※ ※ ※
A girl and a man face each other with a transparent coffin between them.
Girl: “Mother...”
Murmurs the girl as she looks at the woman in the crystal coffin.
It feels like she's floating, like her feet aren't touching the ground. Some of it is from the remaining
rush of battle, some of it is from her feelings of loss and liberation from losing her old haunt, and
most of it is from the unreal sight before her.
She had never thought that she would see her mother again.
The woman in the coffin—the witch, Echidna—looks not at all different from Beatrice's memories.
Long, white, beautiful hair alongside her intelligent yet gentle features. It vividly revives memories
of how she smiled at Beatrice, though it only happened rarely.
321
Beatrice: “Betty... wasn't able to keep her promise to you, I suppose. I'm sorry.”
Beatrice strokes the coffin, beginning the four-hundred-year reunion with an apology.
When they parted, Echidna had instructed Beatrice to give her stockpile of knowledge to THEY. Had
given her abundant books to fill the Archive, and a gospel that told the future.
Beatrice no longer has either.
The gospel telling the future that Echidna desired of Beatrice, and all of the knowledge that Echidna
amassed, has departed the world as ashes.
Beatrice: “Betty never even met THEY... and the books have burned, in fact. I've done excessively
many things I must apologize for, I suppose.”
I'm a terrible daughter, thinks Beatrice.
A foolish daughter who could not achieve even one of her mother's requests, even with four
centuries. Now she is meeting her mother who she cannot even face, and should be apologizing
profusely, but—
???: “...You look raaaaaaaather more refreshed.”
Mutters the man across from her, easily disclosing her thoughts.
Beatrice glances up to see a man with long hair arise from the dim, smiling weakly. It's Roswaal.
He's supposed to be a familiar face, but Beatrice cannot keep herself from feeling offput by him.
Perhaps because his eyes, always crazed in pursuit of his goals ever since Beatrice had met him,
now look uncertain—and because he is missing is clown makeup, his face bare.
Beatrice: “You best me in terms of refreshed in fact, Roswaal. Making my presence without
cosmetics means violating the instructions from your predecessor, I suppose.”
Roswaal: “The clown make-up was a sort of war paint for me, yooooooou see. Wearing it let me
interact with others spiritedly, as though I were donning a mask. But there's sooooooooomething I
realised.”
Beatrice: “Yes?”
Roswaal: “That regardless of the make-up, I am aaaaaaaan absolute clown. So how meaningful is it,
truly, that I neglect my cosmetics?”
Beatrice: “I see, in fact.”
Beatrice nods as Roswaal gives a joking shrug. She fiddles with her pigtails in silence before going
on,
Beatrice: “Now,”
Beatrice: “You must have things to say to Mother, I suppose. Reunion with her has been your... has
been your family's deepest wish, in fact.”
Roswaal says nothing.
322
Beatrice: “You mark perhaps the tenth Roswaal since the progenitor who directly knew Mother, I
suppose. Lords of the Mathers family have been short-lived for generations, so the visitors to the
Archive shifted rather steadily, in fact. ...You've been different ever since childhood, I suppose.”
Beatrice may not have been deeply involved in the history of the Mathers Family, but she did watch
from aside how their affairs progressed.
The first Roswaal was Echidna's only student. Though he lost almost all of his magical ability in his
fight with the warlock Hector, he did not give up on being Echidna's student.
He frequented the Archive even after Echidna's death, disregarding the dazed Beatrice as he
obsessively searched and searched and searched for something, and likely gave that something to
his descendant before dying.
Ever since, all the descendants from Roswaal's line demonstrated magical capabilities bordering on
those of their progenitor, and the Mathers family expanded.
Now is the current Roswaal. The man standing in front of Beatrice.
This Roswaal exhibited the most supreme talent out of all the Roswaals yet. He was such a genius
that, secretly, even Beatrice had to shiver.
His power eclipsed that of the progenitor, who Echidna had singled out personally, and could have
done anything he wanted with his claim as one of the strongest magicians in the world.
Beatrice: “You had all that talent, and you still failed to escape the Mathers' curse, in fact. Your
family has been entranced with thoughts of reuniting with my deceased Mother, the path a cruel one
you fixedly walked... I do sympathise with you somewhat, I suppose.”
Roswaal: “Do you? But how are you and we any different? You spent four centuries bound by the
words of your deceased mother. It's identical. Or rather, unlike my family's shifting over the
generations, you suffered pain in solitude beyond what anyone can empathise. We did what we
needed to strive forward toward our goal. You simply suffered in place.”
Says Roswaal, his words even graver than Beatrice's.
In the end, they're both bad, she thinks.
Roswaal's family has inherited the same feelings over lives upon short lives, in pursuit of a single
reunion.
Beatrice had been trapped in an empty cage for her immortal life, waiting for the day that she could
fulfil her promise.
An objective onlooker would see them as equally foolish clowns.
The two glare at each other in silence.
But their silent competition ends when Roswaal averts his gaze.
Roswaal: “This is a tedious argument. When two fools point at the other whilst mocking their
foolishness, we begin crossing the boundaries of vain comedy.”
Beatrice: “...You are correct there, in fact.”
Roswaal: “Do you mind me asking something?”
Roswaal raises his finger. Beatrice silently looks up, expressing her consent by neglecting to reject
323
him.
Roswaal looks down at Echidna as she sleeps in the coffin.
Roswaal: “Did Subaru-kun manage to be your THEY?”
The word 'they' makes Beatrice swallow her breath. She has never spoken directly with Roswaal
about THEY. But Beatrice does not think it strange for him to learn about her from sources outside
her knowledge.
And thinking back on it, the people who had visited the Archive until now had ultimately been
brought there by Roswaals up to the previous generation. The Roswaals easily could have heard the
story from them and passed it on to their descendants.
And frankly you could say that even Subaru had been brought there by Roswaal.
—Not that Subaru would accept it if you told him so.
Roswaal: “...Why are you laughing?”
Beatrice: “—Ah. Sorry, I suppose. I'm not laughing at you, Roswaal, in fact. It just made me
imagine something amusing, I suppose.”
It amuses Beatrice how she managed to figure, with pinpoint accuracy, what the black-haired man
would say. He's just that straightforward, perhaps. She doesn't want to think any further into it than
that.
Either way, Beatrice shakes her head.
Beatrice: “That man is... Subaru is not fit to be my THEY, in fact.”
Roswaal: “...Hrm.”
Beatrice: “Subaru isn't nearly qualified to inherit Mother's archive of knowledge, I suppose. He has
no mind to educate himself with the knowledge or use it for his purposes, and he lacks the
fundamental background to do either, in fact. And he looks dumb and he's flimsy and he's useless at
magic and his legs are short, I suppose. He isn't Betty's awaited THEY in any capacity.”
Roswaal: “That soooooooounds quiiiiiiiiiite the harsh opinion.”
Beatrice: “Exactly, I suppose, Betty is harsh, in fact. And so I rebuffed every opportunity that came
to me over these four centuries. ...I rebuffed them with THEY, in fact.”
Beatrice does feel something like guilt towards all those who tried to take her out of the Archive,
when she thinks of it now. Not all of them had reached out to Beatrice while thinking only in their
own interests. Some of them had spoken kindly to her.
But Beatrice cast away every single hand that reached for her.
Beatrice: “I know that I should've chosen THEY, I suppose. That I should have faced everyone who
called to me, individual by individual, and properly thought out my answer, in fact. I was meant to
choose someone suitable to inherit the Archive, Echidna's knowledge... that has to be what it was, I
suppose.”
Roswaal: “However, you say that the one you picked, Subaru-kun, is unfit to be THEY?”
324
Beatrice: “I do, in fact. There's no issue, I suppose. Betty's choice is Subaru, in fact. Not THEY. I
chose Subaru, I suppose.”
Beatrice sees how Roswaal's breath catches and his eyes open wide.
It must be a difficult answer for him to accept, considering how he has devoted himself to Echidna.
Beatrice had been in the exact same position as him until only a moment ago. She understands how
Roswaal feels so much that it hurts.
And because she understands, she has to explain it at length.
Beatrice: “Subaru laughed at me when I begged him to be they, in fact. He crowed that he could
make me happier than someone I've never seen, I suppose.”
Roswaal: “What a... prideful thing to say.”
Beatrice: “I don't dislike that forcefulness, in fact.”
Rather than enticing her with polite speech, explaining to her what she should do, and clarifying
how he would use Echidna's knowledge, he was utterly candid.
Roswaal: “But no matter what he preaches, Subaru-kun will not place you in first. It's obvious
simply by looking at him... you must already recognize this.”
Beatrice: “You don't seem to understand, I suppose, Roswaal.”
Roswaal: “I don't?”
Beatrice: “Betty didn't leave the Archive because she's Subaru's number one, in fact. I left the
Archive because I want Subaru to be my number one, I suppose.”
Choose me, he said.
I'll be too lonely to live without you, he said.
Convenient prattle, she thought. Pleasant bullshit, she thought.
But it swayed Beatrice's heart. It resonated. It took her heart, sealed stuck in one place for four
hundred years, and jolted it.
Now that she knows the freedom she felt the instant she took his hand and left the Archive, and how
it almost brought her to tears, her heart just won't stop.
Beatrice: “Abandoning my post may disqualify me as Mother's spirit, but I don't mind, in fact. Betty
is contractor Natsuki Subaru's spirit, I suppose. My regret and shame for that... is gone, I suppose.”
Roswaal might consider it a betrayal.
He had also been bound for four centuries by Echidna's curse, and perhaps Beatrice's announcement
that she escaped it first was a betrayal to him. She didn't escape by fulfilling her role, but by
abandoning it.
If she's going to face her Mother, or face Roswaal, she has to rationalize that.
Beatrice: “—”
325
Her heart is already resolved. She has already taken that hand.
Beatrice is going to live a life so vivid it never fades to sepia. Something so intense that, no matter
how the years drag on, she never forgets those important to her.
So she keeps silent, waiting for Roswaal to reply.
Roswaal: “You don't have to brace yourself. I'm not the Witch Echidna's spokesman. I have no right
to intrude on your answer, whatever it may be. Just do what you wish.”
Beatrice: “Roswaal...”
Roswaal: “And even had you not abandoned them, you would have never fulfilled Echidna's orders.
Because I would have prioritised my own desires over you and sacrificed you. If we are speaking of
betrayals, that constitutes a significant one.”
Beatrice: “—”
Penitently, Roswaal acknowledges his wrongdoings for what happened in the mansion.
Just as Beatrice had realised in the Archive, Roswaal was the one plotting to take Beatrice's life. She
had reasoned it the result of the gospel. Though she doesn't see how it all connects.
Beatrice: “Roswaal. What happened to your gospel, I suppose?”
Roswaal: “...It's burned to nothing. Thanks to a wicked maid who deeeeeeefied her master. The
future is in ashes now. And perhaps eeeeeeeeeeverything is.”
Beatrice: “Everything is hollow and the future lies imperceptible... would be something, but you
look considerably refreshed, in fact.”
Roswaal: “—I wonder iiiiiiiiiif I am.”
Roswaal casts his gaze down in reply to Beatrice's perfect repeat of their previous conversation. He
reaches for Echidna in the coffin, for her untouchable fingertips.
Roswaal: “I'm sad that I've lost the definite path to the answer I seek, and scared. ...But perhaps I'm
also joyed to read a story that I never could have read before. Though, I haven't felt so in over four
centuries now, so I can't tell whether it's legitimate.”
Beatrice: “...?”
Beatrice scrunches her brows. Something feels off about that statement.
Seeing her confusion makes Roswaal smile slightly.
Roswaal: “We haven't spoken nearly enough,”
He says with some self-deprecation.
Roswaal: “You can't dismiss it aaaaaaas being beyond our control. At first there was need to be
blindly fixated, but after that we did have time. We spent so much time in the same mansion. And
even so, even though we had seen the same things, I kept avoiding you, like I was scared of talking
326
    """
    
    print(len(text))
    
    # encodedMessage, huffTree = HuffmanEncoding.encode(text)
    # print(encodedMessage)
    
    # Measure time and memory consumption
    Testing.measurePerformance(text)
    